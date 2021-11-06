from redidit import community
from flask import Blueprint, render_template, g, request
from flask_login import current_user
from .models import User
import sqlite3

main = Blueprint('main', __name__)

@main.route('/')
def index():
	g.db = sqlite3.connect("redidit/db.sqlite")
	cur = g.db.execute("SELECT * FROM post LIMIT 5")
	posts = [dict(id=row[0], title=row[7], body=row[1], upvotes=row[2], downvotes=row[3],
		author=row[4], creation_datetime=row[5], nsfw_flag=row[6], community_id=row[8])
		for row in cur.fetchall()]
	cur = g.db.execute("SELECT * FROM community WHERE community_id=1")
	communities = [dict(community_id=row[0], community_name=row[1]) for row in cur.fetchall()]
	g.db.close()
	return render_template('index.html', posts=posts, communities=communities)


@main.route('/profile', methods=['GET'])
def profile():
	username = request.args.get('username')

	if(username is None):
		username = current_user.username

	user = User.query.filter_by(username=username).first()

	return render_template('profile.html', user=user)

@main.route('/search', methods=['GET','POST'])
def search():
	g.db = sqlite3.connect("redidit/db.sqlite")
	query = request.args.get('search')
	req_search = g.db.query.filter_by(query)
	return render_template('search.html', req_search=req_search)