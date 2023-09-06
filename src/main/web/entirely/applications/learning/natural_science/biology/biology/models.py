from django.db import models
from simplepro.components import fields

from docs.utils.model_communal.model_communal import BasesModelCommunal
from docs.utils.model_communal.model_filter import get_combobox_queryset
from docs.utils.model_communal.model_queryset import get_queryset_function_authority_type_data


class LearningNaturalScienceBiologicalSpecies(BasesModelCommunal):
    """生物种类"""
    NAME_CHINESE = fields.CharField(
        verbose_name='中文描述', max_length=255, blank=True, null=True, show_word_limit=True)
    NAME_ENGLISH = fields.CharField(
        verbose_name='英文描述', max_length=255, blank=True, null=True, show_word_limit=True)
    NAME_REFERRED_TO_AS = fields.CharField(
        verbose_name='简称', max_length=255, blank=True, null=True, show_word_limit=True)
    STATUS_IS_EXTINCTION = models.BooleanField(verbose_name="是否灭绝", default=False, blank=False, null=False)
    ID_PARENT = fields.TreeComboboxField(
        'biology.LearningNaturalScienceBiologicalSpecies', on_delete=models.CASCADE, null=True, blank=True,
        verbose_name='上级', to_field='id', strictly=True, queryset=get_combobox_queryset, )
    STATUS_AUTHORITY = fields.ForeignKey(
        'standard_encoding.ProvenanceSystemSettingsStandardCodeMainDict', verbose_name='权限控制',
        on_delete=models.CASCADE, null=True, blank=True, clearable=True,
        placeholder='权限控制', queryset=get_queryset_function_authority_type_data, )

    class Meta:
        db_table = "LearningNaturalScienceBiologicalSpecies"
        ordering = ['-CREATE_TIME']
        verbose_name = "生物种类"
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.NAME_REFERRED_TO_AS:
            return f'{self.NAME_REFERRED_TO_AS}'
        elif self.NAME_CHINESE and self.NAME_ENGLISH:
            return f'{self.NAME_CHINESE}({self.NAME_ENGLISH})'
        elif self.NAME_CHINESE:
            return f'{self.NAME_CHINESE}'
        elif self.NAME_ENGLISH:
            return f'{self.NAME_ENGLISH}'
        else:
            return f'{self.id}'
