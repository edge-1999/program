from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin

from district.models import TransactionGeographyPoliticsDistrictBasic
from docs.utils.admin_communal.admin_filter_obj import TransactionGeographyPoliticsDistrictType


@admin.register(TransactionGeographyPoliticsDistrictBasic)
class MainResourcePlaceAdmin(ImportExportActionModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = TransactionGeographyPoliticsDistrictBasic

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = ('TYPE_TOWN', 'NAME_CHINESE', 'NAME_ENGLISH', 'ID_SUBORDINATE', 'ID_PARENT',)
    search_fields = ('NAME_CHINESE', 'ID_SUBORDINATE', 'NAME_ENGLISH',)
    list_filter = ('ID_NATION', 'ID_PARENT', TransactionGeographyPoliticsDistrictType)
    list_filter_tree = ('ID_PARENT',)

    list_per_page = 10

    def get_list_filter_tree(self, request):
        return self.list_filter_tree

    def get_list_filter_tree_queryset(self, request, field_name):
        if field_name == 'ID_PARENT':
            return self.get_queryset(request)
