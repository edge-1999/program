from django.contrib import admin
from import_export import resources

from biology.models import LearningNaturalScienceBiologicalSpecies
from docs.utils.admin_communal.admin_filter_obj import PermissionControlDataLearningNaturalScienceAstronomyCosmologyCode


@admin.register(LearningNaturalScienceBiologicalSpecies)
class MainResourceAccountAuthorChangeAdmin(admin.ModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = LearningNaturalScienceBiologicalSpecies

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = ('NAME_REFERRED_TO_AS', 'NAME_CHINESE', 'NAME_ENGLISH', 'ID_PARENT')
    search_fields = ('NAME_CHINESE', 'NAME_ENGLISH', 'NAME_REFERRED_TO_AS',)
    list_filter = (
        'ID_PARENT', PermissionControlDataLearningNaturalScienceAstronomyCosmologyCode, 'STATUS_IS_EXTINCTION',
        'STATUS_IS_DELETE', 'STATUS_IS_EFFECTIVE',)
    list_filter_tree = ('ID_PARENT',)
    list_per_page = 10

    def get_list_filter_tree(self, request):
        return self.list_filter_tree

    def get_list_filter_tree_queryset(self, request, field_name):
        if field_name == 'ID_PARENT':
            return self.get_queryset(request)
