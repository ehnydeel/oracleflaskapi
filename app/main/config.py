# app/main/config.py

import os

# uncomment this line below for postgres database url from enviroment variable
#postgres_local_base = os.environ['DATABASE_URL']

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
	DEBUG = False


class DevelopmentConfig(Config):
	# uncomment this line below to use postgres
	#SQLALCHEMY_DATABASE_URI = postgres_local_base
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'flask_boilerplate_main.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	DEBUG = True


class TestingConfig(Config):
	TESTING = True
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'flask_boilerplate_test.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	DEBUG = True


class ProductionConfig(Config):
	# uncomment this line below to use postgres
	#SQLALCHEMY_DATABASE_URI = postgres_local_base
	DEBUG = False


config_by_name = dict(
	dev = DevelopmentConfig,
	test = TestingConfig,
	prod = ProductionConfig
)


key = Config.SECRET_KEY
