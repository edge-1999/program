from django.contrib import admin
from import_export import resources

from docs.utils.admin_communal.admin_filter_obj import (
    TransactionEconomyIndustryOrganizationsBasesAdminEnterprise, TransactionEconomyIndustryOrganizationsCallAdminCode,
    TransactionEconomyIndustryOrganizationsAddressAdminCode, TransactionEconomyIndustryOrganizationsCertificateCode
)
from organizations.models import (
    TransactionEconomyIndustryOrganizationsBases, TransactionEconomyIndustryOrganizationsCall,
    TransactionEconomyIndustryOrganizationsAddress, TransactionEconomyIndustryOrganizationsDetails,
    TransactionEconomyIndustryOrganizationsCertificate, TransactionEconomyIndustryOrganizationsContact
)


@admin.register(TransactionEconomyIndustryOrganizationsBases)
class TransactionEconomyIndustryOrganizationsBasesAdmin(admin.ModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = TransactionEconomyIndustryOrganizationsBases

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = ('ENTERPRISE_NAME', 'ENTERPRISE_CODE', 'COUNTRY_CREATE_TIME',)
    search_fields = ('ENTERPRISE_NAME',)
    list_filter = (TransactionEconomyIndustryOrganizationsBasesAdminEnterprise, 'COUNTRY_CREATE_TIME',)
    list_per_page = 10


@admin.register(TransactionEconomyIndustryOrganizationsCall)
class TransactionEconomyIndustryOrganizationsCallAdmin(admin.ModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = TransactionEconomyIndustryOrganizationsCall

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = ('ID_ORGANIZATIONS', 'ENTERPRISE_NAME_CODE', 'ENTERPRISE_NAME',)
    search_fields = ('ENTERPRISE_NAME',)
    list_filter = ('ID_ORGANIZATIONS', TransactionEconomyIndustryOrganizationsCallAdminCode,)
    list_per_page = 10


@admin.register(TransactionEconomyIndustryOrganizationsAddress)
class TransactionEconomyIndustryOrganizationsAddressAdmin(admin.ModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = TransactionEconomyIndustryOrganizationsAddress

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = ('ID_ORGANIZATIONS', 'ENTERPRISE_ADDRESS_CODE', 'ENTERPRISE_ADDRESS_NAME',)
    search_fields = ('ENTERPRISE_ADDRESS_NAME',)
    list_filter = ('ID_ORGANIZATIONS', TransactionEconomyIndustryOrganizationsAddressAdminCode,)
    list_per_page = 10


@admin.register(TransactionEconomyIndustryOrganizationsDetails)
class TransactionEconomyIndustryOrganizationsDetailsAdmin(admin.ModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = TransactionEconomyIndustryOrganizationsDetails

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = ('ID_ORGANIZATIONS', 'DETAIL',)
    search_fields = ('DETAIL',)
    list_filter = ('ID_ORGANIZATIONS',)
    list_per_page = 10


@admin.register(TransactionEconomyIndustryOrganizationsCertificate)
class TransactionEconomyIndustryOrganizationsCertificateAdmin(admin.ModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = TransactionEconomyIndustryOrganizationsCertificate

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = ('ID_ORGANIZATIONS', 'CODE', 'NUMBER', 'DATE_START',)
    search_fields = ('NUMBER',)
    list_filter = ('ID_ORGANIZATIONS', TransactionEconomyIndustryOrganizationsCertificateCode,)
    list_per_page = 10


@admin.register(TransactionEconomyIndustryOrganizationsContact)
class TransactionEconomyIndustryOrganizationsContactAdmin(admin.ModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = TransactionEconomyIndustryOrganizationsContact

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = ('ID_ORGANIZATIONS', 'ID_PRODUCTS', 'NUMBER',)
    search_fields = ('NUMBER',)
    list_filter = ('ID_ORGANIZATIONS', 'ID_PRODUCTS',)
    list_per_page = 10
