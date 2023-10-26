from flask_login import UserMixin
from sqlalchemy import Null
from sqlalchemy.orm import relationship

from app.extensions import db
from app.models.comment import Comment
# from app.models.task import Task
# from app.models.user import User


# The rudimental types have “CamelCase” names such as String, Numeric, Integer, and DateTime.
# Examples of UPPERCASE types include VARCHAR, NUMERIC, INTEGER, and TIMESTAMP, which inherit directly from
# the previously mentioned “CamelCase” types String, Numeric, Integer, and DateTime, respectively.


class Activity(UserMixin, db.Model):
    __tablename__ = "activity"
    id = db.Column(db.Integer, primary_key=True)

    # user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, default=0)
    executorId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, default=0)
    # executor = relationship('User', back_populates='activities', foreign_keys=[executorId])
    executor = relationship('User', foreign_keys=[executorId])

    createdBy = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, default=0)
    # creator = relationship(argument='User', back_populates='created_activities', foreign_keys=[createdBy])
    creator = relationship(argument='User', foreign_keys=[createdBy])

    updatedBy = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, default=0)
    # updator = relationship(argument='User', back_populates='updated_activities', foreign_keys=[updatedBy])
    updator = relationship(argument='User', foreign_keys=[updatedBy])

    taskId = db.Column(db.Integer, db.ForeignKey('task.id'), nullable=False, default=0)
    # task = relationship('Task', back_populates='activities', foreign_keys=[taskId])
    task = relationship('Task', foreign_keys=[taskId])

    title = db.Column(db.String(512), nullable=False, default=Null)
    description = db.Column(db.String(2048), nullable=False, default=Null)
    status = db.Column(db.Integer, nullable=False, default=Null)
    hours = db.Column(db.Integer, default='09121234567')
    createdAt = db.Column(db.DateTime, nullable=False)
    updatedAt = db.Column(db.DateTime, nullable=False)
    plannedStartDate = db.Column(db.DateTime, nullable=False)
    plannedEndDate = db.Column(db.DateTime, nullable=False)
    actualStartDate = db.Column(db.DateTime, nullable=False)
    actualEndDate = db.Column(db.DateTime, nullable=False)
    content = db.Column(db.String(512), nullable=False)

    comments = relationship('Comment', back_populates='activity')

    def __repr__(self):
        return f'<Activity "{self.title}">'
