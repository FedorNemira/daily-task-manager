from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), unique=False, nullable=True)
    password_hash = db.Column(db.String(250))
    email = db.Column(db.String(300), unique=False, nullable=True)
    active = db.Column(db.Boolean, default=False, nullable=False)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns if c.name != 'password_hash'}