from django.db import models

# Create your models here.

class LogEntryManager(models.Manager):
    use_in_migrations = True

class tbl_user(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.TextField(max_length=20)
    password=models.TextField(max_length=30)
    appid=models.TextField(max_length=100)
    nickname=models.TextField(max_length=20)
    realname=models.TextField(max_length=10)
    phone=models.TextField(max_length=11)
    cardNo=models.TextField(max_length=18)
    gender=models.IntegerField(max_length=3)
    address=models.TextField()
    signature=models.TextField()
    img=models.TextField()
    time=models.TimeField()
    class Meta:
        db_table = 'tbl_user'
    object=LogEntryManager()