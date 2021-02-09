from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings #retrive settings from settings file

# Create your models here.
class UserProfileManager(BaseUserManager):

    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('Email address required')
        email = self.normalize_email(email) #case sensetive check
        user = self.model(email=email, name=name) # set user model object

        #password hashing
        user.set_password(password)

        #save and support for multiple db <using=self._db>
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user



class UserProfile(AbstractBaseUser,PermissionsMixin):
    '''DB model for users in the system'''
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length = 255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    #Model manager
    objects = UserProfileManager()

    USERNAME_FIELD='email' #override default username field
    REQUIRED_FIELDS=['name']

    def get_full_name(self):
        '''Retrive full name of user'''
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        '''return string represantation of user'''
        return self.email
    
    
class ProfileFeedItem(models.Model):
    '''Profile status update'''
    user_profile = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status_text = models.CharField(max_length = 255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status_text
    
    

    
