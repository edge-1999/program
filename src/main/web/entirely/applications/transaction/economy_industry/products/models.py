from django.db import models
from simplepro.components import fields
from simplepro.editor import fields as editor_fields

from docs.utils.model_communal.model_communal import BasesModelCommunalId
from docs.utils.model_communal.model_queryset import (
    get_queryset_function_products_type, get_queryset_function_organization_category_code
)
from docs.utils.model_communal.model_values_filter import select_products_detail


# 产品基本信息
class TransactionEconomyIndustryProductsBasis(BasesModelCommunalId):
    """产品基本信息"""
    PRODUCTS_NAME = fields.CharField(
        verbose_name='产品名称', max_length=255, blank=True, null=True, show_word_limit=True)
    PRODUCTS_URL = models.URLField(verbose_name='网站链接', null=True, blank=True)
    DETAIL = editor_fields.MDTextField(verbose_name="详情描述", default=select_products_detail(), blank=True, null=True)

    class Meta:
        db_table = "TransactionEconomyIndustryProductsBasis"
        ordering = ['-CREATE_TIME']
        verbose_name = "产品基本信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.PRODUCTS_NAME}'


# 产品所属组织
class TransactionEconomyIndustryProductsAffiliation(BasesModelCommunalId):
    """产品所属组织"""
    ID_PRODUCTS = fields.ForeignKey(
        'products.TransactionEconomyIndustryProductsBasis', verbose_name='产品', on_delete=models.CASCADE, null=True,
        blank=True, to_field='ID', clearable=True, placeholder='产品')
    ID_ORGANIZATIONS = fields.ForeignKey(
        'organizations.TransactionEconomyIndustryOrganizationsBases', verbose_name='组织', on_delete=models.CASCADE,
        null=True, blank=True, to_field='ID', clearable=True, placeholder='组织', )

    class Meta:
        db_table = "TransactionEconomyIndustryProductsAffiliation"
        ordering = ['-CREATE_TIME']
        verbose_name = "产品所属组织"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.ID_PRODUCTS}:{self.ID_ORGANIZATIONS}'


# 产品类型
class TransactionEconomyIndustryProductsType(BasesModelCommunalId):
    """产品类型"""
    ID_PRODUCTS = fields.ForeignKey(
        'products.TransactionEconomyIndustryProductsBasis', verbose_name='产品', on_delete=models.CASCADE, null=True,
        blank=True, to_field='ID', clearable=True, placeholder='产品')
    PRODUCTS_CODE = fields.ForeignKey(
        'standard_encoding.ProvenanceSystemSettingsStandardCodeMainDict', verbose_name='产品类型',
        on_delete=models.CASCADE, null=True, blank=True, to_field='id', clearable=True, placeholder='产品类型',
        queryset=get_queryset_function_products_type, )

    class Meta:
        db_table = "TransactionEconomyIndustryProductsType"
        ordering = ['-CREATE_TIME']
        verbose_name = "产品类型"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.ID_PRODUCTS}:{self.PRODUCTS_CODE}'


# 产品称呼信息
class TransactionEconomyIndustryProductsCall(BasesModelCommunalId):
    """产品称呼信息"""
    ID_PRODUCTS = fields.ForeignKey(
        'products.TransactionEconomyIndustryProductsBasis', verbose_name='产品', on_delete=models.CASCADE, null=True,
        blank=True, to_field='ID', clearable=True, placeholder='产品')
    NAME_CODE = fields.ForeignKey(
        'standard_encoding.ProvenanceSystemSettingsStandardCodeMainDict', verbose_name='称呼类型',
        on_delete=models.CASCADE, null=True, blank=True, to_field='id', clearable=True, placeholder='称呼类型',
        queryset=get_queryset_function_organization_category_code, )
    NAME = fields.CharField(verbose_name='名称', max_length=255, blank=False, null=False, show_word_limit=True)

    class Meta:
        db_table = "TransactionEconomyIndustryProductsCall"
        ordering = ['-CREATE_TIME']
        verbose_name = "产品称呼信息"
        verbose_name_plural = verbose_name
        unique_together = ('ID_PRODUCTS', 'NAME_CODE', 'NAME')

    def __str__(self):
        return f'{self.ID_PRODUCTS}'
