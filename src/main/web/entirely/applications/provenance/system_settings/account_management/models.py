import uuid

from django.contrib.auth.models import AbstractUser, UserManager, AbstractBaseUser
from django.db import models
from simplepro.components import fields
from simplepro.editor import fields as editor_fields

from docs.utils.model_communal.model_communal import BasesModelCommunalId, BasesModelCommunal
from docs.utils.model_communal.model_filter import get_combobox_queryset
from docs.utils.model_communal.model_queryset import get_queryset_account_management_subscriber_land, \
    get_queryset_function_permission_control_menu


class ProvenanceSystemSettingsAccountManagementSuperManager(UserManager):
    """
    自定义 user manager self, username, email=None, password=None, **extra_fields
    """

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        return super().create_superuser(username=username, password=password, email=email, **extra_fields)


class ProvenanceSystemSettingsAccountManagementSuper(AbstractUser):
    """
    超级用户表
    """
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    username = models.CharField(verbose_name='用户姓名', max_length=128, blank=False, default=False, unique=True)
    mobile = models.CharField(
        verbose_name='手机号', db_index=True, max_length=32, unique=True, blank=False, null=False,
        error_messages={'unique': 'This mobile number is already registered'})
    email = models.CharField(verbose_name='邮箱', db_index=True, max_length=255, unique=True, blank=False, null=False)

    class Meta:
        db_table = 'ProvenanceSystemSettingsAccountManagementSuper'
        verbose_name = '超级用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

    REQUIRED_FIELDS = ['mobile', 'email']  # 必输项
    objects = ProvenanceSystemSettingsAccountManagementSuperManager()


# 订阅用户
class ProvenanceSystemSettingsAccountManagementSubscriber(BasesModelCommunalId):
    """订阅用户"""
    NAME = fields.CharField(verbose_name='账户', max_length=255, blank=True, null=True, show_word_limit=True)
    PASSWORD = fields.CharField(verbose_name='密码', max_length=255, blank=True, null=True, show_password=True)

    class Meta:
        db_table = "ProvenanceSystemSettingsAccountManagementSubscriber"
        ordering = ['-CREATE_TIME']
        verbose_name = "订阅用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.NAME}'


# 关联登陆
class ProvenanceSystemSettingsAccountManagementSubscriberLand(BasesModelCommunalId):
    """关联登陆"""
    ID_SUBSCRIBER = fields.ForeignKey(
        'account_management.ProvenanceSystemSettingsAccountManagementSubscriber', verbose_name='订阅用户',
        on_delete=models.CASCADE, null=False, blank=False, to_field='ID', clearable=True, placeholder='订阅用户', )
    UNIQUE_NUMBER = fields.CharField(verbose_name='账号', max_length=255, blank=True, null=True, show_word_limit=True)
    CODE = fields.ForeignKey(
        'standard_encoding.ProvenanceSystemSettingsStandardCodeMainDict', verbose_name='关联登陆',
        placeholder='关联登陆', on_delete=models.CASCADE, null=False, blank=False, to_field='id', clearable=True,
        queryset=get_queryset_account_management_subscriber_land, )

    class Meta:
        db_table = "ProvenanceSystemSettingsAccountManagementSubscriberLand"
        ordering = ['-CREATE_TIME']
        verbose_name = "关联登陆"
        verbose_name_plural = verbose_name
        unique_together = ('ID_SUBSCRIBER', 'UNIQUE_NUMBER', 'CODE')

    def __str__(self):
        return f'{self.ID_SUBSCRIBER}·{self.CODE}'


# 用户组
class ProvenanceSystemSettingsAccountManagementSubscriberGroup(BasesModelCommunal):
    """用户组"""
    NAME = fields.CharField(
        verbose_name='组名', max_length=255, blank=True, null=True, show_word_limit=True, unique=True)
    ID_PARENT = fields.TreeComboboxField(
        'account_management.ProvenanceSystemSettingsAccountManagementSubscriberGroup', on_delete=models.CASCADE,
        null=True, blank=True, verbose_name='上级', to_field='id', strictly=True, queryset=get_combobox_queryset, )
    DETAIL = editor_fields.MDTextField(verbose_name="详细说明", default=None, blank=True, null=True)

    class Meta:
        db_table = "ProvenanceSystemSettingsAccountManagementSubscriberGroup"
        ordering = ['-CREATE_TIME']
        verbose_name = "用户组"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.ID_PARENT if self.ID_PARENT else ""}{self.NAME}'


# 订阅用户组
class ProvenanceSystemSettingsAccountManagementSubscriberGroupAccount(BasesModelCommunal):
    """订阅用户组"""
    ID_SUBSCRIBER = fields.ForeignKey(
        'account_management.ProvenanceSystemSettingsAccountManagementSubscriber', verbose_name='订阅用户',
        on_delete=models.CASCADE, null=True, blank=True, to_field='ID', clearable=True, placeholder='订阅用户', )
    ID_SUBSCRIBER_GROUP = fields.ForeignKey(
        'account_management.ProvenanceSystemSettingsAccountManagementSubscriberGroup', verbose_name='用户组',
        on_delete=models.CASCADE, null=True, blank=True, to_field='id', clearable=True, placeholder='用户组', )

    class Meta:
        db_table = "ProvenanceSystemSettingsAccountManagementSubscriberGroupAccount"
        ordering = ['-CREATE_TIME']
        verbose_name = "订阅用户组"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.ID_SUBSCRIBER_GROUP}{self.ID_SUBSCRIBER}'


# 角色管理
class ProvenanceSystemSettingsAccountManagementRole(BasesModelCommunal):
    """角色管理"""
    NAME = fields.CharField(
        verbose_name='角色名称', max_length=255, blank=True, null=True, show_word_limit=True, unique=True)
    ID_PARENT = fields.TreeComboboxField(
        'account_management.ProvenanceSystemSettingsAccountManagementRole', on_delete=models.CASCADE, null=True,
        blank=True, verbose_name='上级', to_field='id', strictly=True, queryset=get_combobox_queryset, )

    class Meta:
        db_table = "ProvenanceSystemSettingsAccountManagementRole"
        ordering = ['-CREATE_TIME']
        verbose_name = "角色管理"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.ID_PARENT if self.ID_PARENT else ""}{self.NAME}'


# 用户角色
class ProvenanceSystemSettingsAccountManagementRoleSubscriber(BasesModelCommunalId):
    """用户角色"""
    ID_ROLE = fields.ForeignKey(
        'account_management.ProvenanceSystemSettingsAccountManagementRole', verbose_name='角色',
        on_delete=models.CASCADE, null=True, blank=True, to_field='id', clearable=True, placeholder='角色', )
    ID_SUBSCRIBER = fields.ForeignKey(
        'account_management.ProvenanceSystemSettingsAccountManagementSubscriber', verbose_name='订阅用户',
        on_delete=models.CASCADE, null=True, blank=True, to_field='ID', clearable=True, placeholder='订阅用户', )

    class Meta:
        db_table = "ProvenanceSystemSettingsAccountManagementRoleSubscriber"
        ordering = ['-CREATE_TIME']
        verbose_name = "用户角色"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.ID_ROLE}{self.ID_SUBSCRIBER}'


# 用户组角色
class ProvenanceSystemSettingsAccountManagementRoleSubscriberGroup(BasesModelCommunalId):
    """用户组角色"""
    ID_ROLE = fields.ForeignKey(
        'account_management.ProvenanceSystemSettingsAccountManagementRole', verbose_name='角色',
        on_delete=models.CASCADE, null=True, blank=True, to_field='id', clearable=True, placeholder='角色', )
    ID_SUBSCRIBER_GROUP = fields.ForeignKey(
        'account_management.ProvenanceSystemSettingsAccountManagementSubscriberGroup', verbose_name='用户组',
        on_delete=models.CASCADE, null=True, blank=True, to_field='id', clearable=True, placeholder='用户组', )

    class Meta:
        db_table = "ProvenanceSystemSettingsAccountManagementRoleSubscriberGroup"
        ordering = ['-CREATE_TIME']
        verbose_name = "用户组角色"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.ID_ROLE}{self.ID_SUBSCRIBER_GROUP}'


# 权限管理
class ProvenanceSystemSettingsAccountManagementAuthority(BasesModelCommunal):
    """权限管理"""
    NAME = fields.CharField(
        verbose_name='权限名称', max_length=255, blank=True, null=True, show_word_limit=True, unique=True)
    CODE = fields.ForeignKey(
        'standard_encoding.ProvenanceSystemSettingsStandardCodeMainDict', verbose_name='权限类别',
        placeholder='权限类别', on_delete=models.CASCADE, null=True, blank=True, to_field='id', clearable=True,
        queryset=get_queryset_function_permission_control_menu, )
    ID_PARENT = fields.TreeComboboxField(
        'account_management.ProvenanceSystemSettingsAccountManagementAuthority', on_delete=models.CASCADE, null=True,
        blank=True, verbose_name='上级', to_field='id', strictly=True, queryset=get_combobox_queryset, )

    class Meta:
        db_table = "ProvenanceSystemSettingsAccountManagementAuthority"
        ordering = ['-CREATE_TIME']
        verbose_name = "权限管理"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.NAME}'


class ProvenanceSystemSettingsAccountManagementPermissionMenuDisplay(BasesModelCommunalId):
    """菜单需要展示的对应权限"""
    ID_DISPLAY = fields.ForeignKey(
        'menu_management.ProvenanceSystemSettingsMenuManagementMenuRoleDisplay', verbose_name='展示菜单',
        on_delete=models.CASCADE, null=True, blank=True, to_field='ID', clearable=True, placeholder='展示菜单', )
    ID_AUTHORITY = fields.ForeignKey(
        'account_management.ProvenanceSystemSettingsAccountManagementAuthority', verbose_name='权限',
        on_delete=models.CASCADE, null=True, blank=True, to_field='id', clearable=True, placeholder='权限', )

    class Meta:
        db_table = "ProvenanceSystemSettingsAccountManagementPermissionMenuDisplay"
        ordering = ['-CREATE_TIME']
        verbose_name = "菜单展示"
        verbose_name_plural = verbose_name
        unique_together = ('ID_DISPLAY', 'ID_AUTHORITY')

    def __str__(self):
        return f'{self.ID_DISPLAY}{self.ID_AUTHORITY}'


# 权限结果
class ProvenanceSystemSettingsAccountManagementPermissionResults(BasesModelCommunalId):
    """权限结果"""
    ID_AUTHORITY = fields.ForeignKey(
        'account_management.ProvenanceSystemSettingsAccountManagementAuthority', verbose_name='权限',
        on_delete=models.CASCADE, null=True, blank=True, to_field='id', clearable=True, placeholder='权限', )
    ID_SUBSCRIBER = fields.ForeignKey(
        'account_management.ProvenanceSystemSettingsAccountManagementSubscriber', verbose_name='用户',
        on_delete=models.CASCADE, null=True, blank=True, to_field='ID', clearable=True, placeholder='用户', )
    ID_SUBSCRIBER_GROUP = fields.ForeignKey(
        'account_management.ProvenanceSystemSettingsAccountManagementSubscriberGroup', verbose_name='用户组',
        on_delete=models.CASCADE, null=True, blank=True, to_field='id', clearable=True, placeholder='用户组', )
    ID_ROLE = fields.ForeignKey(
        'account_management.ProvenanceSystemSettingsAccountManagementRole', verbose_name='角色',
        on_delete=models.CASCADE, null=True, blank=True, to_field='id', clearable=True, placeholder='角色', )

    # ID_ROLE_GROUP = fields.ForeignKey(
    #     'account_management.ProvenanceSystemSettingsAccountManagementRoleSubscriberGroup', verbose_name='角色',
    #     on_delete=models.CASCADE, null=True, blank=True, to_field='id', clearable=True, placeholder='角色', )

    class Meta:
        db_table = "ProvenanceSystemSettingsAccountManagementPermissionResults"
        ordering = ['-CREATE_TIME']
        verbose_name = "权限结果"
        verbose_name_plural = verbose_name
        unique_together = ('ID_AUTHORITY', 'ID_SUBSCRIBER', 'ID_SUBSCRIBER_GROUP', 'ID_ROLE')

    def __str__(self):
        return f'{self.ID_AUTHORITY}{self.ID_SUBSCRIBER}{self.ID_SUBSCRIBER_GROUP}{self.ID_ROLE}'
