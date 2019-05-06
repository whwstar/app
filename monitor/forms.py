# -*- coding:UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired,Email,EqualTo,Length


class LoginForm(FlaskForm):
    username = StringField('用户名：',validators=[DataRequired('请输入用户名')])
    password = PasswordField('密码：',validators=[DataRequired('请输出密码')])
    email = StringField('邮箱：',validators=[DataRequired('请输入邮箱'),Email('请输入有效邮箱')])
    remember_me = BooleanField('记住我')
    submit = SubmitField('登录')


class RegisterForm(FlaskForm):
    username = StringField('用户名：',validators=[DataRequired('请输入用户名')])
    password = PasswordField('密码：',validators=[DataRequired('请输出密码')])
    password2 = PasswordField('再次输出密码：',validators=[EqualTo('password',message='两次输入的密码不一致')])
    email = StringField('邮箱：',validators=[DataRequired('请输入邮箱'),Email('请输入有效邮箱')])
    submit = SubmitField('注册')


class Server_Form(FlaskForm):
    host = StringField('主机名称：',validators=[DataRequired('请输入主机名称')])
    servername = StringField('服务名称：',validators=[DataRequired('请输入用户名')])
    serverport = StringField('服务端口：',validators=[DataRequired('请输入服务端口号')])
    serveruser = StringField('服务用户：',validators=[DataRequired('请输入服务用户')])
    submit = SubmitField('提交')


class Edit_Form(FlaskForm):
    host = StringField('主机名称：',validators=[DataRequired('请输入主机名称')])
    servername = StringField('服务名称：',validators=[DataRequired('请输入用户名')])
    serverport = StringField('服务端口：',validators=[DataRequired('请输入服务端口号')])
    serveruser = StringField('服务用户：', validators=[DataRequired('请输入服务用户')])
    submit = SubmitField('提交')
