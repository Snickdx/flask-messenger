from . import db
import datetime

class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) 
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    messages = db.relationship('Message', backref='user', lazy=True) 

    def toDict(self):
        return{
            'id': self.id,
            'student': self.student,
            'created': self.created.strftime("%m/%d/%Y, %H:%M:%S")
        }
