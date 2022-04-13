from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True) # 이름
    created = models.DateTimeField(auto_now_add=True) # 생성일
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False) # id
    name = models.CharField(max_length=200, blank=True, null=True) # 닉네임
    username = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True) # 이메일

    def __str__(self):
        return str(self.username)
