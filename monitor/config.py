# -*- coding:UTF-8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = '告警监控'
    FLASKY_MAIL_SENDER = 'hwwang@mobvoi.com'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = '25'
    MAIL_USERNAME = 'henry8wang@163.com'
    MAIL_PASSWORD = '1qaz2wsx'


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1/monitor-dev'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1/monitor'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1/monitor'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

config = {
    'dev': DevelopmentConfig,
    'testing': TestingConfig,
    'prodection': ProductionConfig,

    'default': DevelopmentConfig
}

