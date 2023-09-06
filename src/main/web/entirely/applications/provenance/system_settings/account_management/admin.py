from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from import_export import resources

from account_management.models import (
    ProvenanceSystemSettingsAccountManagementSuper,
    ProvenanceSystemSettingsAccountManagementSubscriber,
    ProvenanceSystemSettingsAccountManagementSubscriberLand,
    ProvenanceSystemSettingsAccountManagementSubscriberGroup,
    ProvenanceSystemSettingsAccountManagementRole,
    ProvenanceSystemSettingsAccountManagementAuthority,
    ProvenanceSystemSettingsAccountManagementPermissionResults,
    ProvenanceSystemSettingsAccountManagementSubscriberGroupAccount,
    ProvenanceSystemSettingsAccountManagementRoleSubscriber,
    ProvenanceSystemSettingsAccountManagementRoleSubscriberGroup,
    ProvenanceSystemSettingsAccountManagementPermissionMenuDisplay
)
from docs.utils.admin_communal.admin_filter_obj import ProvenanceSystemSettingsAccountManagementSubscriberLandAdminCode, \
    ProvenanceSystemSettingsAccountManagementAuthorityAdminCode


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = ProvenanceSystemSettingsAccountManagementSuper
        fields = ('email', 'mobile',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin 's
    disabled password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = ProvenanceSystemSettingsAccountManagementSuper
        fields = ('email', 'password', 'mobile', 'username', 'is_active', 'is_superuser')


class ProvenanceSystemSettingsAccountManagementSuperAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm
    # change_password_form = AdminPasswordChangeForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('username', 'mobile', 'email', 'is_superuser', 'is_staff', 'is_active',)
    search_fields = ('username', 'mobile', 'email',)
    list_filter = ('is_superuser', 'is_staff', 'is_active',)
    list_per_page = 10
    fieldsets = (
        (None, {'fields': ('email', 'password', 'mobile',)}),
        ('Personal info', {'fields': ('username',)}),
        ('Permissions', {'fields': ('is_superuser',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'mobile', 'password1', 'password2'),
        }),
    )
    # ordering = ('email',)
    filter_horizontal = ()


admin.site.register(ProvenanceSystemSettingsAccountManagementSuper, ProvenanceSystemSettingsAccountManagementSuperAdmin)


@admin.register(ProvenanceSystemSettingsAccountManagementSubscriber)
class ProvenanceSystemSettingsAccountManagementSubscriberAdmin(admin.ModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = ProvenanceSystemSettingsAccountManagementSubscriber

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = ('NAME', 'PASSWORD',)
    search_fields = ('NAME', 'PASSWORD',)
    list_per_page = 10


@admin.register(ProvenanceSystemSettingsAccountManagementSubscriberLand)
class ProvenanceSystemSettingsAccountManagementSubscriberLandAdmin(admin.ModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = ProvenanceSystemSettingsAccountManagementSubscriberLand

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = ('ID_SUBSCRIBER', 'UNIQUE_NUMBER', 'CODE')
    search_fields = ('UNIQUE_NUMBER',)
    list_filter = ('ID_SUBSCRIBER', ProvenanceSystemSettingsAccountManagementSubscriberLandAdminCode,)
    list_per_page = 10


@admin.register(ProvenanceSystemSettingsAccountManagementSubscriberGroup)
class ProvenanceSystemSettingsAccountManagementSubscriberGroupAdmin(admin.ModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = ProvenanceSystemSettingsAccountManagementSubscriberGroup

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = ('NAME', 'ID_PARENT',)
    search_fields = ('NAME', 'DETAIL',)
    list_filter = ('ID_PARENT',)
    list_filter_tree = ('ID_PARENT',)
    list_per_page = 10

    # list_display_tree_cascade = 'ID_ASTRO_PARENT'
    # list_display_tree_expand_all = True  # 展开状态，默认不展开
    def get_list_filter_tree(self, request):
        return self.list_filter_tree

    def get_list_filter_tree_queryset(self, request, field_name):
        if field_name == 'ID_PARENT':
            return self.get_queryset(request)


@admin.register(ProvenanceSystemSettingsAccountManagementSubscriberGroupAccount)
class ProvenanceSystemSettingsAccountManagementSubscriberGroupAccountAdmin(admin.ModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = ProvenanceSystemSettingsAccountManagementSubscriberGroupAccount

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = ('ID_SUBSCRIBER', 'ID_SUBSCRIBER_GROUP',)
    list_filter = ('ID_SUBSCRIBER', 'ID_SUBSCRIBER_GROUP',)
    list_per_page = 10


@admin.register(ProvenanceSystemSettingsAccountManagementRole)
class ProvenanceSystemSettingsAccountManagementRoleAdmin(admin.ModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = ProvenanceSystemSettingsAccountManagementRole

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = ('NAME', 'ID_PARENT',)
    search_fields = ('NAME',)
    list_filter = ('ID_PARENT',)
    list_filter_tree = ('ID_PARENT',)
    list_per_page = 10

    # list_display_tree_cascade = 'ID_ASTRO_PARENT'
    # list_display_tree_expand_all = True  # 展开状态，默认不展开
    def get_list_filter_tree(self, request):
        return self.list_filter_tree

    def get_list_filter_tree_queryset(self, request, field_name):
        if field_name == 'ID_PARENT':
            return self.get_queryset(request)


@admin.register(ProvenanceSystemSettingsAccountManagementRoleSubscriber)
class ProvenanceSystemSettingsAccountManagementRoleSubscriberAdmin(admin.ModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = ProvenanceSystemSettingsAccountManagementRoleSubscriber

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = ('ID_ROLE', 'ID_SUBSCRIBER',)
    list_filter = ('ID_ROLE', 'ID_SUBSCRIBER',)
    list_per_page = 10


@admin.register(ProvenanceSystemSettingsAccountManagementRoleSubscriberGroup)
class ProvenanceSystemSettingsAccountManagementRoleSubscriberGroupAdmin(admin.ModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = ProvenanceSystemSettingsAccountManagementRoleSubscriberGroup

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = ('ID_ROLE', 'ID_SUBSCRIBER_GROUP',)
    list_filter = ('ID_ROLE', 'ID_SUBSCRIBER_GROUP',)
    list_per_page = 10


@admin.register(ProvenanceSystemSettingsAccountManagementAuthority)
class ProvenanceSystemSettingsAccountManagementAuthorityAdmin(admin.ModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = ProvenanceSystemSettingsAccountManagementAuthority

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = ('NAME', 'CODE', 'ID_PARENT',)
    list_filter = ('ID_PARENT', ProvenanceSystemSettingsAccountManagementAuthorityAdminCode,)
    list_filter_tree = ('ID_PARENT',)
    list_per_page = 10

    # list_display_tree_cascade = 'ID_ASTRO_PARENT'
    # list_display_tree_expand_all = True  # 展开状态，默认不展开
    def get_list_filter_tree(self, request):
        return self.list_filter_tree

    def get_list_filter_tree_queryset(self, request, field_name):
        if field_name == 'ID_PARENT':
            return self.get_queryset(request)


@admin.register(ProvenanceSystemSettingsAccountManagementPermissionResults)
class ProvenanceSystemSettingsAccountManagementPermissionResultsAdmin(admin.ModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = ProvenanceSystemSettingsAccountManagementPermissionResults

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = ('ID_AUTHORITY', 'ID_SUBSCRIBER', 'ID_SUBSCRIBER_GROUP', 'ID_ROLE')
    list_filter = ('ID_AUTHORITY', 'ID_SUBSCRIBER', 'ID_SUBSCRIBER_GROUP', 'ID_ROLE')
    list_per_page = 10


@admin.register(ProvenanceSystemSettingsAccountManagementPermissionMenuDisplay)
class ProvenanceSystemSettingsAccountManagementPermissionMenuDisplayAdmin(admin.ModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = ProvenanceSystemSettingsAccountManagementPermissionMenuDisplay

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = ('ID_DISPLAY', 'ID_AUTHORITY',)
    list_filter = ('ID_DISPLAY', 'ID_AUTHORITY',)
    list_per_page = 10
