from django.contrib import admin
from import_export import resources

from docs.utils.admin_communal.admin_filter_obj import ProvenanceSystemFunctionPasswordRecordsAdminCode
from password_records.models import ProvenanceSystemFunctionPasswordRecords, ProvenanceSystemFunctionPasswordCorrelation


@admin.register(ProvenanceSystemFunctionPasswordRecords)
class ProvenanceSystemFunctionPasswordRecordsAdmin(admin.ModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = ProvenanceSystemFunctionPasswordRecords

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = ('ID_PERSON', 'ID_PRODUCTS', 'NUMBER', 'PASSWORD',)
    search_fields = ('NUMBER', 'PASSWORD', 'DETAIL',)
    list_filter = ('ID_PERSON', 'ID_PRODUCTS',)
    list_per_page = 10


@admin.register(ProvenanceSystemFunctionPasswordCorrelation)
class ProvenanceSystemFunctionPasswordCorrelationAdmin(admin.ModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = ProvenanceSystemFunctionPasswordCorrelation

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = ('ID_PASSWORD', 'ID_PASSWORD_RELATION', 'CODE',)
    list_filter = ('ID_PASSWORD', 'ID_PASSWORD_RELATION', ProvenanceSystemFunctionPasswordRecordsAdminCode,)
    list_per_page = 10
