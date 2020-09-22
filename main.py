import json
from flask_cors import CORS
from flask_login import LoginManager, current_user, login_user, login_required, logout_user
from flask import Flask, request, render_template, redirect, flash, url_for
from flask_jwt import JWT, jwt_required, current_identity
from sqlalchemy.exc import IntegrityError
from flask_socketio import SocketIO, send, emit, disconnect, join_room
from datetime import timedelta
import functools

from models import db, Message, Chat, User

''' Begin boilerplate code '''

''' Begin Flask Login Functions '''

login_manager = LoginManager()
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

''' End Flask Login Functions '''

def create_app():
  app = Flask(__name__, static_url_path='')
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
  app.config['SECRET_KEY'] = "MYSECRET"
  CORS(app)
  login_manager.init_app(app) # uncomment if using flask login
  db.init_app(app)
  return app

app = create_app()
socketio = SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")


app.app_context().push()

''' End Boilerplate Code '''


''' Messenger Setup '''

sessionMap = {}

def get_room(sender, receiver):
  list = [sender, receiver]
  list.sort()
  return '#'.join(list)

@socketio.on('join_room')
def handle_join_room(data):
  sender = current_user.username
  room = get_room(sender, data['to'])
  join_room(room)
  send({ 'text':'Now messaging '+ data['to'], 'from':'System', 'to':sender})

@socketio.on('message')
def handle_message(message):
  print('received: ' + str(message))
  message['from'] = current_user.username
  room = get_room(message['from'], message['to'])
  send(message, room=room)

@socketio.on('connect')
def test_connect():
    emit('my response', {'data': 'Connected'})

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')

# define @authenticated_only decorator for socket connections
def authenticated_only(f):
    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        if not current_user.is_authenticated:
            disconnect()
        else:
            return f(*args, **kwargs)
    return wrapped

''' End Messenger Setup '''

@app.route('/login', methods=['GET'])
def login():
  logout_user()
  user = request.args.get('sender')
  user_obj = User.query.filter_by(username=user).first()
  if (user_obj):
    login_user(user_obj)
    return redirect(url_for('index'))
  return 'User Does not exist'

@app.route('/create/<user>/<password>')
def create(user, password):
  new_user = User(username=user)
  new_user.set_password(password)
  db.session.add(new_user)
  db.session.commit()
  return user+' created '
  

@app.route('/')
def index():
  return render_template('app.html', user=current_user, authenticated = current_user.is_authenticated)

if __name__ == '__main__':
  socketio.run(app, host='0.0.0.0', port=8080, debug=True)
