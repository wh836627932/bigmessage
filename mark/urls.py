#coding:utf-8
from django.conf.urls import include, url

from views.announcement import announcementlist,announcement
from views.user_login import userlogin,userconf,Verify_landing,userCollection
from views.user_login import userColletionlist

urlpatterns = [
    #公告搜索
    url(r'search/', include('haystack.urls')),
    #公共列表
    url(r'marks/notice', announcementlist),
    #公告详情
    url(r'mark/item', announcement),
    #用户登陆
    url(r'user/login', userlogin),
    #验证登陆
    url(r'user/userconf', userconf),
    #收藏/取消收藏
    url(r'mark/collect',userCollection),
    #用户收藏
    url(r'my/collections',userColletionlist)
]