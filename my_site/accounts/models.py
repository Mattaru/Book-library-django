from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class UserProfile(models.Model):
    first_name = models.CharField(verbose_name='First name', max_length=50)
    last_name = models.CharField(verbose_name='Last name', max_length=100)
    age = models.SmallIntegerField(verbose_name='Age',
                                   default=0)
    avatar = models.ImageField(verbose_name='Avatar', blank=True, null=True, upload_to='profile_imgs')
    user = models.OneToOneField(User, verbose_name='User data', on_delete=models.CASCADE, related_name='profile')

    def __str__(self):
        return f'{self.first_name} {self.last_name} user({self.user})'


def create_profile(sender, **kwargs):
    """
    Function will execute, when you will create a new object of the UserProfile class
    """
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = UserProfile(user=user)
        user_profile.save()

post_save.connect(create_profile, sender=User)