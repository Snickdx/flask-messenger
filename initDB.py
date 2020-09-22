from main import app, db, User


db.create_all(app=app)

user = User(username='bob')
user.set_password('bobpass')
db.session.add(user)
db.session.commit()

print('database initialized!')