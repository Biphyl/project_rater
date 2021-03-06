from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    bio = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='images/', default='images/smoke.jpeg')
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    
    
    
    def save_profile(self):
        self.save()
        
    def delete_profile(self):
        self.delete()
     
    @classmethod   
    def update_name(cls,id,new_first_name):
        cls.objects.filter(user_id = id).update(first_name=new_first_name)
        new_title_object = cls.objects.get(first_name=new_first_name)
        new_name = new_title_object.first_name
        return new_name
        
    @classmethod
    def get_user_profile(cls,id):
        profile = cls.objects.get(user_id=id)
        return profile

@receiver(post_save,sender=User)
def create_profile(sender, instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
    
@receiver(post_save,sender=User)
def save_profile(sender, instance,**kwargs):
    instance.profile.save()


class Post(models.Model):
    title =  models.CharField(max_length=30)
    image = models.ImageField(upload_to='post/')
    description = HTMLField()
    link = models.CharField(max_length=500)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def save_post(self):
        self.save()
        
    def delete_post(self):
        self.delete()
     
    @classmethod   
    def update_title(cls,id,new_title):
        cls.objects.filter(pk = id).update(title=new_title)
        new_title_object = cls.objects.get(title=new_title)
        new_title = new_title_object.title
        return new_title
        
    @classmethod
    def get_single_project(cls,id):
        post = cls.objects.get(pk=id)
        return post
    
    def __str__(self):
        
        return self.title


class Reviews(models.Model):
    title = models.CharField(max_length=50)
    review = models.TextField()
    design = models.PositiveIntegerField(default=0)
    usability = models.PositiveIntegerField(default=0)
    content = models.PositiveIntegerField(default=0)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    