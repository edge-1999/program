from django.db import models
from django.db.models import UniqueConstraint

from simplepro.components import fields
from simplepro.editor import fields as editor_fields

from docs.utils.model_communal.model_filter import get_combobox_queryset


class ProvenanceSystemSettingsStandardEncoding(models.Model):
    """标准编码"""
    NAME_CHINESE = fields.CharField(
        verbose_name='中文描述', max_length=255, blank=False, null=False, show_word_limit=True)
    NAME_ENGLISH = fields.CharField(
        verbose_name='英文描述', max_length=255, blank=False, null=False, show_word_limit=True)
    ENCODING = fields.CharField(
        verbose_name='标准格式编码', db_index=True, max_length=16, blank=False, null=False, show_word_limit=True)
    STATUS_IS_ENABLE = models.BooleanField(verbose_name="是否启用", default=False, blank=False, null=False)
    ID_PARENT = fields.TreeComboboxField(
        'standard_encoding.ProvenanceSystemSettingsStandardEncoding', on_delete=models.CASCADE, null=True, blank=True,
        verbose_name='上级', to_field='id', strictly=True, queryset=get_combobox_queryset, )

    class Meta:
        db_table = "ProvenanceSystemSettingsStandardEncoding"
        ordering = ['-id']
        verbose_name = "标准编码"
        verbose_name_plural = verbose_name
        unique_together = ('ID_PARENT', 'ENCODING')

    def __str__(self):
        return f'{self.NAME_CHINESE}{self.ENCODING}'


class ProvenanceSystemSettingsStandardCodeMain(models.Model):
    """
    码表分类
    """
    DESCRIBE = fields.CharField(
        verbose_name='中文描述', db_index=True, max_length=255, unique=True, blank=False, null=False,
        show_word_limit=True)
    TECHNOLOGY = fields.CharField(
        verbose_name='格式编码', db_index=True, max_length=255, unique=True, blank=False, null=False,
        show_word_limit=True)

    class Meta:
        verbose_name = "码表分类"  # 在admin站点中显示的名称设置模型的别名
        ordering = ['-id']
        verbose_name_plural = verbose_name
        db_table = "ProvenanceSystemSettingsStandardCodeMain"  # 指明数据库表名
        UniqueConstraint(
            fields=['TECHNOLOGY'],
            name='TECHNOLOGY'
        )

    def __str__(self):
        return f'{self.TECHNOLOGY}'


class ProvenanceSystemSettingsStandardCodeMainDict(models.Model):
    """
    码表详情
    """
    CODE_MAIN = models.ForeignKey(
        'standard_encoding.ProvenanceSystemSettingsStandardCodeMain', verbose_name='分类', on_delete=models.CASCADE,
        null=False, blank=False, to_field='TECHNOLOGY', related_name='分类')
    TECHNOLOGY = fields.CharField(
        verbose_name='格式编码', db_index=True, max_length=255, blank=False, null=False, show_word_limit=True, )
    ABBREVIATION = fields.CharField(
        verbose_name='中文描述', max_length=100, blank=False, null=False, show_word_limit=True)

    class Meta:
        verbose_name = "码表详细"
        ordering = ['-id']
        verbose_name_plural = verbose_name
        db_table = "ProvenanceSystemSettingsStandardCodeMainDict"
        UniqueConstraint(
            fields=['CODE_MAIN', 'TECHNOLOGY'],
            name='unique_code_dict'
        )

    def __str__(self):
        return f'{self.ABBREVIATION}'


class ProvenanceSystemSettingsStandardContent(models.Model):
    """
    默认内容
    """
    DESCRIBE = fields.CharField(
        verbose_name='中文描述', db_index=True, max_length=255, unique=True, blank=False, null=False,
        show_word_limit=True)
    TECHNOLOGY = fields.CharField(
        verbose_name='格式编码', db_index=True, max_length=255, unique=True, blank=False, null=False,
        show_word_limit=True)
    DETAIL = editor_fields.MDTextField(verbose_name="默认内容", default=None, blank=True, null=True)

    class Meta:
        verbose_name = "默认内容"  # 在admin站点中显示的名称设置模型的别名
        ordering = ['-id']
        verbose_name_plural = verbose_name
        db_table = "ProvenanceSystemSettingsStandardContent"  # 指明数据库表名
        UniqueConstraint(
            fields=['TECHNOLOGY'],
            name='TECHNOLOGY'
        )

    def __str__(self):
        return f'{self.TECHNOLOGY}'
