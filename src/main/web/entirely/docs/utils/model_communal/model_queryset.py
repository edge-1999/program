from standard_encoding.models import ProvenanceSystemSettingsStandardCodeMainDict


def get_queryset_function_authority_type_data():
    """权限控制-数据"""
    return ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(CODE_MAIN='PermissionControlData')


def get_queryset_function_permission_control_menu():
    """权限控制-操作"""
    return ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(CODE_MAIN='PermissionControlMenu')


def get_queryset_function_person_sex_physiological():
    """人类生理性别"""
    return ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(CODE_MAIN='HumanPhysiologicalGender')


def get_queryset_function_calendar():
    """日历"""
    return ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(CODE_MAIN='Calendar')


def get_queryset_function_personal_address():
    """个人地址"""
    return ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(CODE_MAIN='PersonalAddress')


def get_queryset_function_personal_event():
    """人员事件"""
    return ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(CODE_MAIN='PersonalEvent')


def get_queryset_function_organization_category():
    """组织类别"""
    return ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(CODE_MAIN='OrganizationCategory')


def get_queryset_function_organization_category_code():
    """组织称呼类型"""
    return ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(CODE_MAIN='OrganizationCategoryCode')


def get_queryset_function_organization_address_code():
    """组织地址类型"""
    return ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(CODE_MAIN='OrganizationAddressCode')


def get_queryset_function_organization_certificate_code():
    """组织证件类别"""
    return ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(CODE_MAIN='OrganizationsCertificateCode')


def get_queryset_function_person_certificate_code():
    """个人证件类别"""
    return ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(CODE_MAIN='PersonCertificateCode')


def get_queryset_function_products_type():
    """产品类型"""
    return ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(CODE_MAIN='ProductsType')


def get_queryset_records_event_type():
    """事件类型"""
    return ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(CODE_MAIN='RecordsEventType')


def get_queryset_records_event_identity():
    """事件参与身份"""
    return ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(CODE_MAIN='RecordsEventIdentity')


def get_queryset_password_correlation_code():
    """产品关联类别"""
    return ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(CODE_MAIN='PasswordCorrelationCode')


def get_queryset_politics_district_code():
    """城镇位置类别"""
    return ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(CODE_MAIN='PoliticsDistrictCode')


def get_queryset_account_management_subscriber_land():
    """关联登陆"""
    return ProvenanceSystemSettingsStandardCodeMainDict.objects.filter(CODE_MAIN='SubscriberLandCode')
