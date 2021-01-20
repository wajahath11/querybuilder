from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserAccountManager(BaseUserManager):
    def create_user(self, email,password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email,name=None, password=None,):
        user = self.create_user(
            email,
            name=name,
            password=password,
            is_staff=True,
            is_admin=True,
        )
        return user
class User(AbstractBaseUser):
    name    = models.CharField(max_length=20,unique=True)
    email   = models.EmailField(null=True,blank=True)
    objects = UserAccountManager()

    is_active         = models.BooleanField(default=True)
    is_staff          = models.BooleanField(default=False)
    is_admin          = models.BooleanField(default=False)

    USERNAME_FIELD    = 'name'
    REQUIRED_FIELDS   = ['email']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

class Bankdata(models.Model):
    branch_code = models.CharField(max_length=20,)
    branch_name = models.CharField(max_length=20,)
    account_number = models.IntegerField()
    customer_account = models.CharField(max_length=20,)
    tran_date = models.DateTimeField()
    branch_code = models.CharField(max_length=20,)
    tran_ref_no = models.CharField(max_length=20,)
    acc_entry_sr_no = models.IntegerField()
    amount = models.FloatField()

    def __str__(self):
        return self.branch_code