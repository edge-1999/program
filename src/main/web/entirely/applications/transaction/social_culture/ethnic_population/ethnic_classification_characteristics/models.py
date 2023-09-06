from simplepro.components import fields
from simplepro.editor import fields as editor_fields

from docs.utils.model_communal.model_communal import BasesModelCommunalId
from docs.utils.model_communal.model_values_filter import select_ethnic_classification_characteristics_brief


# 民族基本信息
class TransactionSocialCultureEthnicPopulationEthnicClassificationCharacteristicsBrief(BasesModelCommunalId):
    """民族基本信息"""
    NAME = fields.CharField(verbose_name='名称', max_length=127, blank=True, null=True, show_word_limit=True)
    DETAIL = editor_fields.MDTextField(
        verbose_name="简介", default=select_ethnic_classification_characteristics_brief(), blank=True, null=True)

    class Meta:
        db_table = "TransactionSocialCultureEthnicPopulationEthnicClassificationCharacteristicsBrief"
        ordering = ['-CREATE_TIME']
        verbose_name = "民族基本信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.NAME}'
