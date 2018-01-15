# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from utils.ssh import Command

import json

from django.http import HttpResponse,request


def list(request,node=None):
    '''
    Command.handle(node)
    format json
    data
    '''
    getNode = request.GET.get('node')
    nodes=str(getNode)
    # cmd="find /data/logs -type d |grep -v '^/data/logs$'"
    cmd="ls -d /data/logs/*"
    ssh = Command(node=str(nodes),arg=cmd)
    data =ssh.handle()
    data_list=[]
    for value in data:
        data_dict = {}
        data_dict['name']=value.rstrip()
        data_dict['value']=value.rstrip()
        data_list.append(data_dict)

    return HttpResponse(json.dumps(data_list), content_type="application/json")


def log(request,node=None,arg=None):

    getNode = request.GET.get('node')
    getArg = request.GET.get('arg')
    nodes=str(getNode)
    cmd="find  %s  -type f -mtime -1" % getArg
    print cmd
    ssh = Command(node=str(nodes),arg=cmd)
    data =ssh.handle()
    print len(data),type(data)


    data_list=[]
    if not data:
        notfile='not file'
        data_dict = {}
        data_dict['name']=notfile
        data_dict['value']=notfile
        data_list.append(data_dict)

    else:
        print data
        for value in data:
            data_dict = {}
            data_dict['name']=value.rstrip()
            data_dict['value']=value.rstrip()
            data_list.append(data_dict)

    return HttpResponse(json.dumps(data_list), content_type="application/json")