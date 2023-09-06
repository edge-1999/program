import os
import sys

import django

# sys.path.insert(0, project)
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'entirely.settings')
django.setup()


def run_main():
    # from docs.scripts.database.model_orm.role_orm_model import MenuPermission
    # from docs.utils.middlewares_communal.subscriber_permission import SubscriberRoleMenu
    # from docs.scripts.database.model_orm.role_orm_model import MenuPermissionTreeNode, MenuPermissionTree
    from menu_management.models import ProvenanceSystemSettingsMenuManagementMenu
    from docs.scripts.database.subscriber_permission import SubscriberRoleMenu

    subscriber_id = 'dc2c1d98b9604f87a383f3e522ef53e2'
    # menu_id = '10'
    role_permission = SubscriberRoleMenu(subscriber_id)
    # role_permission.subscriber_id = subscriber_id
    # role_permission.menu_id = menu_id
    subscriber_permission = role_permission.run
    print(subscriber_permission)
    # a_ = MenuPermissionTree(subscriber_id, subscriber_permission.get(subscriber_id))
    # print(a_.dict)


if __name__ == '__main__':
    run_main()
