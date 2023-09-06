from django.db import models
from simplepro.components import fields
from simplepro.editor import fields as editor_fields
from docs.utils.model_communal.model_communal import BasesModelCommunalId


# 国家基本信息
class TransactionGeographyPoliticsCountryCollect(BasesModelCommunalId):
    """国家基本信息"""
    NAME_CHINA = fields.CharField(
        verbose_name='国家中文名称', max_length=255, show_word_limit=True, blank=True, null=True)
    NAME_ENGLISH = fields.CharField(
        verbose_name='国家英文名称', max_length=255, show_word_limit=True, blank=True, null=True)
    CHINESE_ABBREVIATION = fields.CharField(
        verbose_name='国家中文简称', max_length=100, blank=True, null=True, show_word_limit=True)
    ENGLISH_ABBREVIATION = fields.CharField(
        verbose_name='国家英文简称', max_length=100, blank=True, null=True, show_word_limit=True)
    TWO_CHARACTER_CODE = fields.CharField(
        verbose_name='国家两字符代码', max_length=100, blank=True, null=True, show_word_limit=True)
    THREE_CHARACTER_CODE = fields.CharField(
        verbose_name='国家三字符代码', max_length=100, blank=True, null=True, show_word_limit=True)
    NUMERIC_CODE = fields.CharField(
        verbose_name='国家数字代码', max_length=100, blank=True, null=True, show_word_limit=True)

    class Meta:
        db_table = "TransactionGeographyPoliticsCountryCollect"
        ordering = ['-CREATE_TIME']
        verbose_name = "国家基本信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.CHINESE_ABBREVIATION:
            return f'{self.CHINESE_ABBREVIATION}'
        elif self.ENGLISH_ABBREVIATION:
            return f'{self.ENGLISH_ABBREVIATION}'
        elif self.NAME_CHINA:
            return f'{self.NAME_CHINA}'
        elif self.NAME_ENGLISH:
            return f'{self.NAME_ENGLISH}'
        else:
            return f'{self.ID}'


class TransactionGeographyPoliticsCountryCurrency(BasesModelCommunalId):
    """国家货币"""
    ID_NATION = fields.ForeignKey(
        'country.TransactionGeographyPoliticsCountryCollect', verbose_name='国家', on_delete=models.CASCADE, null=True,
        blank=True, to_field='ID', clearable=True, placeholder='国家', )
    COUNTRY_DESCRIBE_CHINESE = fields.CharField(
        verbose_name='货币中文描述', max_length=100, blank=True, null=True, show_word_limit=True)
    COUNTRY_DESCRIBE_ENGLISH = fields.CharField(
        verbose_name='货币英文描述', max_length=100, blank=True, null=True, show_word_limit=True)
    COUNTRY_NOTATION = fields.CharField(
        verbose_name='货币符号', max_length=100, blank=True, null=True, show_word_limit=True)
    COUNTRY_ISO_CODE = fields.CharField(
        verbose_name='ISO代码', max_length=100, blank=True, null=True, show_word_limit=True)
    COUNTRY_AUXILIARY_UNIT = fields.CharField(
        verbose_name='辅助单位', max_length=100, blank=True, null=True, show_word_limit=True)
    COUNTRY_CARRY_SYSTEM = fields.CharField(
        verbose_name='进位制', max_length=100, blank=True, null=True, show_word_limit=True)
    DETAIL = editor_fields.MDTextField(verbose_name="备注", default=None, blank=True, null=True)

    class Meta:
        db_table = "TransactionGeographyPoliticsCountryCurrency"
        ordering = ['-CREATE_TIME']
        verbose_name = "国家货币"
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.COUNTRY_DESCRIBE_CHINESE:
            return f'{self.COUNTRY_DESCRIBE_CHINESE}'
        elif self.COUNTRY_DESCRIBE_ENGLISH:
            return f'{self.COUNTRY_DESCRIBE_ENGLISH}'
        elif self.COUNTRY_NOTATION:
            return f'{self.COUNTRY_NOTATION}'
        else:
            return '{}'.format(self.ID)
