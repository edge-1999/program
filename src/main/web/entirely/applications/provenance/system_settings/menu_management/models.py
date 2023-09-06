from django.db import models

from simplepro.components import fields

from docs.utils.model_communal.model_communal import BasesModelCommunal, BasesModelCommunalId
from docs.utils.model_communal.model_filter import get_combobox_queryset


# 菜单管理
class ProvenanceSystemSettingsMenuManagementMenu(BasesModelCommunal):
    """菜单管理"""
    NAME = fields.CharField(verbose_name='中文描述', max_length=255, blank=False, null=False, show_word_limit=True)
    ID_PARENT = fields.TreeComboboxField(
        'menu_management.ProvenanceSystemSettingsMenuManagementMenu', on_delete=models.CASCADE, null=True,
        blank=True, verbose_name='上级', to_field='id', strictly=True, queryset=get_combobox_queryset, )

    class Meta:
        db_table = "ProvenanceSystemSettingsMenuManagementMenu"
        ordering = ['-CREATE_TIME']
        verbose_name = "菜单管理"
        verbose_name_plural = verbose_name
        unique_together = ('id', 'ID_PARENT',)

    def __str__(self):
        return f'{self.ID_PARENT if self.ID_PARENT else ""}{self.NAME}'


# 菜单参数
class ProvenanceSystemSettingsMenuManagementMenuParameter(BasesModelCommunal):
    """菜单参数"""
    ID_MENU = fields.ForeignKey(
        'menu_management.ProvenanceSystemSettingsMenuManagementMenu', verbose_name='菜单',
        on_delete=models.CASCADE, null=True, blank=True, to_field='id', clearable=True, placeholder='菜单', )
    APP_URL_NAME = fields.CharField(
        verbose_name='APP URL NAME', max_length=255, blank=True, null=True, show_word_limit=True)
    URL_NAME = fields.CharField(verbose_name='URL NAME', max_length=255, blank=True, null=True, show_word_limit=True)
    ICON = fields.CharField(verbose_name='图标', max_length=255, blank=True, null=True, show_word_limit=True)

    class Meta:
        db_table = "ProvenanceSystemSettingsMenuManagementMenuParameter"
        ordering = ['-CREATE_TIME']
        verbose_name = "菜单参数"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.ID_MENU}'


# 菜单权限
class ProvenanceSystemSettingsMenuManagementMenuPermission(BasesModelCommunalId):
    """菜单权限"""
    ID_MENU = fields.ForeignKey(
        'menu_management.ProvenanceSystemSettingsMenuManagementMenu', verbose_name='菜单',
        on_delete=models.CASCADE, null=True, blank=True, to_field='id', clearable=True, placeholder='菜单', )
    ID_AUTHORITY = fields.ForeignKey(
        'account_management.ProvenanceSystemSettingsAccountManagementAuthority', verbose_name='权限',
        on_delete=models.CASCADE, null=True, blank=True, to_field='id', clearable=True, placeholder='权限', )

    class Meta:
        db_table = "ProvenanceSystemSettingsMenuManagementMenuPermission"
        ordering = ['-CREATE_TIME']
        verbose_name = "菜单权限"
        verbose_name_plural = verbose_name
        unique_together = ('ID_MENU', 'ID_AUTHORITY')

    def __str__(self):
        return f'{self.ID_MENU}{self.ID_AUTHORITY}'


class ProvenanceSystemSettingsMenuManagementMenuRoleDisplay(BasesModelCommunalId):
    """角色对应的菜单 菜单展示，仅限查看查看菜单"""
    ID_ROLE = fields.ForeignKey(
        'account_management.ProvenanceSystemSettingsAccountManagementRole', verbose_name='角色',
        on_delete=models.CASCADE, null=True, blank=True, to_field='id', clearable=True, placeholder='角色', )
    ID_MENU = fields.ForeignKey(
        'menu_management.ProvenanceSystemSettingsMenuManagementMenu', verbose_name='菜单',
        on_delete=models.CASCADE, null=True, blank=True, to_field='id', clearable=True, placeholder='菜单', )

    class Meta:
        db_table = "ProvenanceSystemSettingsMenuManagementMenuRoleDisplay"
        ordering = ['-CREATE_TIME']
        verbose_name = "菜单展示"
        verbose_name_plural = verbose_name
        unique_together = ('ID_ROLE', 'ID_MENU')

    def __str__(self):
        return f'{self.ID_MENU}{self.ID_ROLE}'
