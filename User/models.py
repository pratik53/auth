from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser
# Create your models here.

class MyManager(BaseUserManager):
    def create_user(self,email,first_name,middle_name,last_name,password=None,password2=None):
        if not email:
            raise ValueError("User must have email address")
        user = self.model(email=self.normalize_email(email),
                            first_name=first_name,
                            middle_name=middle_name,
                            last_name=last_name)


        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self,email,password=None):
        user  = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(verbose_name = 'Email',max_length = 500,unique = True)
    first_name = models.CharField(max_length = 100)
    middle_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    objects = MyManager()

    USERNAME_FIELD = 'email'
    
    def __str__(self):
        return self.email

    def is_staff(self):
        return self.is_admin

    def has_module_perms(self,perm,obj=None):
        return True

    def has_perm(self,perm,obj=None):
        return True