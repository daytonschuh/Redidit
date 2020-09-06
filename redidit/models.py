from flask_login import UserMixin, AnonymousUserMixin
from . import db

class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True) #required to identify
	username = db.Column(db.String(30), unique=True)
	email = db.Column(db.String(100), unique=True)
	password = db.Column(db.String(100))
	name = db.Column(db.String(100))
	karma = db.Column(db.Integer)

class AnonymousUser(AnonymousUserMixin):
	id = None

class Post(db.Model):
	post_id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(50))
	body = db.Column(db.String(1024))
	upvotes = db.Column(db.Integer, default=0)
	downvotes = db.Column(db.Integer, default=0)
	author = db.Column(db.String, foreign_key=True)
