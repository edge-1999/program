from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin

from country.models import TransactionGeographyPoliticsCountryCollect, TransactionGeographyPoliticsCountryCurrency


@admin.register(TransactionGeographyPoliticsCountryCollect)
class MainResourceUserBasesAdmin(ImportExportActionModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = TransactionGeographyPoliticsCountryCollect

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = (
        'NAME_CHINA', 'NAME_ENGLISH', 'TWO_CHARACTER_CODE', 'THREE_CHARACTER_CODE', 'NUMERIC_CODE',)
    search_fields = ('NAME_CHINA', 'NAME_ENGLISH',)
    list_filter = ('STATUS_IS_DELETE', 'STATUS_IS_EFFECTIVE',)
    list_per_page = 10


@admin.register(TransactionGeographyPoliticsCountryCurrency)
class MainResourceUserBasesAdmin(admin.ModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = TransactionGeographyPoliticsCountryCurrency

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = (
        'ID_NATION', 'COUNTRY_DESCRIBE_CHINESE', 'COUNTRY_DESCRIBE_ENGLISH', 'COUNTRY_NOTATION',
        'COUNTRY_ISO_CODE', 'COUNTRY_AUXILIARY_UNIT', 'COUNTRY_CARRY_SYSTEM',)
    search_fields = ('COUNTRY_DESCRIBE_CHINESE', 'COUNTRY_DESCRIBE_ENGLISH',)
    list_filter = ('ID_NATION', 'STATUS_IS_DELETE', 'STATUS_IS_EFFECTIVE',)
    list_per_page = 10
