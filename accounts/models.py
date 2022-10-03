from django.db import models
import os
from datetime import datetime
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, username, password):
        if not email:
            raise ValueError('User must have an email')
        if not username:
            raise ValueError('User must have an username')
        user = self.model(
            email = self.normalize_email(email),
            username = username,
        )
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, email, username, password):
        user  = self.create_user(
            email = self.normalize_email(email),
            password = password,
            username = username
        )
        user.is_admin     = True
        user.is_staff     = True
        user.is_superuser = True
        user.save( using = self._db )
        return user


class User(AbstractBaseUser):
    avatar          = models.ImageField(upload_to = f'user{os.sep}',default='images/example.jpg',blank=True,null=True)
    biograph        = models.TextField(default = '')
    email           = models.EmailField(verbose_name = 'Email', max_length = 60, unique = True)
    username        = models.CharField(max_length = 50, unique = True)
    date_joined     = models.DateTimeField(verbose_name = 'date joined', auto_now_add = True)
    is_admin        = models.BooleanField(default = False)
    is_staff        = models.BooleanField(default = False)
    is_superuser    = models.BooleanField(default = False)
    last_login      = models.DateTimeField(default=datetime.now)

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['username']

    objects         = UserManager()

    def __str__(self):
        return f'{self.username} {self.email}'

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
