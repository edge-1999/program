from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin

from cosmology.models import LearningNaturalScienceAstronomyCosmologyCode
from docs.utils.admin_communal.admin_filter_obj import PermissionControlDataLearningNaturalScienceAstronomyCosmologyCode


@admin.register(LearningNaturalScienceAstronomyCosmologyCode)
class MainResourceAstroAdmin(ImportExportActionModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = LearningNaturalScienceAstronomyCosmologyCode

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = ('NAME', 'ID_PARENT', 'STATUS_IS_EFFECTIVE',)
    search_fields = ('NAME',)
    list_filter = (
        'ID_PARENT', PermissionControlDataLearningNaturalScienceAstronomyCosmologyCode,
        'STATUS_IS_EFFECTIVE', 'STATUS_IS_DELETE',)
    list_filter_tree = ('ID_PARENT',)

    def get_list_filter_tree(self, request):
        return self.list_filter_tree

    def get_list_filter_tree_queryset(self, request, field_name):
        if field_name == 'ID_PARENT':
            return self.get_queryset(request)
