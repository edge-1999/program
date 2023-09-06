from django.db import models
from simplepro.components import fields

from docs.utils.model_communal.model_communal import BasesModelCommunal
from docs.utils.model_communal.model_filter import get_combobox_queryset
from docs.utils.model_communal.model_queryset import get_queryset_function_authority_type_data


# 天体基本信息
class LearningNaturalScienceAstronomyCosmologyCode(BasesModelCommunal):
    """天体基本信息"""
    NAME = fields.CharField(verbose_name='中文描述', max_length=100, blank=True, null=True, show_word_limit=True)
    STATUS_AUTHORITY = fields.ForeignKey(
        'standard_encoding.ProvenanceSystemSettingsStandardCodeMainDict', verbose_name='权限控制',
        on_delete=models.CASCADE, null=True, related_name='权限控制', blank=True, clearable=True,
        placeholder='权限控制', queryset=get_queryset_function_authority_type_data, )
    ID_PARENT = fields.TreeComboboxField(
        'cosmology.LearningNaturalScienceAstronomyCosmologyCode', on_delete=models.CASCADE, null=True, blank=True,
        verbose_name='父级', to_field='id', strictly=True, queryset=get_combobox_queryset, )

    class Meta:
        db_table = "LearningNaturalScienceAstronomyCosmologyCode"
        ordering = ['-CREATE_TIME']
        verbose_name = "天体基本信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.NAME}'
