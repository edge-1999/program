from django.contrib import admin
from import_export import resources

from standard_encoding.models import (
    ProvenanceSystemSettingsStandardEncoding,
    ProvenanceSystemSettingsStandardCodeMain,
    ProvenanceSystemSettingsStandardCodeMainDict,
    ProvenanceSystemSettingsStandardContent
)


@admin.register(ProvenanceSystemSettingsStandardEncoding)
class ProvenanceSystemSettingsStandardEncodingAdmin(admin.ModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = ProvenanceSystemSettingsStandardEncoding

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = ('NAME_CHINESE', 'NAME_ENGLISH', 'ENCODING', 'ID_PARENT', 'STATUS_IS_ENABLE')
    search_fields = ('NAME_CHINESE', 'NAME_ENGLISH', 'ENCODING',)
    list_filter = ('ID_PARENT', 'STATUS_IS_ENABLE',)
    list_filter_tree = ('ID_PARENT',)
    list_per_page = 10

    # list_display_tree_cascade = 'ID_ASTRO_PARENT'
    # list_display_tree_expand_all = True  # 展开状态，默认不展开
    def get_list_filter_tree(self, request):
        return self.list_filter_tree

    def get_list_filter_tree_queryset(self, request, field_name):
        if field_name == 'ID_PARENT':
            return self.get_queryset(request)


@admin.register(ProvenanceSystemSettingsStandardCodeMain)
class ProvenanceSystemSettingsStandardCodeMainAdmin(admin.ModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = ProvenanceSystemSettingsStandardCodeMain

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = ('DESCRIBE', 'TECHNOLOGY',)
    search_fields = ('DESCRIBE', 'TECHNOLOGY',)
    list_per_page = 10


@admin.register(ProvenanceSystemSettingsStandardCodeMainDict)
class ProvenanceSystemSettingsStandardCodeMainDictAdmin(admin.ModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = ProvenanceSystemSettingsStandardCodeMainDict

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = ('CODE_MAIN', 'TECHNOLOGY', 'ABBREVIATION',)
    search_fields = ('TECHNOLOGY', 'ABBREVIATION',)
    list_filter = ('CODE_MAIN',)
    list_per_page = 10


@admin.register(ProvenanceSystemSettingsStandardContent)
class ProvenanceSystemSettingsStandardContentAdmin(admin.ModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = ProvenanceSystemSettingsStandardContent

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = ('DESCRIBE', 'TECHNOLOGY',)
    search_fields = ('DESCRIBE', 'TECHNOLOGY',)
    list_per_page = 10
