# -*- coding:UTF-8 -*-

from flask import Flask,Blueprint,render_template,url_for,flash,request,redirect
from flask_login import logout_user,login_required,current_user,user_logged_out,login_user
from monitor.models import User,db
from monitor.utils import redirect_back


from monitor.forms import LoginForm


auth_bp = Blueprint('auth',__name__)


@auth_bp.route('/adduser')
def adduser():
    user = User()
    admin = User(username='whwstar', email='whwstar@yeah.net', password=user.set_password('!QAZ2wsx'))
    print admin
    db.session.add(admin)
    db.session.commit()

@auth_bp.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('server.serverlist'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        remember = request.form['remember-me']
        user = User.query.filter(User.username == username).first()
        if user is None:
            flash('No account','warning')
        else:
            if user.validate_password(password):
                login_user(user,remember)
                flash('Welcome back','info')
                return redirect(url_for('server.serverlist'))
            else:
                flash('Password Invalid','warning')
    return render_template('auth/login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logout Success','info')
    return redirect(url_for('auth.login'))