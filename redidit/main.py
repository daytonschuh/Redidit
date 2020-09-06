from flask import Blueprint, render_template, g, session
from flask_login import login_required, current_user
from . import db
import sqlite3

main = Blueprint('main', __name__)

@main.route('/')
def index():
	g.db = sqlite3.connect("project/db.sqlite")
	cur = g.db.execute("SELECT * FROM post LIMIT 5")
	posts = [dict(post_id=row[0], title=row[1], body=row[2], upvotes=row[3], downvotes=row[4], author=row[5]) for row in cur.fetchall()]

	g.db.close()
	return render_template('index.html', posts=posts)


@main.route('/profile')
@login_required
def profile():
	return render_template('profile.html', name=current_user.name)
