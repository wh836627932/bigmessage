#coding:utf-8
from django.db import models

# Create your models here.

"""
用户收藏表
"""

class LogEntryManager(models.Manager):
    use_in_migrations = True


class tbl_user_collection(models.Model):
    id=models.AutoField(max_length=20,primary_key=True,db_index=True)
    userId=models.IntegerField(max_length=10)
    MarkId=models.IntegerField(max_length=20)
    isCollection=models.IntegerField(max_length=2)
    time=models.TimeField()
    object = LogEntryManager()
    class Meta:
        db_table = 'tbl_user_collection'
