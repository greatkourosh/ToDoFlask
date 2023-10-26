from flask_login import UserMixin
from sqlalchemy import Null
from sqlalchemy.orm import relationship

from app.extensions import db
# from app.models.user import User
from app.models.task_meta import TaskMeta
from app.models.task_tag import TaskTag
from app.models.activity import Activity
from app.models.comment import Comment

# The rudimental types have “CamelCase” names such as String, Numeric, Integer, and DateTime.
# Examples of UPPERCASE types include VARCHAR, NUMERIC, INTEGER, and TIMESTAMP, which inherit directly from
# the previously mentioned “CamelCase” types String, Numeric, Integer, and DateTime, respectively.


class Task(UserMixin, db.Model):
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True)
    # userId = db.Column(db.Integer, nullable=False, default=0)

    executorId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, default=0)
    # executor = relationship(argument='User', back_populates='tasks', foreign_keys=[executorId])
    executor = relationship(argument='User', foreign_keys=[executorId])

    createdById = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, default=0)
    # creator = relationship(argument='User', back_populates='created_tasks', foreign_keys=[createdById])
    creator = relationship(argument='User', foreign_keys=[createdById])

    updatedById = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, default=0)
    # updator = relationship(argument='User', back_populates='updated_tasks', foreign_keys=[updatedById])
    updator = relationship(argument='User', foreign_keys=[updatedById])

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

    metas = relationship('TaskMeta', back_populates='task')
    tag = relationship(argument='TaskTag', back_populates='task')
    activities = relationship(argument='Activity', back_populates='task')
    comments = relationship(argument='Comment', back_populates='task')

    def __repr__(self):
        return f'<Task "{self.title}">'
