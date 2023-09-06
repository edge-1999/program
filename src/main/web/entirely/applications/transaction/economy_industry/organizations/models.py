import time

from django.db import models
from simplepro.components import fields
from simplepro.editor import fields as editor_fields

from docs.utils.system_communal.configuration import options_date
from docs.utils.model_communal.model_communal import BasesModelCommunalId
from docs.utils.model_communal.model_queryset import get_queryset_function_organization_category, \
    get_queryset_function_organization_address_code, get_queryset_function_organization_category_code, \
    get_queryset_function_organization_certificate_code
from docs.utils.model_communal.model_values_filter import select_organizations_details


# 组织基本信息
class TransactionEconomyIndustryOrganizationsBases(BasesModelCommunalId):
    """组织基本信息"""
    ENTERPRISE_NAME = fields.CharField(
        verbose_name='组织名称', max_length=255, blank=False, null=False, show_word_limit=True)
    ENTERPRISE_CODE = fields.ForeignKey(
        'standard_encoding.ProvenanceSystemSettingsStandardCodeMainDict', verbose_name='组织类别',
        on_delete=models.CASCADE, null=True, blank=True, to_field='id', clearable=True, placeholder='组织类别',
        queryset=get_queryset_function_organization_category, )
    COUNTRY_CREATE_TIME = fields.DateField(
        verbose_name='成立时间', options=options_date, default=time.strftime("%Y-%m-%d"), null=True, blank=True, )
    COUNTRY_END_TIME = fields.DateField(
        verbose_name='结束时间', default=time.strftime("%Y-%m-%d"), blank=True, null=True)

    class Meta:
        db_table = "TransactionEconomyIndustryOrganizationsBases"
        ordering = ['-CREATE_TIME']
        verbose_name = "组织基本信息"
        verbose_name_plural = verbose_name
        unique_together = ('ENTERPRISE_NAME', 'ENTERPRISE_CODE',)

    def __str__(self):
        return f'{self.ENTERPRISE_NAME}'


# 组织称呼信息
class TransactionEconomyIndustryOrganizationsCall(BasesModelCommunalId):
    """组织称呼信息"""
    ID_ORGANIZATIONS = fields.ForeignKey(
        'organizations.TransactionEconomyIndustryOrganizationsBases', verbose_name='组织', on_delete=models.CASCADE,
        null=True, blank=True, to_field='ID', clearable=True, placeholder='组织', )
    ENTERPRISE_NAME_CODE = fields.ForeignKey(
        'standard_encoding.ProvenanceSystemSettingsStandardCodeMainDict', verbose_name='组织称呼类型',
        on_delete=models.CASCADE, null=True, blank=True, to_field='id', clearable=True, placeholder='组织称呼类型',
        queryset=get_queryset_function_organization_category_code, )
    ENTERPRISE_NAME = fields.CharField(
        verbose_name='名称', max_length=255, blank=False, null=False, show_word_limit=True)

    class Meta:
        db_table = "TransactionEconomyIndustryOrganizationsCall"
        ordering = ['-CREATE_TIME']
        verbose_name = "组织称呼信息"
        verbose_name_plural = verbose_name
        unique_together = ('ID_ORGANIZATIONS', 'ENTERPRISE_NAME_CODE', 'ENTERPRISE_NAME')

    def __str__(self):
        return f'{self.ID_ORGANIZATIONS}'


# 组织地址信息
class TransactionEconomyIndustryOrganizationsAddress(BasesModelCommunalId):
    """组织地址信息"""
    ID_ORGANIZATIONS = fields.ForeignKey(
        'organizations.TransactionEconomyIndustryOrganizationsBases', verbose_name='组织', on_delete=models.CASCADE,
        null=True, blank=True, to_field='ID', clearable=True, placeholder='组织', )
    ENTERPRISE_ADDRESS_CODE = fields.ForeignKey(
        'standard_encoding.ProvenanceSystemSettingsStandardCodeMainDict', verbose_name='组织地址类型',
        on_delete=models.CASCADE, null=True, blank=True, to_field='id', clearable=True, placeholder='组织地址类型',
        queryset=get_queryset_function_organization_address_code, )
    ENTERPRISE_ADDRESS_NAME = fields.CharField(
        verbose_name='地址', max_length=255, blank=False, null=False, show_word_limit=True)

    class Meta:
        db_table = "TransactionEconomyIndustryOrganizationsAddress"
        ordering = ['-CREATE_TIME']
        verbose_name = "组织地址信息"
        verbose_name_plural = verbose_name
        unique_together = ('ID_ORGANIZATIONS', 'ENTERPRISE_ADDRESS_CODE', 'ENTERPRISE_ADDRESS_NAME')

    def __str__(self):
        return f'{self.ID_ORGANIZATIONS}'


# 组织详情描述
class TransactionEconomyIndustryOrganizationsDetails(BasesModelCommunalId):
    """组织详情描述"""
    ID_ORGANIZATIONS = fields.ForeignKey(
        'organizations.TransactionEconomyIndustryOrganizationsBases', verbose_name='组织', on_delete=models.CASCADE,
        null=True, blank=True, to_field='ID', clearable=True, placeholder='组织', )
    DETAIL = editor_fields.MDTextField(
        verbose_name="详情描述", default=select_organizations_details(), blank=True, null=True)

    class Meta:
        db_table = "TransactionEconomyIndustryOrganizationsDetails"
        ordering = ['-CREATE_TIME']
        verbose_name = "组织详情描述"
        verbose_name_plural = verbose_name
        unique_together = ('ID_ORGANIZATIONS',)

    def __str__(self):
        return f'{self.ID_ORGANIZATIONS}'


# 组织证件信息
class TransactionEconomyIndustryOrganizationsCertificate(BasesModelCommunalId):
    """组织证件信息"""
    ID_ORGANIZATIONS = fields.ForeignKey(
        'organizations.TransactionEconomyIndustryOrganizationsBases', verbose_name='组织', on_delete=models.CASCADE,
        null=True, blank=True, to_field='ID', clearable=True, placeholder='组织', related_name='组织')
    SIGNING_AND_ISSUING_ORGANIZATION = fields.ForeignKey(
        'organizations.TransactionEconomyIndustryOrganizationsBases', verbose_name='签发机关', on_delete=models.CASCADE,
        null=True, blank=True, to_field='ID', clearable=True, placeholder='签发机关', related_name='签发机关')
    DATE_ISSUED = fields.DateField(
        verbose_name='签发日期', options=options_date, default=time.strftime("%Y-%m-%d %H:%M:%S"), blank=True,
        null=True, )
    CODE = fields.ForeignKey(
        'standard_encoding.ProvenanceSystemSettingsStandardCodeMainDict', verbose_name='组织证件类别',
        on_delete=models.CASCADE, null=True, blank=True, to_field='id', clearable=True, placeholder='组织证件类别',
        queryset=get_queryset_function_organization_certificate_code, )
    NUMBER = fields.CharField(verbose_name='组织证件号', max_length=255, blank=True, null=True, show_word_limit=True)
    DATE_START = fields.DateField(
        verbose_name='组织证件号有效开始日期', options=options_date, default=time.strftime("%Y-%m-%d %H:%M:%S"),
        blank=True, null=True, )
    DATE_END = fields.DateField(
        verbose_name='组织证件号有效结束日期', default=time.strftime("%Y-%m-%d %H:%M:%S"), blank=True, null=True, )

    class Meta:
        db_table = "TransactionEconomyIndustryOrganizationsCertificate"
        ordering = ['-CREATE_TIME']
        verbose_name = "组织证件信息"
        verbose_name_plural = verbose_name
        unique_together = ('ID_ORGANIZATIONS', 'NUMBER',)

    def __str__(self):
        return f'{self.ID_ORGANIZATIONS}'


# 组织联系方式
class TransactionEconomyIndustryOrganizationsContact(BasesModelCommunalId):
    """组织联系方式"""
    ID_ORGANIZATIONS = fields.ForeignKey(
        'organizations.TransactionEconomyIndustryOrganizationsBases', verbose_name='组织', on_delete=models.CASCADE,
        null=True, blank=True, to_field='ID', clearable=True, placeholder='组织')
    ID_PRODUCTS = fields.ForeignKey(
        'products.TransactionEconomyIndustryProductsBasis', verbose_name='产品', on_delete=models.CASCADE, null=True,
        blank=True, to_field='ID', clearable=True, placeholder='产品')
    NUMBER = fields.CharField(verbose_name='编号', max_length=255, blank=True, null=True, show_word_limit=True)

    class Meta:
        db_table = "TransactionEconomyIndustryOrganizationsContact"
        ordering = ['-CREATE_TIME']
        verbose_name = "组织联系表方式"
        verbose_name_plural = verbose_name
        unique_together = ('ID_ORGANIZATIONS', 'ID_PRODUCTS', 'NUMBER',)

    def __str__(self):
        return f'{self.ID_ORGANIZATIONS}:{self.ID_PRODUCTS}'
