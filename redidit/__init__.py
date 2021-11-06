from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

def create_app():
	app = Flask(__name__)
	app.config['SECRET_KEY'] = 'secret-key-goes-here'
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	app.config.from_object(__name__)

	CORS(app, resources={r'/*':{'origins':'*'}})

	login_manager = LoginManager()
	login_manager.login_view = 'auth.login'
	login_manager.init_app(app)

	from .models import User
	from .models import Post

	@login_manager.user_loader
	def load_user(user_id):
		return User.query.get(int(user_id))

	#blueprint for auth
	from .auth import auth as auth_blueprint
	app.register_blueprint(auth_blueprint)

	#blueprint for main
	from .main import main as main_blueprint
	app.register_blueprint(main_blueprint)

	#blueprint for posts
	from .post import post as post_blueprint
	app.register_blueprint(post_blueprint)

	#blueprint for community
	from .community import community as community_blueprint
	app.register_blueprint(community_blueprint)

	#blueprint for messages
	from .message import message as message_blueprint
	app.register_blueprint(message_blueprint)

	with app.test_request_context():
		db.init_app(app)
		db.create_all()
		db.session.commit()
		from . import template_filters

	return app
