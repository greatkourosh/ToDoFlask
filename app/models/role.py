from flask_login import UserMixin
from sqlalchemy import Null
from sqlalchemy.orm import relationship

from app.extensions import db


# The rudimental types have “CamelCase” names such as String, Numeric, Integer, and DateTime.
# Examples of UPPERCASE types include VARCHAR, NUMERIC, INTEGER, and TIMESTAMP, which inherit directly from
# the previously mentioned “CamelCase” types String, Numeric, Integer, and DateTime, respectively.


class Role(UserMixin, db.Model):
    __tablename__ = "role"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(75), nullable=False, default='Admin', unique=True)

    users = db.relationship(argument='User', back_populates='role')
    # users = db.relationship('User', back_populates='role')

    def __repr__(self):
        return f'<Role "{self.title}">'
