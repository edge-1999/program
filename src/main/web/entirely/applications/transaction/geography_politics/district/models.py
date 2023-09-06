from django.db import models
from simplepro.components import fields
from docs.utils.model_communal.model_communal import BasesModelCommunal
from docs.utils.model_communal.model_filter import get_combobox_queryset
from docs.utils.model_communal.model_queryset import get_queryset_politics_district_code


# 城镇信息
class TransactionGeographyPoliticsDistrictBasic(BasesModelCommunal):
    """城镇信息"""
    ID_NATION = fields.ForeignKey(
        'country.TransactionGeographyPoliticsCountryCollect', verbose_name='国家', on_delete=models.CASCADE, null=True,
        blank=True, to_field='ID', clearable=True, placeholder='国家', )
    TYPE_TOWN = fields.ForeignKey(
        'standard_encoding.ProvenanceSystemSettingsStandardCodeMainDict', verbose_name='位置类别',
        on_delete=models.CASCADE, null=True, blank=True, to_field='id', clearable=True, placeholder='位置类别',
        queryset=get_queryset_politics_district_code, )
    NAME_CHINESE = fields.CharField(
        verbose_name='位置中文名称', max_length=255, blank=True, null=True, show_word_limit=True)
    NAME_ENGLISH = fields.CharField(
        verbose_name='位置英文名称', max_length=255, blank=True, null=True, show_word_limit=True)
    ID_SUBORDINATE = fields.CharField(
        verbose_name='位置编码', max_length=255, blank=True, null=True, show_word_limit=True)
    ID_PARENT = fields.TreeComboboxField(
        'district.TransactionGeographyPoliticsDistrictBasic', on_delete=models.CASCADE, null=True, blank=True,
        verbose_name='父级位置', to_field='id', strictly=True, queryset=get_combobox_queryset, )

    class Meta:
        db_table = "TransactionGeographyPoliticsDistrictBasic"
        ordering = ['-CREATE_TIME']
        verbose_name = "城镇信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.NAME_CHINESE:
            return f'{self.NAME_CHINESE}'
        elif self.NAME_ENGLISH:
            return f'{self.NAME_ENGLISH}'
        else:
            return f'{self.id}'
