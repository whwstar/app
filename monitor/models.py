# -*- coding:UTF-8 -*-

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
#  从flask_login导入UserMixin类
#  USerMixin类包含的以上四种方法的默认实现。
from monitor.extensions import db,login_manager
#  从程序的工厂函数引入login_manager实例


class User(db.Model,UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(128),nullable = False)
    email = db.Column(db.String(128),unique=True)

    def set_password(self,password):
        self.password = generate_password_hash(password)
    def validate_password(self,password):
        return  check_password_hash(self.password,password)


class Server(db.Model):
    __tablename__ = 'server'

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    host = db.Column(db.String(128),nullable = False)
    servername = db.Column(db.String(64),nullable = False)
    serverport = db.Column(db.Integer,nullable = False)
    status = db.Column(db.Integer,nullable = False)
    created = db.Column(db.String(64),nullable = False)
    serveruser = db.Column(db.String(64),nullable = False)


class Alert(db.Model):
    __tablename__ = 'alert'

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    alert_name = db.Column(db.String(128),nullable = False)
    alert_info = db.Column(db.String(64))
    server_id = db.Column(db.Integer,db.ForeignKey('server.id'))
    created = db.Column(db.String(64),nullable = False)
    count = db.Column(db.String(64),nullable = False)