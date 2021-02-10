from typing import Optional
from django.db import models


class AbstractModel(models.Model):
    created_at: Optional[models.DateTimeField] = models.DateTimeField(
        null=False, auto_now_add=True, verbose_name="作成日時")
    updated_at: Optional[models.DateTimeField] = models.DateTimeField(
        null=False, auto_now=True, verbose_name="更新日時")

    class Meta:
        abstract = True
