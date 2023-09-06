from django.contrib import admin
from import_export import resources

from daily_records.models import ProvenanceSystemFunctionDailyRecordsEvent, \
    ProvenanceSystemFunctionDailyRecordsEventType, ProvenanceSystemFunctionDailyRecordsDiary
from docs.utils.admin_communal.admin_filter_obj import ProvenanceSystemFunctionDailyRecordsEventIdentity, \
    ProvenanceSystemFunctionDailyRecordsEventTypeCode


@admin.register(ProvenanceSystemFunctionDailyRecordsEvent)
class ProvenanceSystemFunctionDailyRecordsEventAdmin(admin.ModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = ProvenanceSystemFunctionDailyRecordsEvent

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = ('ID_PERSON', 'DATE', 'IDENTITY', 'NAME',)
    search_fields = ('NAME', 'DETAIL',)
    list_filter = ('ID_PERSON', 'DATE', ProvenanceSystemFunctionDailyRecordsEventIdentity,)
    list_per_page = 10


@admin.register(ProvenanceSystemFunctionDailyRecordsEventType)
class ProvenanceSystemFunctionDailyRecordsEventTypeAdmin(admin.ModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = ProvenanceSystemFunctionDailyRecordsEventType

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = ('ID_EVENT', 'CODE',)
    list_filter = ('ID_EVENT', ProvenanceSystemFunctionDailyRecordsEventTypeCode,)
    list_per_page = 10


@admin.register(ProvenanceSystemFunctionDailyRecordsDiary)
class ProvenanceSystemFunctionDailyRecordsDiaryAdmin(admin.ModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = ProvenanceSystemFunctionDailyRecordsDiary

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = ('ID_PERSON', 'DATE',)
    search_fields = ('DETAIL',)
    list_filter = ('ID_PERSON', 'DATE',)
    list_per_page = 10
