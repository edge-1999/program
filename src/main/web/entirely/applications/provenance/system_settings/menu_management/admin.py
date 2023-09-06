from django.contrib import admin
from import_export import resources

from menu_management.models import (
    ProvenanceSystemSettingsMenuManagementMenu,
    ProvenanceSystemSettingsMenuManagementMenuPermission,
    ProvenanceSystemSettingsMenuManagementMenuParameter,
    ProvenanceSystemSettingsMenuManagementMenuRoleDisplay
)


@admin.register(ProvenanceSystemSettingsMenuManagementMenu)
class ProvenanceSystemSettingsMenuManagementMenuAdmin(admin.ModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = ProvenanceSystemSettingsMenuManagementMenu

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


@admin.register(ProvenanceSystemSettingsMenuManagementMenuParameter)
class ProvenanceSystemSettingsMenuManagementMenuParameterAdmin(admin.ModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = ProvenanceSystemSettingsMenuManagementMenuParameter

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = ('ID_MENU', 'APP_URL_NAME', 'URL_NAME', 'ICON',)
    list_filter = ('ID_MENU',)
    search_fields = ('APP_URL_NAME', 'URL_NAME', 'ICON')
    list_per_page = 10


@admin.register(ProvenanceSystemSettingsMenuManagementMenuPermission)
class ProvenanceSystemSettingsMenuManagementMenuPermissionAdmin(admin.ModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = ProvenanceSystemSettingsMenuManagementMenuPermission

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = ('ID_MENU', 'ID_AUTHORITY',)
    list_filter = ('ID_MENU', 'ID_AUTHORITY',)
    list_per_page = 10


@admin.register(ProvenanceSystemSettingsMenuManagementMenuRoleDisplay)
class ProvenanceSystemSettingsMenuManagementMenuRoleDisplay(admin.ModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = ProvenanceSystemSettingsMenuManagementMenuRoleDisplay

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = ('ID_ROLE', 'ID_MENU',)
    list_filter = ('ID_ROLE', 'ID_MENU',)
    list_per_page = 10
