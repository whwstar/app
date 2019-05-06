# -*- coding:UTF-8 -*-

from flask_mail import Message
from extensions import mail

# -*- coding:UTF-8 -*-

from flask_mail import Message
from extensions import mail

def sendmail_alarm(servername,alert_info,host,created,count):
    msg = Message('告警邮件',
                sender=(host,'henry8wang@163.com'),
                recipients=['hwwang@mobvoi.com'])
    msg.html = '<p>告警邮件：</p>' \
                   '<p>服务名称："%s"</p>' \
                   '<p>告警内容：产生了"%s"，请及时处理</p>' \
                '<p>告警产生时间："%s"</p>' \
               '<p>告警次数：第"%s"次产生告警</p>' \
               '<p><small style="color: #868e96">邮件无需回复.</small></p>'%(servername,alert_info,created,count)

#        with app.open_resource(info_list['filename']) as fp:
#            msg.attach(info_list['filename'], "warn/log", fp.read())
    print msg
    mail.send(msg)
    return "发送成功"

def sendmail_release(servername,alert_info,host):
    msg = Message('解除告警邮件',
                sender=(host,'henry8wang@163.com'),
                recipients=['hwwang@mobvoi.com'])
    msg.html = '<p>解除告警邮件：</p>' \
                   '<p>服务名称："%s"</p>' \
                   '<p>告警内容："%s"告警已解除</p>' \
                   '<p><small style="color: #868e96">邮件无需回复.</small></p>'%(servername,alert_info)

#        with app.open_resource(info_list['filename']) as fp:
#            msg.attach(info_list['filename'], "warn/log", fp.read())
    mail.send(msg)
    return "发送成功"

