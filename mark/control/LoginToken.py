#coding:utf-8
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import SignatureExpired, BadSignature, BadData
from django.http import HttpResponse
from django.http import Http404
from django.conf import settings

import time

class QXToken(object):
    def __init__(self):
        self.expiration=43200

    def genTokenSeq(self, user_id):
        """
        生产token
        :param user_id:
        :return: token
        """
        s = Serializer(
            secret_key=settings.SECRET_KEY,
            expires_in=self.expiration)
        timestamp = time.time()
        return s.dumps(
            {'user_id': user_id,
             'iat': timestamp})

    def tokenAuth(self,fun):
        """
        验证token
        :param token:
        :return: 用户id
        """
        def wrap(request):
            if  request.META.get("HTTP_ACCESS_TOKEN"):
                s = Serializer(settings.SECRET_KEY)
                try:
                    data = s.loads(request.META.get("HTTP_ACCESS_TOKEN"))
                except SignatureExpired:
                    return HttpResponse("{errcode:40001}") #"valid token, but expired"
                except BadSignature:
                    return HttpResponse("{errcode:40002}") #"invalid token"
                return fun(request,data['user_id'])
            else:
                return HttpResponse("{errcode:40003}")
        return wrap


if __name__ == '__main__':
    app=QXToken()
    tolen = app.genTokenSeq('123456')
    print tolen