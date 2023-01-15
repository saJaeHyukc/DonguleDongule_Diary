from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_confirmed = models.BooleanField(default=False)
    withdraw = models.BooleanField(default=False)
    password_expired = models.BooleanField(default=False)
    last_password_changed = models.DateTimeField(auto_now=True) # 변경 되었을 때
    created_at = models.DateTimeField(auto_now_add=True) # 생성 되었을 때
    withdraw_at = models.DateTimeField(null=True)
    

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=10)
    profile_image = models.ImageField(default="default_profile_pic.jpg", upload_to="profile_pics")
    
class ConfirmEmail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    expired_at = models.DateTimeField()
    secured_key = models.CharField(max_length=255)