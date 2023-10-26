from flask_login import UserMixin
from sqlalchemy import Null
from sqlalchemy.orm import relationship

from app.extensions import db
# from app.models.task_tag import TaskTag


# The rudimental types have “CamelCase” names such as String, Numeric, Integer, and DateTime.
# Examples of UPPERCASE types include VARCHAR, NUMERIC, INTEGER, and TIMESTAMP, which inherit directly from
# the previously mentioned “CamelCase” types String, Numeric, Integer, and DateTime, respectively.


class Tag(UserMixin, db.Model):
    __tablename__ = "tag"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(75), nullable=False)
    slug = db.Column(db.String(100), nullable=False)

    task = relationship('TaskTag', back_populates='tag')

    def __repr__(self):
        return f'<Tag "{self.title}">'
