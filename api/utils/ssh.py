#!/usr/bin/env python
#coding=utf-8
__author__ = "yidong.lu"
__email__ = "yidongsky@gmail.com"


import subprocess

from django.conf import settings
server_user = settings.SERVER_USERS

class Command(object):

    def __init__(self,prom=None,env=None,node=None,arg=None,options=None):
        self.prom = prom   #指定项目名
        self.env = env     #环境beta dev preview online
        self.node = node   #id地址...
        self.arg = arg     #参数
        self.options = options #保留参数

    def handle(self):
        connect = server_user+'@'+self.node
        ssh = subprocess.Popen(["ssh", "%s" % connect, self.arg],
                           shell=False,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
        result = ssh.stdout.readlines()

        if result == []:
            error = ssh.stderr.readlines()
            return error
        else:
            return result
