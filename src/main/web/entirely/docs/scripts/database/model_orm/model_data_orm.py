from django.db import transaction

from django.db.models import Max, Min, Sum, Count, Avg
from django.db.models import Q, F

from standard_encoding.models import ProvenanceSystemSettingsStandardContent


def select_db():
    print('MySQL DataBase Start Query')

    data = ProvenanceSystemSettingsStandardContent.objects.filter(
        TECHNOLOGY='EthnicClassificationCharacteristicsBrief', DESCRIBE='民族分类与特征'
    ).values('DETAIL')
    print(data[0]['DETAIL'])
    try:
        with transaction.atomic():
            print('数据库操作正常')
            # raise Exception()
            # print('数据库操作异常')
    except:
        transaction.rollback()


class ModelDb:

    # @transaction.atomic
    def select_db_model(self):
        """查看数据"""

        try:
            with transaction.atomic():
                print('数据库操作正常')
                # raise Exception()
                # print('数据库操作异常')
        except:
            transaction.rollback()
