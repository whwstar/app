# -*- coding:UTF-8 -*-

from flask import Blueprint,render_template,request,redirect,url_for,flash
from monitor.models import Server,Alert,db
from monitor.forms import Server_Form,Edit_Form
from monitor.emails import sendmail_release,sendmail_alarm
from flask_login import login_required
import time


now = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))

server_bp = Blueprint('server',__name__,url_prefix='/server')


@server_bp.route('/alarmlist',methods=["GET", "POST"])
@login_required
def alarmlist():
    res = db.session.query(Alert.id,Alert.alert_name,Alert.alert_info,Alert.created,Server.servername,Alert.count,Server.host).filter(Alert.server_id == Server.id ).all()
    return render_template('server/alarmlist.html',list=res)


@server_bp.route('/addalarm',methods=['GET','POST'])
def addalarm():
    if request.method == 'POST':
        data = request.get_json()
        servername = data['servername']
        host = data['host']
        result = Server.query.filter_by(servername = servername,host = host).first()
        server_id = result.id
        alert_name = data['alert_name']
        alert_info = data['alert_info']
        created = data['created']
        alert_list = Alert.query.filter(Alert.alert_name == alert_name,Alert.server_id == server_id).first()
        count = 1
        if alert_list is None:
            '''
            In this host no this alert_info ,insert
            '''
            alert = Alert(alert_name= alert_name,alert_info = alert_info,server_id = server_id,created = created ,count=count)
            db.session.add(alert)
            db.session.commit()
            """
            设置服务状态为错误，100
            """
            Server.query.filter_by(id=server_id).update({'status': '100'})
            db.session.commit()
        else:
            '''
            This alert_info has been exist
            '''
            count = int(alert_list.count) + 1
            alert_list.count = count
            db.session.add(alert_list)
            db.session.commit()
        sendmail_alarm(servername,alert_info,host,created,count)
    return render_template('/auth/userlist.html')




@server_bp.route('/delalert')
@login_required
def delalert():
    '''
    删除告警
    :return:
    '''
    alert_id = request.args['id']
    servername = request.args['servername']
    host = request.args['host']
    alert_info = request.args['alert_info']
    res = Alert.query.filter(Alert.id == alert_id).first()
    server_id = res.server_id
    db.session.delete(res)
    db.session.commit()
    """
    恢复服务状态为正确，200
    """
    Server.query.filter_by(id=server_id).update({'status': '200'})
    db.session.commit()

    sendmail_release(servername,alert_info,host)

    return redirect(url_for('server.alarmlist'))



@server_bp.route('/serverlist')
@login_required
def serverlist():
    res = Server.query.order_by(Server.host.asc()).all()
    return render_template('server/serverlist.html',list=res)


@server_bp.route('/addserver',methods=['POST','GET'])
@login_required
def addserver():
    forms = Server_Form()
    if forms.validate_on_submit():
        if  request.method == 'POST':
            host = forms.host.data
            servername = forms.servername.data
            serverport = int(forms.serverport.data)
            serveruser = forms.serveruser.data
            res = Server.query.filter(Server.host == host,Server.servername == servername)
            if res is None:
                server = Server(servername=servername,serverport=serverport,status=200,serveruser=serveruser,created=now,host=host)
                db.session.add(server)
                db.session.commit()
                return redirect(url_for('server.serverlist'))
            else:
                flash('主机上已部署了此服务')
    return render_template('server/addserver.html',form=forms)


@server_bp.route('/delserver',methods=["GET", "POST"])
@login_required
def delserver():
    servername = request.args['servername']
    print servername
    res = Server.query.filter(Server.servername == servername).first()
    db.session.delete(res)
    db.session.commit()
    return redirect(url_for('server.serverlist'))


'''

'''
@server_bp.route('/editserver/<int:id>',methods=['GET', 'POST'])
@login_required
def editserver(id):
    form = Edit_Form()
    server = Server.query.get_or_404(id)
    if form.validate_on_submit() :
        server.host = form.host.data
        server.servername = form.servername.data
        server.serverport = form.serverport.data
        server.serveruser = form.serveruser.data
        db.session.commit()
        flash('server update .','sucess')
        return redirect(url_for('server.serverlist'))
    form.host.data = server.host
    form.servername.data = server.servername
    form.serverport.data = server.serverport
    form.serveruser.data = server.serveruser
    return render_template('server/editserver.html',form=form)

