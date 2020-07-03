from django.db import models
from django.contrib.auth.models import auth,User
from django.contrib.auth import login,logout

# Create your models here.

class question_answer(models.Model):
    question=models.CharField(max_length=250)
    answer=models.CharField(max_length=3)
    explain=models.TextField()

class test(models.Model):
    section=models.CharField(max_length=3,default='A')
    question=models.CharField(max_length=250)
    optionA=models.CharField(max_length=100)
    optionB=models.CharField(max_length=100)
    optionC=models.CharField(max_length=100)
    optionD=models.CharField(max_length=100)
    answer=models.CharField(max_length=3,default='answer')
    explain=models.TextField(default='explain')
    

class saved_test(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    question=models.CharField(max_length=250)
    answer=models.CharField(max_length=3)
    optionA=models.CharField(max_length=100,default='optionA')
    optionB=models.CharField(max_length=100,default='optionB')
    optionC=models.CharField(max_length=100,default='optionC')
    optionD=models.CharField(max_length=100,default='optionD')
