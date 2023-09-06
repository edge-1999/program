from django.contrib import admin
from import_export import resources
from django.utils.html import format_html

from docs.utils.admin_communal.admin_filter_obj import (
    TransactionSocialCultureEthnicPopulationPersonalInformationPersonAdminSex,
    TransactionSocialCultureEthnicPopulationPersonalInformationPersonBirthdayAdminBirthday,
    TransactionSocialCultureEthnicPopulationPersonalInformationPersonAddressAdminAddress,
    TransactionSocialCultureEthnicPopulationPersonalInformationPersonEventAdminEvent,
    TransactionSocialCultureEthnicPopulationPersonalInformationPersonCertificateCode
)
from personal_Information.models import (
    TransactionSocialCultureEthnicPopulationPersonalInformationPerson,
    TransactionSocialCultureEthnicPopulationPersonalInformationPersonCountry,
    TransactionSocialCultureEthnicPopulationPersonalInformationPersonBirthday,
    TransactionSocialCultureEthnicPopulationPersonalInformationPersonAddress,
    TransactionSocialCultureEthnicPopulationPersonalInformationPersonEvent,
    TransactionSocialCultureEthnicPopulationPersonalInformationPersonNation,
    TransactionSocialCultureEthnicPopulationPersonalInformationPersonConnections,
    TransactionSocialCultureEthnicPopulationPersonalInformationPersonCertificate
)


@admin.register(TransactionSocialCultureEthnicPopulationPersonalInformationPerson)
class TransactionSocialCultureEthnicPopulationPersonalInformationPersonAdmin(admin.ModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = TransactionSocialCultureEthnicPopulationPersonalInformationPerson

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = ('SURNAME', 'NAME', 'SEX', 'DATE_OF_DEATH',)
    search_fields = ('NAME', 'NATION',)
    list_filter = (TransactionSocialCultureEthnicPopulationPersonalInformationPersonAdminSex,)
    list_per_page = 10


@admin.register(TransactionSocialCultureEthnicPopulationPersonalInformationPersonCountry)
class TransactionSocialCultureEthnicPopulationPersonalInformationPersonCountryAdmin(admin.ModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = TransactionSocialCultureEthnicPopulationPersonalInformationPersonCountry

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = ('ID_PERSON', 'ID_NATION', 'DATE_OF_DEATH',)
    list_filter = ('ID_PERSON', 'ID_NATION', 'DATE_OF_DEATH')
    list_per_page = 10


@admin.register(TransactionSocialCultureEthnicPopulationPersonalInformationPersonBirthday)
class TransactionSocialCultureEthnicPopulationPersonalInformationPersonBirthdayAdmin(admin.ModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = TransactionSocialCultureEthnicPopulationPersonalInformationPersonBirthday

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = ('ID_PERSON', 'TYPE_BIRTHDAY', 'DATE_START', 'user_date_time',)
    list_filter = (
        'ID_PERSON', TransactionSocialCultureEthnicPopulationPersonalInformationPersonBirthdayAdminBirthday,
        'STATUS_IS_EFFECTIVE',

    )
    list_per_page = 10

    def user_date_time(self, obj):
        import time
        import datetime

        from borax.calendars.lunardate import LunarDate

        user_datetime = obj.DATE_START
        type_b = obj.TYPE_BIRTHDAY
        status = obj.STATUS_IS_DELETE
        if user_datetime is None or type_b is None or str(status) == 'True':
            return format_html('<span>{}</span>')

        g_year = time.strftime("%Y")
        g_date = time.strftime("%m%d")
        yl_date = LunarDate.from_solar_date(int(g_year), int(time.strftime("%m")), int(time.strftime("%d")))
        y_date = yl_date.strftime("%A%B")

        if str(type_b) == '公历' and str(user_datetime) > g_date:
            db_date = str(g_year) + '-' + str(user_datetime[:2]) + '-' + str(user_datetime[2:])
        elif str(type_b) == '公历' and str(user_datetime) <= g_date:
            db_date = str(int(g_year) + 1) + '-' + str(user_datetime[:2]) + '-' + str(user_datetime[2:])
        elif str(type_b) == '阴历' and str(user_datetime) > y_date:
            db_date = str(LunarDate(
                yl_date.year, int(str(user_datetime[:2])), int(str(user_datetime[2:]))).to_solar_date())
        elif str(type_b) == '阴历' and str(user_datetime) <= y_date:
            db_date = str(LunarDate(
                yl_date.year + 1, int(str(user_datetime[:2])), int(str(user_datetime[2:]))).to_solar_date())
        else:
            return format_html('<span>{}</span>')

        birthday_date = datetime.datetime.strptime(db_date, "%Y-%m-%d")
        curr_datetime = datetime.datetime.now()
        minus_date = birthday_date - curr_datetime
        if minus_date.days < 30:
            return format_html(f'<span style="color:red">{db_date}</span>')
        elif str(birthday_date.year) == str(g_year):
            return format_html(f'<span style="color:blue">{db_date}</span>')
        else:
            return format_html(f'<span>{db_date}</span>')

    user_date_time.short_description = '公历生日'
    user_date_time.admin_order_field = 'birthday'


@admin.register(TransactionSocialCultureEthnicPopulationPersonalInformationPersonAddress)
class TransactionSocialCultureEthnicPopulationPersonalInformationPersonAddressAdmin(admin.ModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = TransactionSocialCultureEthnicPopulationPersonalInformationPersonAddress

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = ('ID_PERSON', 'TYPE_ADDRESS', 'ADDRESS_TXT', 'STATUS_IS_EFFECTIVE',)
    search_fields = ('ADDRESS_TXT',)
    list_filter = (
        'ID_PERSON', TransactionSocialCultureEthnicPopulationPersonalInformationPersonAddressAdminAddress,
        'STATUS_IS_EFFECTIVE')
    list_per_page = 10


@admin.register(TransactionSocialCultureEthnicPopulationPersonalInformationPersonEvent)
class TransactionSocialCultureEthnicPopulationPersonalInformationPersonEventAdmin(admin.ModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = TransactionSocialCultureEthnicPopulationPersonalInformationPersonEvent

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = ('ID_PERSON', 'DATE', 'RTYPE_EVENT',)
    search_fields = ('DETAIL',)
    list_filter = (
        'ID_PERSON', 'DATE', TransactionSocialCultureEthnicPopulationPersonalInformationPersonEventAdminEvent)
    list_per_page = 10


@admin.register(TransactionSocialCultureEthnicPopulationPersonalInformationPersonNation)
class TransactionSocialCultureEthnicPopulationPersonalInformationPersonEventAdmin(admin.ModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = TransactionSocialCultureEthnicPopulationPersonalInformationPersonNation

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = ('ID_PERSON', 'ID_NATION', 'STATUS_IS_EFFECTIVE',)
    list_filter = ('ID_PERSON', 'ID_NATION', 'STATUS_IS_EFFECTIVE')
    list_per_page = 10


@admin.register(TransactionSocialCultureEthnicPopulationPersonalInformationPersonConnections)
class TransactionSocialCultureEthnicPopulationPersonalInformationPersonConnectionsAdmin(admin.ModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = TransactionSocialCultureEthnicPopulationPersonalInformationPersonConnections

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = ('ID_PERSON', 'ID_PRODUCTS', 'NUMBER',)
    search_fields = ('NUMBER',)
    list_filter = ('ID_PERSON', 'ID_PRODUCTS',)
    list_per_page = 10


@admin.register(TransactionSocialCultureEthnicPopulationPersonalInformationPersonCertificate)
class TransactionSocialCultureEthnicPopulationPersonalInformationPersonCertificateAdmin(admin.ModelAdmin):
    class AdminProxyResource(resources.ModelResource):
        class Meta:
            model = TransactionSocialCultureEthnicPopulationPersonalInformationPersonCertificate

    resource_class = AdminProxyResource
    actions = ('custom_btn',)
    list_display = ('ID_PERSON', 'CODE', 'NUMBER', 'ID_ORGANIZATIONS',)
    search_fields = ('NUMBER',)
    list_filter = (
        'ID_PERSON', TransactionSocialCultureEthnicPopulationPersonalInformationPersonCertificateCode,
        'ID_ORGANIZATIONS',)
    list_per_page = 10
