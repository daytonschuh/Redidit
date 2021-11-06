from flask_login import UserMixin, AnonymousUserMixin
from sqlalchemy_utils import ScalarListType
from . import db
from datetime import datetime

class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True) #required to identify
	username = db.Column(db.String(30), unique=True)
	email = db.Column(db.String(100), unique=True)
	password = db.Column(db.String(100))
	fname = db.Column(db.String(100))
	lname = db.Column(db.String(100))
	karma = db.Column(db.Integer)
	following = db.Column(db.String)
	nsfw_flag = db.Column(db.Boolean, default=False)
	communities = db.Column(ScalarListType(int))

class AnonymousUser(AnonymousUserMixin):
	id = None

class BaseTextClass():
	id = db.Column(db.Integer, primary_key=True)
	body = db.Column(db.String(1024))
	upvotes = db.Column(db.Integer, default=0)
	downvotes = db.Column(db.Integer, default=0)
	author = db.Column(db.String)
	creation_datetime = db.Column(db.DateTime, default=datetime.now) # anything <1h displayed in minutes, <24h display hours, <1 month display days, <1 year display months, >=1 year display years
	nsfw_flag = db.Column(db.Boolean, default=False)
	# awards = db.Column(db.ARRAY)

class Post(db.Model, BaseTextClass):
	title = db.Column(db.String(50))
	community_id = db.Column(db.Integer, db.ForeignKey('community.community_id'), default=1)

class Message(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	body = db.Column(db.String(1024))
	reaction = db.Column(db.String(20))
	msg_from = db.Column(db.String(30))
	msg_to = db.Column(db.String(30))

class Community(db.Model):
	community_id = db.Column(db.Integer, primary_key=True)
	community_name = db.Column(db.Integer, unique=True)
	nsfw_flag = db.Column(db.Boolean, default=False)
