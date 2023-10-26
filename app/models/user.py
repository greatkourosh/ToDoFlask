from flask_login import UserMixin
from sqlalchemy import Null
from sqlalchemy.orm import relationship
from app.extensions import db
from app.models import role
# from app.models.activity import Activity
from app.models.task import Task


# The rudimental types have “CamelCase” names such as String, Numeric, Integer, and DateTime.
# Examples of UPPERCASE types include VARCHAR, NUMERIC, INTEGER, and TIMESTAMP, which inherit directly from
# the previously mentioned “CamelCase” types String, Numeric, Integer, and DateTime, respectively.

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)

    # roleId = db.Column(db.Integer, nullable=False, default=0)
    roleId = db.Column(db.Integer, db.ForeignKey('role.id'))
    role = relationship(argument='Role', back_populates='users', foreign_keys=[roleId])

    firstName = db.Column(db.String(50), nullable=False, default=Null)
    lastName = db.Column(db.String(50), nullable=False, default=Null)
    username = db.Column(db.String(50), nullable=False, unique=True)
    mobile = db.Column(db.String(50), unique=True, default='09121234567')
    # db.Column('mobile', db.String(50), default='09121234567')
    email = db.Column(db.String(50), unique=True)
    # password = db.Column(db.String(100), nullable=False)
    passwordHash = db.Column(db.String(32), nullable=False)
    registeredAt = db.Column(db.DateTime, nullable=False)
    lastLogin = db.Column(db.DateTime, default=Null)
    intro = db.Column(db.String(10), default=Null)
    profile = db.Column(db.String(50), default=Null)

    # tasks = relationship('Task', back_populates='executorId', foreign_keys=[Task.executor])
    # created_tasks = relationship('Task', back_populates='creatorId', foreign_keys=[Task.creator])
    # updated_tasks = relationship('Task', back_populates='updatorId', foreign_keys=[Task.updator])

    # activities = relationship(argument='Activity', back_populates='executor')
    # activities = relationship('Activity', back_populates='user')
    # created_activities = relationship(argument='Activity', back_populates='creator')
    # updated_activities = relationship(argument='Activity', back_populates='updater')

    def __repr__(self):
        return f'<Post "{self.firstName}">'
