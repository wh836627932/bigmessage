#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from mark.models.tbl_mark import tbl_Mark
from mark.models.tbl_user import tbl_user
from mark.models.tbl_user_collection import tbl_user_collection
import json
# Create your views here.


def announcementlist(request):
    """
    公开招标列表信息
    :param request: get请求
    :from 列表开始值
    ：size 列表条数
    :return:
    """
    start=request.GET.get("from")
    size=request.GET.get("size")
    sorting=request.GET.get("sorting")
    if isinstance(start,unicode) & isinstance(size,unicode) & isinstance(sorting,unicode):
        markall=tbl_Mark.object.filter(bxlx=sorting)[start:int(start)+int(size)]
        data=dict()
        value=list()
        for i in markall:
            p={
                'id':i.id,'title':i.title,'coding':i.coding,'date':i.time,
                'method':i.bxlx,'budget':i.budget
            }
            value.append(p)
        data['data']=value
        data['errcode'] = 0
        return HttpResponse(json.dumps(data))
    else:
        return HttpResponse("参数错误")


def announcement(request):
    """
    项目详情视图
    :param request:
    :return:
    """
    markid=request.GET.get('markid')
    if isinstance(markid, unicode):
        item=tbl_Mark.object.filter(id=markid)
        isCollection=tbl_user_collection.object.filter(MarkId=markid)
        if len(isCollection)==0:
            isCollection=0
        data=dict()
        data['isCollection']=isCollection
        data['errcode']=0
        data['data']={
            'id':item[0].id,'title':item[0].title,'time':item[0].time,'coding':item[0].coding,
            'html':item[0].html,'Administrative_Areas':item[0].Administrative_Areas,
            'bxlx':item[0].bxlx
        }
        return HttpResponse(json.dumps(data))
    else:
        return HttpResponse("参数错误")
