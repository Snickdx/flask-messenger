from . import db
import datetime

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    text = db.Column(db.String(300), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    chat = db.Column(db.Integer, db.ForeignKey('chat.id'), nullable=False) 

    def toDict(self):
        return{
            'id': self.id,
            'student': self.student,
            'created': self.created.strftime("%m/%d/%Y, %H:%M:%S")
        }
