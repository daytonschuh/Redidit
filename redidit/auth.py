from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		email = request.form.get('email')
		password = request.form.get('password')
		remember = True if request.form.get('remember') else False

		user = User.query.filter_by(email=email).first()

		# Does the user exist?
		# Does the password match?
		if not user or not check_password_hash(user.password, password):
			flash('Please check your login details and try again.')
			return redirect(url_for('auth.login'))

		# We passed the checks!
		login_user(user, remember=remember)
		return redirect(url_for('main.profile'))

	return render_template('login.html')

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
	if request.method == 'POST':
		email = request.form.get('email')
		fname = request.form.get('fname')
		lname = request.form.get('lname')
		password = request.form.get('password')
		username = request.form.get('username')

		email_exists = User.query.filter_by(email=email).first()
		username_taken = User.query.filter_by(username=username).first()

		# Check all fields
		if email_exists:
			flash('Email address already exists!')
			return redirect(url_for('auth.signup'))

		if username_taken:
			resp = jsonify('<span style=\'color:red;\'>Username unavailable</span>')
			resp.status_code=200
			return resp
			#flash('Username taken!')
			#return redirect(url_for('auth.signup'))

		if len(username) < 5:
			flash('Username requires at least 5 characters!')
			return redirect(url_for('auth.signup'))

		#if email does not match *@*.* expression:
		#	flash('Please check email format!')
		#	return redirect(url_for('auth.signup'))

		#if password != conf_password:

		new_user = User(username=username, email=email, fname=fname, lname=lname, password=generate_password_hash(password, method='sha256'), karma=0)

		db.session.add(new_user)
		db.session.commit()

		return redirect(url_for('auth.login'))

	return render_template('signup.html')

@auth.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('main.index'))

@auth.route('/delete_user', methods=['POST'])
@login_required
def delete_user():
	email = request.form.get('email')
	user = User.query.filter_by(email=email).first()
	if user:
		db.session.delete(user)
		db.session.commit()

	return redirect(url_for('main.index'))
