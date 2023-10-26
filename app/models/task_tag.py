from flask_login import UserMixin
from sqlalchemy import Null
from sqlalchemy.orm import relationship

from app.extensions import db
# from app.models.task import Task
from app.models.tag import Tag


# The rudimental types have “CamelCase” names such as String, Numeric, Integer, and DateTime.
# Examples of UPPERCASE types include VARCHAR, NUMERIC, INTEGER, and TIMESTAMP, which inherit directly from
# the previously mentioned “CamelCase” types String, Numeric, Integer, and DateTime, respectively.


class TaskTag(UserMixin, db.Model):
    __tablename__ = "task_tag"
    id = db.Column(db.Integer, primary_key=True)

    task_id = db.Column(db.Integer, db.ForeignKey('task.id'), primary_key=True)
    task = relationship(argument='Task', back_populates='tag', foreign_keys=[task_id])

    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'), primary_key=True)
    tag = relationship(argument='Tag', back_populates='task', foreign_keys=[tag_id])

    # def __repr__(self):
    #     return f'<Task Tag "{self.title}">'
