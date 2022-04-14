from email.policy import default
from tkinter import CASCADE
from django.db import models
import uuid
from users.models import Profile
from datetime import datetime, date

# Create your models here.

class Funding(models.Model):
    created = models.DateTimeField(auto_now_add=True) # 생성일
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False) # id
    owner = models.ForeignKey(Profile,null=True,blank=True,on_delete=models.CASCADE) # 게시자명
    description = models.CharField(max_length=200) # 상품설명
    image = models.ImageField(null=True, blank=True, default="default.png") # 이미지
    target = models.IntegerField(default=0, null=False, blank=False) # 목표금액
    total_num = models.IntegerField(default=0, null=True, blank=True) # 총펀딩금액
    limitation = models.IntegerField(default=0, null=False, blank=False) # 1회펀딩금액
    dday = models.DateField('D-Day(mm/dd/yyyy)',auto_now_add=False, auto_now=False, null=False, blank=True) # d-day
    title = models.CharField(max_length=200, default='default title')
    

    def __str__(self):
        return str(self.title)


    @property
    def percentage(self):
        return self.total_num // self.target * 100


class Participant(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    funding = models.ForeignKey(Funding, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True) # 생성일
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False) # id

    def __str__(self):
        return str(self.funding)