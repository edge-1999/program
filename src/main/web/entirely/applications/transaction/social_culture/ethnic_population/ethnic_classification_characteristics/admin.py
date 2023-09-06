from django.contrib import admin
from import_export import resources

from ethnic_classification_characteristics.models import (
    TransactionSocialCultureEthnicPopulationEthnicClassificationCharacteristicsBrief
)


@admin.register(TransactionSocialCultureEthnicPopulationEthnicClassificationCharacteristicsBrief)
class TransactionSocialCultureEthnicPopulationEthnicClassificationCharacteristicsBriefAdmin(admin.ModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = TransactionSocialCultureEthnicPopulationEthnicClassificationCharacteristicsBrief

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = ('NAME', 'STATUS_IS_EFFECTIVE',)
    search_fields = ('NAME', 'DETAIL',)
    list_filter = ('STATUS_IS_EFFECTIVE',)
    list_per_page = 10
