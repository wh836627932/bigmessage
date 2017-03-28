#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import json
import time
import requests
from mark.models.tbl_mark import tbl_Mark
from mark.models.tbl_user_collection import tbl_user_collection
from mark.models.tbl_user import tbl_user
from mark.control.LoginToken import QXToken


token = QXToken()

@token.tokenAuth
def Verify_landing(request, userid):
    """
    验证用户是否登陆测试
    :param request:
    :param userid:
    :return:
    """
    print request.META.get("HTTP_ACCESS_TOKEN")
    return HttpResponse(userid)

def userlogin(request):
    """
    用户登陆
    :param request:
    :return:
    """
    id=None
    uudi=None
    isNew=None
    code = request.GET.get("code")
    if not isinstance(code,unicode):
        return HttpResponse("{errcode:40003}")
    if request.method != 'GET' :
        return HttpResponse({"errcode":40003})
    else:
        url=("https://api.weixin.qq.com/sns/jscode2session?appid="+settings.APPID+"&secret="+settings.SECRET_ID+"&js_code="+code+"&grant_type=authorization_code")
        appid=eval(requests.get(url=url).text)
        print type(appid.get("openid"))
        if isinstance(appid.get("openid"),str):
            id = tbl_user.object.filter(appid=appid.get("openid")).values('id')
            if len(id) > 0:
                isNew = 0
            else:
                isNew = 1
                tbl_user.object.create(appid=appid.get("openid"))
                id = tbl_user.object.filter(appid=appid).values('id')
            uudi = token.genTokenSeq(id[0].get('id'))
            data = json.dumps({"errcode": 0, "data": {"userId": id[0].get('id'), "token": uudi, "isNew": isNew}})
            return HttpResponse(data)
        else:
            return HttpResponse(json.dumps(appid))

@token.tokenAuth
def userconf(request,userid):
    """
    修改用户信息
    :param request:
    :param userid:
    :return:
    """

    return HttpResponse(userid)

@token.tokenAuth
def userCollection(request,userid):
    """
    用户收藏公告
    :return:
    """
    markid=request.GET.get("markid")
    isCollect=request.GET.get("isCollect")
    if isinstance(markid,unicode) & isinstance(isCollect,unicode) & int(isCollect)==1 :
        p=tbl_user_collection.object.filter(userId=userid,MarkId=markid)
        if len(p)==0:
            tbl_user_collection.object.create(userId=userid,MarkId=markid)
            return HttpResponse("添加成功")
            # tbl_user_collection.object.filter(userId=userid)
        return HttpResponse("已经存在")
    elif isinstance(markid,unicode) & isinstance(isCollect,unicode) & int(isCollect)==0 :
         tbl_user_collection.object.filter(userId=userid,MarkId=markid).delete()
         return HttpResponse("取消成功")
    else:
        return HttpResponse("参数错误")


def userColletionlist(request):
    userid=6
    collectlist=tbl_user_collection.object.filter(userId=userid)
    collect=list()
    for i in collectlist:
        collect.append(i.MarkId)
    # marklist=tbl_user_collection.object.filter(roles__userId__in=",".join(collect))
    marklist=tbl_Mark.object.filter(id__in=(23,24,25,26))
    data=dict()
    data['errcode']=0
    p=list()
    for j in marklist:
        p.append({
            'id': j.id, 'title': j.title, 'coding': j.coding, 'date': j.time,
            'method': j.bxlx, 'budget': j.budget
        })
    data['data']=p
    return HttpResponse(json.dumps(data))