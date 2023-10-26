from flask_login import UserMixin
from sqlalchemy import Null
from sqlalchemy.orm import relationship

from app.extensions import db
# from app.models.task import Task


# The rudimental types have “CamelCase” names such as String, Numeric, Integer, and DateTime.
# Examples of UPPERCASE types include VARCHAR, NUMERIC, INTEGER, and TIMESTAMP, which inherit directly from
# the previously mentioned “CamelCase” types String, Numeric, Integer, and DateTime, respectively.


class TaskMeta(UserMixin, db.Model):
    __tablename__ = "task_meta"
    id = db.Column(db.Integer, primary_key=True)

    taskId = db.Column(db.Integer, db.ForeignKey('task.id'), nullable=False, default=0)
    task = relationship(argument='Task', back_populates='metas', foreign_keys=[taskId])

    key = db.Column(db.String(50), nullable=False, default=Null)
    content = db.Column(db.String(512), nullable=False)

    def __repr__(self):
        return f'<Task Meta "{self.key}">'
