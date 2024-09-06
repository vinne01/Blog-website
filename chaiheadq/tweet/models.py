from django.db import models
#first import django files when admin panel makethenuser comes
from django.contrib.auth.models import User
# Create your models here.
class Tweet(models.Model):
 user=models.ForeignKey(User,on_delete=models.CASCADE)
 text=models.TextField(max_length=400)
 photo=models.ImageField(upload_to='photo/',blank=True,null=True)
 created_at=models.DateTimeField(auto_now_add=True)
 updated_at=models.DateTimeField(auto_now=True)
 
 #it help to modify through username 
 def ___str__(self):
     return f'{self.user.username} - {self.text[:10]}'