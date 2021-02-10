from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from . import AbstractModel


class User(AbstractBaseUser, AbstractModel):

    class Meta:
        db_table = "user"
        verbose_name = "ユーザー"
        verbose_name_plural = "ユーザー"

    email = models.EmailField(
        null=False, max_length=255, unique=True, verbose_name="メールアドレス")
    name = models.CharField(null=True, max_length=100, verbose_name="名前")

    is_active = models.BooleanField(default=True, verbose_name="アクティブフラグ")
    is_staff = models.BooleanField(default=False, verbose_name="システム管理者フラグ")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return str(self.name)

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
