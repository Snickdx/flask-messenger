from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from .chat import Chat
from .message import Message
from .user import User