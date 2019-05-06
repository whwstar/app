# -*- coding:UTF-8 -*-
import sys
import os
reload(sys)
import json
import requests
import subprocess
import time
import socket

#curl localhost:5000/create_alter -d '{"servername":"kafka-server","alter_name":"kafka warn","alter_info":"docker ps 不能发现服务进程","created":"2021-03-15 00:11:11"}' -H 'Content-Type: application/json'

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_list = { 'nginx-server':'80',
                'sagittarius-nlu-service':'8620',
                'knowledge-service':'8088',
                'es-server':'9200',
                'logstash-server':'9600',
                'knowledge-query-clustering':'8633',
                'knowledge-manage':'8540',
                'nlu-model-server':'8071',
                'qap-server':'8449',
                'apollo-simple':'38070',
                'question-match':'9091',
                'sagittarius-dialogue':'8619',
                'sagittarius-multiple-conversations-service':'8617',
                'api-service':'8083',
                'gateway-service':'8616',
                'sentiment-analysis-server':'8306',
                'mysql-server':'3306',
                'kibana-server':'5601',
                'kafka-server':'9092',
                'redis-server':'6379',
                'zk-server':'2181',
                'consul-service':'8500'}
host = "0.0.0.0"
url = 'http://localhost:5000/create_alter'
headers = {'Content-Type': "application/json;", 'Accept': "application/json"}
for server,port in server_list.items():
    res = subprocess.call(" docker ps |  grep {} >/dev/null".format(server),shell=True)
    if res == 0 :
        pass
    else:
        data = {}
        current_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
        data['servername'] = server
        data['alter_name'] = '{}告警'.format(server)
        data['alter_info'] = "docker ps 命令未能发现服务"
        data['created'] = current_time
        res = requests.post(url, json=data, headers=headers)
        print res.status_code
    nc = subprocess.call("nc -z {} {} >/dev/null".format(host,port),shell=True)
    if nc == 0 :
        pass
    else:
        data = {}
        current_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
        data['servername'] = server
        data['alter_name'] = '{}告警'.format(server)
        data['alter_info'] = "nc {} 端口号失败，服务可能出现假死".format(server)
        data['created'] = current_time
        res = requests.post(url, json=data, headers=headers)
        print res.status_code
