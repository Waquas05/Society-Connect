from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

# class User(models.Model):
#     name=models.CharField(max_length=100)
#     email=models.EmailField(unique=True)
#     password=models.CharField(max_length=200)

#     def __str__(self):
#         return self.name


class Society(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    main_description= models.TextField(blank=True, null=True)
    logo = models.ImageField(upload_to="society_images/", blank=True, null=True)
    main_image=models.ImageField(upload_to="society_images", blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.name
    
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField(blank=True, null=True)
    location = models.CharField(max_length=200)
    society = models.ForeignKey(Society, on_delete=models.CASCADE, related_name="events", blank=True, null=True)
    poster = models.ImageField(upload_to='events/', blank=True, null=True) 

    def __str__(self):
        return self.title
    
class CoreMembers(models.Model):
    name=models.CharField(max_length=100)
    society=models.ForeignKey(Society, on_delete=models.CASCADE, related_name="core_members")
    role=models.CharField(max_length=50)
    photo=models.ImageField(upload_to="members/", blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.role}"
    

class Member(models.Model):
    name=models.CharField(max_length=100)
    photo=models.ImageField(upload_to= "profile_photo/", blank=True, null=True)
    society=models.ForeignKey(Society, on_delete=models.CASCADE, related_name="members")
    email=models.EmailField(blank=True, null=True)
    phone=models.CharField(max_length=15, blank=True, null=True)
    roll_no=models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.name
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    photo = models.ImageField(upload_to="profiles/", blank=True, null=True)
    semester = models.CharField(max_length=20, blank=True, null=True)
    course = models.CharField(max_length=100, blank=True, null=True)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username}'s Profile"
    
class Heads(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    society=models.ForeignKey(Society, on_delete=models.CASCADE, related_name="heads")
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    role = models.CharField(max_length=100, blank=True, null=True)  # e.g. President, Secretary, etc.
    approved = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.user.username} - {self.society.name}"

    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



