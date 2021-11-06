# to do
from flask import Blueprint, render_template
from flask_login import current_user
from .models import Message
from . import db

message = Blueprint('message', __name__)

@message.route('/messages')
def messages():
	return render_template('messages.html')
