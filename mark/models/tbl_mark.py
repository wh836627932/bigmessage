#coding:utf-8

from django.db import models

class LogEntryManager(models.Manager):
    use_in_migrations = True

# Create your models here.
class tbl_Mark(models.Model):
    id = models.AutoField(primary_key=True, db_index=True)
    title=models.CharField(max_length=200,blank=True)
    time = models.TimeField()
    coding = models.TextField(max_length=20)
    html = models.TextField()
    Administrative_Areas = models.CharField(max_length=20)
    FileTime = models.TextField(max_length=50)
    FilePrice = models.TextField(max_length=10)
    Fileaddress = models.TextField(max_length=50)
    starttime = models.TextField(max_length=20)
    budget = models.TextField(max_length=20)
    peopleTEL = models.TextField(max_length=20)
    bxlx = models.TextField(max_length=20)
    def __unicode__(self):
        return self.title
    class Meta:
        db_table = 'tbl_Mark'
    object = LogEntryManager()