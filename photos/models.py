from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100,null=False,blank=False)

    def __str__(self):
        return self.name

class Photo(models.Model):
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True)
    image=models.ImageField(null=False,blank=False)
    description=models.TextField()
    selling_price=models.FloatField()
    artist_name=models.CharField(max_length=100,default='SOME STRING')

    def __str__(self):
        return self.description
    
class Comment(models.Model):
     user_name=models.CharField(max_length=100,null=False)  
     user_comment=models.TextField()  

     def __str__(self):
         return self.user_comment   

class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    auth_token=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    is_verified=models.BooleanField(default=False)

    def __str__(self) :
        return self.user.username
    

class urequesr(models.Model):
    username=models.CharField(max_length=100)
    msg=models.CharField(max_length=500)
    insta=models.CharField(max_length=100)
    date=models.DateField(auto_now_add=True,auto_created=True)
    artistname=models.CharField(max_length=100,default="artist")

    def __str__(self) :
        return self.username
    

class artistname(models.Model):
     username=models.CharField(max_length=100,null=False) 


     def __str__(self):
         return self.username   