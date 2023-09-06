from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from standard_encoding.models import ProvenanceSystemSettingsStandardCodeMainDict


class TransactionGeographyPoliticsDistrictType(admin.SimpleListFilter):
    title = _('城镇分类')
    parameter_name = 'TransactionGeographyPoliticsDistrictType'

    def lookups(self, request, model_admin):
        return tuple(
            [(i['id'], _(i["ABBREVIATION"])) for i in ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(
                CODE_MAIN__TECHNOLOGY='PoliticsDistrictType').values("id", "ABBREVIATION")])

    def queryset(self, request, queryset):
        return queryset.filter(TYPE_TOWN=self.value())


class PermissionControlDataLearningNaturalScienceAstronomyCosmologyCode(admin.SimpleListFilter):
    title = _('权限控制-数据')
    parameter_name = 'PermissionControlDataLearningNaturalScienceAstronomyCosmologyCode'

    def lookups(self, request, model_admin):
        return tuple(
            [(i['id'], _(i["ABBREVIATION"])) for i in ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(
                CODE_MAIN__TECHNOLOGY='PermissionControlData').values("id", "ABBREVIATION")])

    def queryset(self, request, queryset):
        # 字段
        return queryset.filter(STATUS_AUTHORITY=self.value())


class ProvenanceSystemSettingsAccountManagementAuthorityAdminCode(admin.SimpleListFilter):
    title = _('权限控制-操作')
    parameter_name = 'ProvenanceSystemSettingsAccountManagementAuthorityAdminCode'

    def lookups(self, request, model_admin):
        return tuple(
            [(i['id'], _(i["ABBREVIATION"])) for i in ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(
                CODE_MAIN__TECHNOLOGY='PermissionControlMenu').values("id", "ABBREVIATION")])

    def queryset(self, request, queryset):
        # 字段
        return queryset.filter(CODE=self.value())


class TransactionSocialCultureEthnicPopulationPersonalInformationPersonAdminSex(admin.SimpleListFilter):
    title = _('生理性别')
    parameter_name = 'TransactionSocialCultureEthnicPopulationPersonalInformationPersonAdminSex'

    def lookups(self, request, model_admin):
        return tuple(
            [(i['id'], _(i["ABBREVIATION"])) for i in ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(
                CODE_MAIN__TECHNOLOGY='HumanPhysiologicalGender').values("id", "ABBREVIATION")])

    def queryset(self, request, queryset):
        # 字段
        return queryset.filter(SEX=self.value())


class TransactionSocialCultureEthnicPopulationPersonalInformationPersonBirthdayAdminBirthday(admin.SimpleListFilter):
    title = _('生日类别')
    parameter_name = 'TransactionSocialCultureEthnicPopulationPersonalInformationPersonAdminSex'

    def lookups(self, request, model_admin):
        return tuple(
            [(i['id'], _(i["ABBREVIATION"])) for i in ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(
                CODE_MAIN__TECHNOLOGY='Calendar').values("id", "ABBREVIATION")])

    def queryset(self, request, queryset):
        # 字段
        return queryset.filter(TYPE_BIRTHDAY=self.value())


class TransactionSocialCultureEthnicPopulationPersonalInformationPersonAddressAdminAddress(admin.SimpleListFilter):
    title = _('地址类别')
    parameter_name = 'TransactionSocialCultureEthnicPopulationPersonalInformationPersonAdminSex'

    def lookups(self, request, model_admin):
        return tuple(
            [(i['id'], _(i["ABBREVIATION"])) for i in ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(
                CODE_MAIN__TECHNOLOGY='PersonalAddress').values("id", "ABBREVIATION")])

    def queryset(self, request, queryset):
        # 字段
        return queryset.filter(TYPE_ADDRESS=self.value())


class TransactionSocialCultureEthnicPopulationPersonalInformationPersonEventAdminEvent(admin.SimpleListFilter):
    title = _('事件类型')
    parameter_name = 'TransactionSocialCultureEthnicPopulationPersonalInformationPersonAdminSex'

    def lookups(self, request, model_admin):
        return tuple(
            [(i['id'], _(i["ABBREVIATION"])) for i in ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(
                CODE_MAIN__TECHNOLOGY='PersonalEvent').values("id", "ABBREVIATION")])

    def queryset(self, request, queryset):
        # 字段
        return queryset.filter(RTYPE_EVENT=self.value())


class TransactionEconomyIndustryOrganizationsBasesAdminEnterprise(admin.SimpleListFilter):
    title = _('组织类别')
    parameter_name = 'TransactionEconomyIndustryOrganizationsBasesAdminEnterprise'

    def lookups(self, request, model_admin):
        return tuple(
            [(i['id'], _(i["ABBREVIATION"])) for i in ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(
                CODE_MAIN__TECHNOLOGY='OrganizationCategory').values("id", "ABBREVIATION")])

    def queryset(self, request, queryset):
        # 字段
        return queryset.filter(ENTERPRISE_CODE=self.value())


class TransactionEconomyIndustryOrganizationsCallAdminCode(admin.SimpleListFilter):
    title = _('组织称呼类型')
    parameter_name = 'TransactionEconomyIndustryOrganizationsCallAdminCode'

    def lookups(self, request, model_admin):
        return tuple(
            [(i['id'], _(i["ABBREVIATION"])) for i in ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(
                CODE_MAIN__TECHNOLOGY='OrganizationCategoryCode').values("id", "ABBREVIATION")])

    def queryset(self, request, queryset):
        # 字段
        return queryset.filter(ENTERPRISE_NAME_CODE=self.value())


class TransactionEconomyIndustryOrganizationsAddressAdminCode(admin.SimpleListFilter):
    title = _('组织称呼类型')
    parameter_name = 'TransactionEconomyIndustryOrganizationsAddressAdminCode'

    def lookups(self, request, model_admin):
        return tuple(
            [(i['id'], _(i["ABBREVIATION"])) for i in ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(
                CODE_MAIN__TECHNOLOGY='OrganizationAddressCode').values("id", "ABBREVIATION")])

    def queryset(self, request, queryset):
        # 字段
        return queryset.filter(ENTERPRISE_ADDRESS_CODE=self.value())


class TransactionEconomyIndustryProductsCallAddressAdminCode(admin.SimpleListFilter):
    title = _('产品称呼类型')
    parameter_name = 'TransactionEconomyIndustryProductsCallAddressAdminCode'

    def lookups(self, request, model_admin):
        return tuple(
            [(i['id'], _(i["ABBREVIATION"])) for i in ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(
                CODE_MAIN__TECHNOLOGY='OrganizationAddressCode').values("id", "ABBREVIATION")])

    def queryset(self, request, queryset):
        # 字段
        return queryset.filter(NAME_CODE=self.value())


class TransactionEconomyIndustryOrganizationsCertificateCode(admin.SimpleListFilter):
    title = _('组织证件信息')
    parameter_name = 'TransactionEconomyIndustryOrganizationsCertificateCode'

    def lookups(self, request, model_admin):
        return tuple(
            [(i['id'], _(i["ABBREVIATION"])) for i in ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(
                CODE_MAIN__TECHNOLOGY='OrganizationsCertificateCode').values("id", "ABBREVIATION")])

    def queryset(self, request, queryset):
        # 字段
        return queryset.filter(CODE=self.value())


class TransactionSocialCultureEthnicPopulationPersonalInformationPersonCertificateCode(admin.SimpleListFilter):
    title = _('个人证件信息')
    parameter_name = 'TransactionSocialCultureEthnicPopulationPersonalInformationPersonCertificateCode'

    def lookups(self, request, model_admin):
        return tuple(
            [(i['id'], _(i["ABBREVIATION"])) for i in ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(
                CODE_MAIN__TECHNOLOGY='PersonCertificateCode').values("id", "ABBREVIATION")])

    def queryset(self, request, queryset):
        # 字段
        return queryset.filter(CODE=self.value())


class TransactionEconomyIndustryProductsTypeType(admin.SimpleListFilter):
    title = _('产品类型')
    parameter_name = 'TransactionEconomyIndustryProductsTypeType'

    def lookups(self, request, model_admin):
        return tuple(
            [(i['id'], _(i["ABBREVIATION"])) for i in ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(
                CODE_MAIN__TECHNOLOGY='ProductsType').values("id", "ABBREVIATION")])

    def queryset(self, request, queryset):
        # 字段
        return queryset.filter(PRODUCTS_CODE=self.value())


class ProvenanceSystemFunctionDailyRecordsEventIdentity(admin.SimpleListFilter):
    title = _('事件参与身份')
    parameter_name = 'ProvenanceSystemFunctionDailyRecordsEventIdentity'

    def lookups(self, request, model_admin):
        return tuple(
            [(i['id'], _(i["ABBREVIATION"])) for i in ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(
                CODE_MAIN__TECHNOLOGY='RecordsEventIdentity').values("id", "ABBREVIATION")])

    def queryset(self, request, queryset):
        # 字段
        return queryset.filter(IDENTITY=self.value())


class ProvenanceSystemFunctionDailyRecordsEventTypeCode(admin.SimpleListFilter):
    title = _('事件类型')
    parameter_name = 'ProvenanceSystemFunctionDailyRecordsEventTypeCode'

    def lookups(self, request, model_admin):
        return tuple(
            [(i['id'], _(i["ABBREVIATION"])) for i in ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(
                CODE_MAIN__TECHNOLOGY='RecordsEventType').values("id", "ABBREVIATION")])

    def queryset(self, request, queryset):
        # 字段
        return queryset.filter(CODE=self.value())


class ProvenanceSystemFunctionPasswordRecordsAdminCode(admin.SimpleListFilter):
    title = _('产品关联类别')
    parameter_name = 'ProvenanceSystemFunctionPasswordRecordsAdminCode'

    def lookups(self, request, model_admin):
        return tuple(
            [(i['id'], _(i["ABBREVIATION"])) for i in ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(
                CODE_MAIN__TECHNOLOGY='PasswordCorrelationCode').values("id", "ABBREVIATION")])

    def queryset(self, request, queryset):
        # 字段
        return queryset.filter(CODE=self.value())


class ProvenanceSystemSettingsAccountManagementSubscriberLandAdminCode(admin.SimpleListFilter):
    title = _('关联登陆')
    parameter_name = 'ProvenanceSystemSettingsAccountManagementSubscriberLandAdminCode'

    def lookups(self, request, model_admin):
        return tuple(
            [(i['id'], _(i["ABBREVIATION"])) for i in ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(
                CODE_MAIN__TECHNOLOGY='SubscriberLandCode').values("id", "ABBREVIATION")])

    def queryset(self, request, queryset):
        # 字段
        return queryset.filter(CODE=self.value())
