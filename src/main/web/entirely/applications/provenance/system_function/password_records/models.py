from django.db import models
from simplepro.components import fields
from simplepro.editor import fields as editor_fields

from docs.utils.model_communal.model_communal import BasesModelCommunalId
from docs.utils.model_communal.model_queryset import get_queryset_password_correlation_code
from docs.utils.model_communal.model_values_filter import select_password_records


# 人员密码
class ProvenanceSystemFunctionPasswordRecords(BasesModelCommunalId):
    """人员密码"""
    ID_PERSON = fields.ForeignKey(
        'personal_Information.TransactionSocialCultureEthnicPopulationPersonalInformationPerson',
        verbose_name='记录人员', on_delete=models.CASCADE, null=False, blank=False, to_field='ID', clearable=True,
        placeholder='记录人员', )
    ID_PRODUCTS = fields.ForeignKey(
        'products.TransactionEconomyIndustryProductsBasis', verbose_name='产品', on_delete=models.CASCADE, null=False,
        blank=False, to_field='ID', clearable=True, placeholder='产品')
    NUMBER = fields.CharField(verbose_name='账号', max_length=255, blank=True, null=True, show_word_limit=True)
    PASSWORD = fields.CharField(verbose_name='密码', max_length=255, blank=True, null=True, show_password=True)
    DETAIL = editor_fields.MDTextField(
        verbose_name="详情描述", default=select_password_records(), blank=True, null=True)

    class Meta:
        db_table = "ProvenanceSystemFunctionPasswordRecords"
        ordering = ['-CREATE_TIME']
        verbose_name = "人员密码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.ID_PERSON}·{self.ID_PRODUCTS}{":" + str(self.NUMBER) if self.NUMBER else ""}'


# 产品账户关联
class ProvenanceSystemFunctionPasswordCorrelation(BasesModelCommunalId):
    """产品账户关联"""
    ID_PASSWORD = fields.ForeignKey(
        'password_records.ProvenanceSystemFunctionPasswordRecords', verbose_name='产品账户', on_delete=models.CASCADE,
        null=False, blank=False, to_field='ID', clearable=True, placeholder='产品账户', related_name='产品账户')
    ID_PASSWORD_RELATION = fields.ForeignKey(
        'password_records.ProvenanceSystemFunctionPasswordRecords', verbose_name='产品账户', on_delete=models.CASCADE,
        null=False, blank=False, to_field='ID', clearable=True, placeholder='产品账户', related_name='产品关联账户')
    CODE = fields.ForeignKey(
        'standard_encoding.ProvenanceSystemSettingsStandardCodeMainDict', verbose_name='产品关联类别',
        placeholder='产品关联类别', on_delete=models.CASCADE, null=False, blank=False, to_field='id', clearable=True,
        queryset=get_queryset_password_correlation_code, )

    class Meta:
        db_table = "ProvenanceSystemFunctionPasswordCorrelation"
        ordering = ['-CREATE_TIME']
        verbose_name = "产品账户关联"
        verbose_name_plural = verbose_name
        unique_together = ('ID_PASSWORD', 'ID_PASSWORD_RELATION',)

    def __str__(self):
        return f'{self.ID_PASSWORD}-{self.ID_PASSWORD_RELATION}'
