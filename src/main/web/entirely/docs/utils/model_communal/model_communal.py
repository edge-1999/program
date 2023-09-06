import uuid

from django.db import models
from simplepro.components import fields


class BasesModelCommunal(models.Model):
    """
    主数据基类，公共字段 无ID
    """
    CREATE_TIME = fields.DateTimeField(
        verbose_name="创建时间", auto_now_add=True, align='right', clearable=False, editable=False, readonly=True)
    UPDATE_TIME = models.DateTimeField(verbose_name="更新时间", auto_now=True, blank=False, null=False)
    STATUS_IS_DELETE = models.BooleanField(verbose_name="逻辑删除", default=False, blank=False, null=False)
    STATUS_IS_EFFECTIVE = models.BooleanField(verbose_name="是否有效", default=True, blank=False, null=False)

    class Meta:
        abstract = True


class BasesModelCommunalId(models.Model):
    """
    主数据基类，公共字段 有ID
    """
    ID = models.UUIDField(primary_key=True, verbose_name='标识', auto_created=True, default=uuid.uuid4, editable=False)
    CREATE_TIME = fields.DateTimeField(
        verbose_name="创建时间", auto_now_add=True, align='right', clearable=False, editable=False, readonly=True)
    UPDATE_TIME = models.DateTimeField(verbose_name="更新时间", auto_now=True, blank=False, null=False)
    STATUS_IS_DELETE = models.BooleanField(verbose_name="逻辑删除", default=False, blank=False, null=False)
    STATUS_IS_EFFECTIVE = models.BooleanField(verbose_name="是否有效", default=True, blank=False, null=False)

    class Meta:
        abstract = True
