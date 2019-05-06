# -*- coding:UTF-8 -*-
import os
import click
from flask import Flask,render_template
from monitor.extensions import db,mail,login_manager,bootstrap
from monitor.buleprints.auth import  auth_bp
from monitor.buleprints.server import server_bp
from config import config
from flask_wtf.csrf import CSRFError
from monitor.models import User,Server,Alert


#  创建应用工厂，接收参数定义成为一个变量，就可以通过接收不同的实参来生成不同的app对象
def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG','dev')
    app = Flask(__name__)
    app.config.from_object(config[config_name])
#    register_errors(app)
    register_extentions(app)
    register_buleprints(app)
    register_commands(app)
    return app


def register_extentions(app):
    mail.init_app(app)
    db.init_app(app)
#    csrf.init_app(app)
    login_manager.init_app(app)
    bootstrap.init_app(app)


def register_buleprints(app):
    app.register_blueprint(auth_bp,url_prefix='/auth')
    app.register_blueprint(server_bp)


def register_shell_context(app):
    @app.shell_context_processor
    def make_shell_context():
        return dict(db=db,User=User,Server=Server,Alert=Alert)

def register_errors(app):
    @app.errorhandler(400)
    def bad_request(e):
        return render_template('errors/400.html'), 400

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('errors/500.html'), 500


def register_commands(app):
    @app.cli.command()
    @click.option('--drop', is_flag=True, help='Create after drop.')
    def initdb(drop):
        """Initialize the database."""
        if drop:
            click.confirm('This operation will delete the database, do you want to continue?', abort=True)
            db.drop_all()
            click.echo('Drop tables.')
        db.create_all()
        click.echo('Initialized database.')

