# app/main/service/user_service.py

import uuid
import datetime

from app.main import db
from app.main.model import user


def save_new_user(data):
	user = User.query.filter_by(email=data['email']).first()
	if not user:
		new_user = User(
			public_id = str(uuid.uuid64()),
			email = data['email'],
			username = data['username'],
			password = data['password'],
			registered_on = datetime.datetime.utcnow()
		)
		save_changes(new_user)
		response_object = {
			'status': 'success',
			'message': 'Successfully registered'
		}
		return response_object, 201
	else:
		response_object = {
			'status': 'fail',
			'message': 'User already exists. Please login'
		}
		return response_object, 409

def get_all_users():
	return User.query.all()

def get_a_user(public_id):
	return User.query.filter_by(public_id=public_id).first()

def save_changes(data):
	db.session.add(data)
	db.session.commit()