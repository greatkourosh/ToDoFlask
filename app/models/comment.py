from flask_login import UserMixin
from sqlalchemy import Null
from sqlalchemy.orm import relationship

from app.extensions import db
# from app.models.activity import Activity
# from app.models.task import Task


# The rudimental types have “CamelCase” names such as String, Numeric, Integer, and DateTime.
# Examples of UPPERCASE types include VARCHAR, NUMERIC, INTEGER, and TIMESTAMP, which inherit directly from
# the previously mentioned “CamelCase” types String, Numeric, Integer, and DateTime, respectively.


class Comment(UserMixin, db.Model):
    __tablename__ = "comment"
    id = db.Column(db.Integer, primary_key=True)

    taskId = db.Column(db.Integer, db.ForeignKey('task.id'), nullable=False, default=0)
    task = relationship('Task', back_populates='comments')

    activityId = db.Column(db.Integer, db.ForeignKey('activity.id'), nullable=False, default=0)
    activity = relationship('Activity', back_populates='comments')

    title = db.Column(db.String(512), nullable=False, default=Null)
    createdAt = db.Column(db.DateTime, nullable=False)
    updatedAt = db.Column(db.DateTime, nullable=False)
    content = db.Column(db.String(512), nullable=False)

    def __repr__(self):
        return f'<Comment "{self.title}">'
