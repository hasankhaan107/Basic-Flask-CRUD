from sqlalchemy import inspect
from datetime import datetime

from .. import db

class Project(db.Model):
    __tablename__ = 'projects' 

    id = db.Column(db.String(50), primary_key=True, nullable=False, unique=True)
    title = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=True)
    completed = db.Column(db.Boolean, default=False)
    created = db.Column(db.DateTime(timezone=True), default=datetime.now)
    updated = db.Column(db.DateTime(timezone=True), default=datetime.now, onupdate=datetime.now)

    # Convert a SQLAlchemy project model instance into a dictionary representation
    def toDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }