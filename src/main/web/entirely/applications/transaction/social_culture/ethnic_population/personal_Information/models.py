import time

from django.db import models
from django.db.models import UniqueConstraint

from simplepro.components import fields
from simplepro.editor import fields as editor_fields

from docs.utils.system_communal.configuration import options_date
from docs.utils.model_communal.model_communal import BasesModelCommunalId
from docs.utils.model_communal.model_queryset import (
    get_queryset_function_person_sex_physiological, get_queryset_function_calendar,
    get_queryset_function_personal_address, get_queryset_function_personal_event,
    get_queryset_function_person_certificate_code
)


# 个人信息
class TransactionSocialCultureEthnicPopulationPersonalInformationPerson(BasesModelCommunalId):
    """个人信息"""
    SURNAME = fields.CharField(
        verbose_name='姓', max_length=100, blank=True, null=True, show_word_limit=True)
    NAME = fields.CharField(
        verbose_name='名称', max_length=100, blank=True, null=True, show_word_limit=True)
    SEX = fields.ForeignKey(
        'standard_encoding.ProvenanceSystemSettingsStandardCodeMainDict', verbose_name='生理性别',
        on_delete=models.CASCADE, null=True, blank=True, to_field='id', clearable=True, placeholder='生理性别',
        queryset=get_queryset_function_person_sex_physiological, )
    DATE_OF_DEATH = fields.DateField(
        verbose_name='出生日期', options=options_date, default=time.strftime("%Y-%m-%d %H:%M:%S"),
        null=True, blank=True, )
    DETAIL = editor_fields.MDTextField(verbose_name="简介", default=None, blank=True, null=True)

    class Meta:
        db_table = "TransactionSocialCultureEthnicPopulationPersonalInformationPerson"
        ordering = ['-CREATE_TIME']
        verbose_name = "个人信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.SURNAME:
            return f'{self.NAME}.{self.SURNAME}'
        else:
            return f'{self.NAME}'


# 个人国家信息
class TransactionSocialCultureEthnicPopulationPersonalInformationPersonCountry(BasesModelCommunalId):
    """个人国家信息"""
    ID_PERSON = fields.ForeignKey(
        'personal_Information.TransactionSocialCultureEthnicPopulationPersonalInformationPerson', verbose_name='个人',
        on_delete=models.CASCADE, null=True, blank=True, to_field='ID', clearable=True, placeholder='个人', )
    ID_NATION = fields.ForeignKey(
        'country.TransactionGeographyPoliticsCountryCollect', verbose_name='国籍', on_delete=models.CASCADE,
        null=True, blank=True, to_field='ID', clearable=True, placeholder='国籍', )
    DATE_OF_DEATH = fields.DateField(
        verbose_name='加入时间', options=options_date, default=time.strftime("%Y-%m-%d %H:%M:%S"), null=True,
        blank=True, )

    class Meta:
        db_table = "TransactionSocialCultureEthnicPopulationPersonalInformationPersonCountry"
        ordering = ['-CREATE_TIME']
        verbose_name = "个人国家信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.ID_PERSON}({self.ID_NATION})'


# 个人生日信息
class TransactionSocialCultureEthnicPopulationPersonalInformationPersonBirthday(BasesModelCommunalId):
    """个人生日信息"""
    ID_PERSON = fields.ForeignKey(
        'personal_Information.TransactionSocialCultureEthnicPopulationPersonalInformationPerson', verbose_name='个人',
        on_delete=models.CASCADE, null=True, blank=True, to_field='ID', clearable=True, placeholder='个人', )
    TYPE_BIRTHDAY = fields.ForeignKey(
        'standard_encoding.ProvenanceSystemSettingsStandardCodeMainDict', verbose_name='生日类别',
        on_delete=models.CASCADE, null=True, blank=True, to_field='id', clearable=True, placeholder='生日类别',
        queryset=get_queryset_function_calendar, )
    DATE_START = fields.CharField(verbose_name='生日', max_length=4, blank=True, null=True, show_word_limit=True)

    class Meta:
        db_table = "TransactionSocialCultureEthnicPopulationPersonalInformationPersonBirthday"
        ordering = ['-CREATE_TIME']
        verbose_name = "个人生日信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.ID_PERSON}:{self.TYPE_BIRTHDAY} {self.DATE_START}'


# 个人地址信息
class TransactionSocialCultureEthnicPopulationPersonalInformationPersonAddress(BasesModelCommunalId):
    """个人地址信息"""
    ID_PERSON = fields.ForeignKey(
        'personal_Information.TransactionSocialCultureEthnicPopulationPersonalInformationPerson', verbose_name='个人',
        on_delete=models.CASCADE, null=True, blank=True, to_field='ID', clearable=True, placeholder='个人', )
    TYPE_ADDRESS = fields.ForeignKey(
        'standard_encoding.ProvenanceSystemSettingsStandardCodeMainDict', verbose_name='地址类别',
        on_delete=models.CASCADE, null=True, blank=True, to_field='id', clearable=True, placeholder='地址类别',
        queryset=get_queryset_function_personal_address, )
    ADDRESS_TXT = fields.CharField(
        verbose_name='地址', help_text='输入地址', max_length=255, blank=True, null=True, show_word_limit=True)

    class Meta:
        db_table = "TransactionSocialCultureEthnicPopulationPersonalInformationPersonAddress"
        ordering = ['-CREATE_TIME']
        verbose_name = "人员地址信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.ID_PERSON}:{self.TYPE_ADDRESS}-{self.ADDRESS_TXT}'


# 个人事件记录
class TransactionSocialCultureEthnicPopulationPersonalInformationPersonEvent(BasesModelCommunalId):
    """个人事件记录"""
    ID_PERSON = fields.ForeignKey(
        'personal_Information.TransactionSocialCultureEthnicPopulationPersonalInformationPerson', verbose_name='个人',
        on_delete=models.CASCADE, null=True, blank=True, to_field='ID', clearable=True, placeholder='个人', )
    DATE = fields.DateField(
        verbose_name='发生日期', default=time.strftime("%Y-%m-%d %H:%M:%S"), blank=True, null=True,
        options=options_date)
    RTYPE_EVENT = fields.ForeignKey(
        'standard_encoding.ProvenanceSystemSettingsStandardCodeMainDict', verbose_name='事件类型',
        on_delete=models.CASCADE, null=True, blank=True, to_field='id', clearable=True, placeholder='事件类型',
        related_name='事件类型', queryset=get_queryset_function_personal_event, )
    DETAIL = editor_fields.MDTextField(verbose_name="正文", default=None, blank=True, null=True)

    class Meta:
        db_table = "TransactionSocialCultureEthnicPopulationPersonalInformationPersonEvent"
        ordering = ['-DATE']
        verbose_name = "人员事件记录"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.ID_PERSON}于{self.DATE}发生{self.RTYPE_EVENT}事件'


# 个人所属民族
class TransactionSocialCultureEthnicPopulationPersonalInformationPersonNation(BasesModelCommunalId):
    """个人所属民族"""
    ID_PERSON = fields.ForeignKey(
        'personal_Information.TransactionSocialCultureEthnicPopulationPersonalInformationPerson', verbose_name='个人',
        on_delete=models.CASCADE, null=True, blank=True, to_field='ID', clearable=True, placeholder='个人', )
    ID_NATION = fields.ForeignKey(
        'ethnic_classification_characteristics.TransactionSocialCultureEthnicPopulationEthnicClassificationCharacteristicsBrief',
        verbose_name='民族', on_delete=models.CASCADE, null=True, blank=True, to_field='ID', clearable=True,
        placeholder='民族', )

    class Meta:
        db_table = "TransactionSocialCultureEthnicPopulationPersonalInformationPersonNation"
        ordering = ['-CREATE_TIME']
        verbose_name = "个人所属民族"
        verbose_name_plural = verbose_name
        unique_together = ('ID_PERSON', 'ID_NATION')
        UniqueConstraint(
            fields=['ID_PERSON', 'ID_NATION'],
            name='unique_person_nation'
        )

    def __str__(self):
        return f'{self.ID_PERSON}:{self.ID_NATION}'


# 人员联系信息
class TransactionSocialCultureEthnicPopulationPersonalInformationPersonConnections(BasesModelCommunalId):
    """人员联系信息"""
    ID_PERSON = fields.ForeignKey(
        'personal_Information.TransactionSocialCultureEthnicPopulationPersonalInformationPerson', verbose_name='个人',
        on_delete=models.CASCADE, null=True, blank=True, to_field='ID', clearable=True, placeholder='个人', )
    ID_PRODUCTS = fields.ForeignKey(
        'products.TransactionEconomyIndustryProductsBasis', verbose_name='产品', on_delete=models.CASCADE, null=True,
        blank=True, to_field='ID', clearable=True, placeholder='产品')
    NUMBER = fields.CharField(verbose_name='账号', max_length=255, blank=True, null=True, show_word_limit=True)

    class Meta:
        db_table = "TransactionSocialCultureEthnicPopulationPersonalInformationPersonConnections"
        ordering = ['-CREATE_TIME']
        verbose_name = "人员联系信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.ID_PERSON}-{self.ID_PRODUCTS}:{self.NUMBER}'


# 人员证件信息
class TransactionSocialCultureEthnicPopulationPersonalInformationPersonCertificate(BasesModelCommunalId):
    """人员证件表"""
    ID_PERSON = fields.ForeignKey(
        'personal_Information.TransactionSocialCultureEthnicPopulationPersonalInformationPerson', verbose_name='个人',
        on_delete=models.CASCADE, null=True, blank=True, to_field='ID', clearable=True, placeholder='个人', )
    CODE = fields.ForeignKey(
        'standard_encoding.ProvenanceSystemSettingsStandardCodeMainDict', verbose_name='个人证件类别',
        on_delete=models.CASCADE, null=True, blank=True, to_field='id', clearable=True, placeholder='个人证件类别',
        queryset=get_queryset_function_person_certificate_code, )
    NUMBER = fields.CharField(
        verbose_name='证件号', help_text='证件号', max_length=255, blank=True, null=True, show_word_limit=True)
    ID_ORGANIZATIONS = fields.ForeignKey(
        'organizations.TransactionEconomyIndustryOrganizationsBases', verbose_name='证件签发组织',
        on_delete=models.CASCADE,
        null=True, blank=True, to_field='ID', clearable=True, placeholder='证件签发组织', related_name='证件签发组织')
    DATE_ISSUED = fields.DateField(
        verbose_name='证件签发日期', options=options_date, default=time.strftime("%Y-%m-%d %H:%M:%S"), blank=True,
        null=True, )
    DATE_START = fields.DateField(
        verbose_name='证件有效开始日期', default=time.strftime("%Y-%m-%d %H:%M:%S"), blank=True, null=True, )
    DATE_END = fields.DateField(
        verbose_name='证件有效结束日期', default=time.strftime("%Y-%m-%d %H:%M:%S"), blank=True, null=True, )

    class Meta:
        db_table = "TransactionSocialCultureEthnicPopulationPersonalInformationPersonCertificate"
        ordering = ['-CREATE_TIME']
        verbose_name = "人员证件信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.ID_PERSON}-{self.CODE}'
