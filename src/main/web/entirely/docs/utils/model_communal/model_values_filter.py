from django.db import transaction

from standard_encoding.models import ProvenanceSystemSettingsStandardContent


def select_ethnic_classification_characteristics_brief():
    try:
        with transaction.atomic():
            return ProvenanceSystemSettingsStandardContent.objects.filter(
                TECHNOLOGY='EthnicClassificationCharacteristicsBrief', DESCRIBE='民族分类与特征'
            ).values('DETAIL')[0]['DETAIL']
    except Exception as e:
        return ''


def select_organizations_details():
    try:
        with transaction.atomic():
            return ProvenanceSystemSettingsStandardContent.objects.filter(
                TECHNOLOGY='OrganizationsDetails', DESCRIBE='组织详情描述'
            ).values('DETAIL')[0]['DETAIL']
    except Exception as e:
        return ''


def select_products_detail():
    try:
        with transaction.atomic():
            return ProvenanceSystemSettingsStandardContent.objects.filter(
                TECHNOLOGY='ProductsDetail', DESCRIBE='产品详情描述'
            ).values('DETAIL')[0]['DETAIL']
    except Exception as e:
        return ''


def select_event_details():
    try:
        with transaction.atomic():
            return ProvenanceSystemSettingsStandardContent.objects.filter(
                TECHNOLOGY='EventDetails', DESCRIBE='事件详情描述'
            ).values('DETAIL')[0]['DETAIL']
    except Exception as e:
        return ''


def select_event_diary():
    try:
        with transaction.atomic():
            return ProvenanceSystemSettingsStandardContent.objects.filter(
                TECHNOLOGY='EventDiary', DESCRIBE='日记详情描述'
            ).values('DETAIL')[0]['DETAIL']
    except Exception as e:
        return ''


def select_password_records():
    try:
        with transaction.atomic():
            return ProvenanceSystemSettingsStandardContent.objects.filter(
                TECHNOLOGY='PasswordRecords', DESCRIBE='密码详情描述'
            ).values('DETAIL')[0]['DETAIL']
    except Exception as e:
        return ''
