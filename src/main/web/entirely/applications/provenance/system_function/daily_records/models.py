import time

from django.db import models
from simplepro.components import fields
from simplepro.editor import fields as editor_fields

from docs.utils.system_communal.configuration import options_date
from docs.utils.model_communal.model_communal import BasesModelCommunalId
from docs.utils.model_communal.model_queryset import (
    get_queryset_records_event_identity, get_queryset_records_event_type)
from docs.utils.model_communal.model_values_filter import select_event_details, select_event_diary


# 事件记录
class ProvenanceSystemFunctionDailyRecordsEvent(BasesModelCommunalId):
    """事件记录"""
    ID_PERSON = fields.ForeignKey(
        'personal_Information.TransactionSocialCultureEthnicPopulationPersonalInformationPerson',
        verbose_name='记录人员', on_delete=models.CASCADE, null=True, blank=True, to_field='ID', clearable=True,
        placeholder='记录人员', )
    DATE = fields.DateField(
        verbose_name='发生日期', default=time.strftime("%Y-%m-%d %H:%M:%S"), blank=True, null=True,
        options=options_date)
    IDENTITY = fields.ForeignKey(
        'standard_encoding.ProvenanceSystemSettingsStandardCodeMainDict', verbose_name='参与身份',
        on_delete=models.CASCADE, null=True, blank=True, to_field='id', clearable=True, placeholder='参与身份',
        queryset=get_queryset_records_event_identity, )
    NAME = fields.CharField(verbose_name='事件名称', max_length=255, blank=True, null=True, show_word_limit=True)
    DETAIL = editor_fields.MDTextField(
        verbose_name="详情描述", default=select_event_details(), blank=True, null=True)

    class Meta:
        db_table = "ProvenanceSystemFunctionDailyRecordsEvent"
        ordering = ['-DATE']
        verbose_name = "事件记录"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.ID_PERSON}:{self.DATE}-{self.NAME}'


# 事件类型
class ProvenanceSystemFunctionDailyRecordsEventType(BasesModelCommunalId):
    """事件类型"""
    ID_EVENT = fields.ForeignKey(
        'daily_records.ProvenanceSystemFunctionDailyRecordsEvent', verbose_name='事件', on_delete=models.CASCADE,
        null=True, blank=True, to_field='ID', clearable=True, placeholder='事件')
    CODE = fields.ForeignKey(
        'standard_encoding.ProvenanceSystemSettingsStandardCodeMainDict', verbose_name='事件类型',
        on_delete=models.CASCADE, null=True, blank=True, to_field='id', clearable=True, placeholder='事件类型',
        queryset=get_queryset_records_event_type, )

    class Meta:
        db_table = "ProvenanceSystemFunctionDailyRecordsEventType"
        ordering = ['-CREATE_TIME']
        verbose_name = "事件类型"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.ID_EVENT}:{self.CODE}'


# 日记本
class ProvenanceSystemFunctionDailyRecordsDiary(BasesModelCommunalId):
    """日记本"""
    ID_PERSON = fields.ForeignKey(
        'personal_Information.TransactionSocialCultureEthnicPopulationPersonalInformationPerson',
        verbose_name='记录人员', on_delete=models.CASCADE, null=True, blank=True, to_field='ID', clearable=True,
        placeholder='记录人员', )
    DATE = fields.DateField(
        verbose_name='日期', default=time.strftime("%Y-%m-%d %H:%M:%S"), blank=True, null=True, options=options_date)
    DETAIL = editor_fields.MDTextField(verbose_name="详情描述", default=select_event_diary(), blank=True, null=True)

    class Meta:
        db_table = "ProvenanceSystemFunctionDailyRecordsDiary"
        ordering = ['-DATE']
        verbose_name = "日记本"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.ID_PERSON}:{self.DATE}'
