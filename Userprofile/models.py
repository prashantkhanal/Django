from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=255, null=True, blank=True)
    # address =models.CharField(max_length=255, null=True, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        
# from django.db import models
# from django.contrib.auth.models import User
# from django.dispatch import receiver
# from django.db.models.signals import post_save



# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     fist_name =models.CharField(max_length=255, null=True, blank=True)
#     last_name =models.CharField(max_length=255, null=True, blank=True)
#     contact =models.CharField(max_length=255, null=True, blank=True)


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)



