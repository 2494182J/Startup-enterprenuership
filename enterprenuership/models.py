from django.db import models
from django.contrib.auth.models import User
###create the 数据库的models here
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ###user
    picture=models.ImageField(upload_to='user_picture',blank=True)

    def __str__(self):
        return self.user.username
