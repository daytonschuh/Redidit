from flask import Blueprint, render_template, redirect, url_for, request, flash, g, session
from flask_login import current_user
from .models import Post
from . import db
import sqlite3

post = Blueprint('post', __name__)

@post.route('/create_post')
def create():
	return render_template('create_post.html')

@post.route('/create_post', methods=['POST'])
def create_post():

	# If not logged in, flash message
	if current_user.get_id() is None:
		flash('You must be logged in to create a post!')
		return redirect(url_for('post.create'))

	title = request.form.get('title')
	body = request.form.get('body')
	author = current_user.username

	new_post = Post(title=title, body=body, author=author)

	db.session.add(new_post)
	db.session.commit()

	return redirect(url_for('main.index'))


@post.route('/view_post', methods=['GET'])
def view_post():
	# Get post_id for query
	post_id = request.args.get('post_id')

	# Make the query
	post = Post.query.filter_by(post_id=post_id).first()

	# Return the page
	return render_template('view_post.html', post=post)


@post.route('/delete_post', methods=['POST'])
def delete_post():
	# Get post_id for query
	post_id = request.form.get('post_id')

	# Make the query
	post = Post.query.filter_by(post_id=post_id).first()

	# If it exists, delete
	if post:
		db.session.delete(post)
		db.session.commit()

	# Go home
	return redirect(url_for('main.index'))
