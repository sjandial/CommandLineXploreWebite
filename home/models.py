from django.db import models
#from django.contrib.auth.models import User
from django.utils import timezone
import time
import datetime
# Create your models here.
class UserProfile(models.Model):
    name=models.CharField(max_length=30)
    username=models.CharField(max_length=30,primary_key=True)
    branch=models.CharField(max_length=30)
    year=models.IntegerField(default=2)
    college=models.CharField(max_length=30)
    contact=models.IntegerField(default=99)
    password=models.CharField(max_length=30)
    def __unicode__(self):
        return self.username
class Question_ans_key(models.Model):
	q_no=models.CharField(max_length=30)
	ans=models.CharField(max_length=30)
	key=models.CharField(max_length=30)
	def __str__(self):
		return self.ans
class Submission(models.Model):
	user=models.ForeignKey(UserProfile)
	time=models.DateTimeField(default=datetime.datetime.now())
	qno=models.CharField(max_length=30)
	def __str__(self):
		return self.user.username