from account_management.models import (
    ProvenanceSystemSettingsAccountManagementSubscriberGroupAccount,
    ProvenanceSystemSettingsAccountManagementRoleSubscriber,
    ProvenanceSystemSettingsAccountManagementRoleSubscriberGroup,
    ProvenanceSystemSettingsAccountManagementPermissionResults,
    ProvenanceSystemSettingsAccountManagementAuthority,
    ProvenanceSystemSettingsAccountManagementRole,
    ProvenanceSystemSettingsAccountManagementSubscriberGroup, ProvenanceSystemSettingsAccountManagementSubscriber
)
from menu_management.models import (
    ProvenanceSystemSettingsMenuManagementMenu,
    ProvenanceSystemSettingsMenuManagementMenuPermission,
    ProvenanceSystemSettingsMenuManagementMenuRoleDisplay
)


class SubscriberPermission(object):
    def __init__(self):
        """
        思路：：一个用户自己本身所属的用户组，用户组是有上下级权限的，但是实际上，上级不会有下级的全部权限。角色同理
        """
        self.subscriber_id = None
        # self.menu_id = None
        self.group_id = None
        self.role_id = None
        self.permission_id = None
        self._subscriber_group = set()  # 用户组：用户所属的用户组
        self._subscriber_group_son = set()  # 用户组_下级：根据用户所属用户组，找到所有下级用户组
        self._role_subscriber = set()  # 用户_角色：用户拥有的角色
        self._role_son_subscriber = set()  # 用户_角色_下级：根据用户拥有的角色找到的下级角色
        self._role_subscriber_group = set()  # 用户组_角色：用户组拥有的角色
        self._role_son_subscriber_group = set()  # 用户组-角色-下级角色：用户组拥有的下级角色
        self._role_subscriber_group_son = set()  # 用户组_下级用户组_角色：所有的下级用户组，找到对应的角色
        self._role_son_subscriber_group_son = set()  # 用户组_下级用户组_角色_下级角色：所有的下级用户组角色的下级角色
        self._permission_subscriber = set()  # 用户对应的权限
        self._permission_subscriber_son = set()  # 用户对应权限的子权限
        self._permission_group = set()  # 用户组对应的权限
        self._permission_group_son = set()  # 用户组对应权限的子权限
        self._permission_role = set()  # 角色对应的权限
        self._permission_role_son = set()  # 角色对应权限的子权限
        self._permission_son = set()  # 所有权限的子权限

    @property
    def dict(self):
        return self.__dict__

    def _def_subscriber_role(self):
        """
        用户的角色
        :return:
        :rtype:
        """
        role_s = ProvenanceSystemSettingsAccountManagementRoleSubscriber.objects.filter(
            STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_SUBSCRIBER__ID=self.subscriber_id
        ).values('ID_ROLE')
        if role_s.exists():
            for role_id in role_s:
                self._role_subscriber.add(role_id["ID_ROLE"])

    def _def_subscriber_role_son(self, p_id):
        """
        当前所属用户角色的所有下级角色
        :return:
        :rtype:
        """
        group_id = ProvenanceSystemSettingsAccountManagementRole.objects.filter(
            STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PARENT=p_id
        ).values('id')
        if group_id.exists():
            for g_id in group_id:
                self._def_subscriber_role_son(g_id['id'])
                self._role_son_subscriber.add(g_id['id'])

    def _def_subscriber_group(self):
        """
        用户所属的用户组
        :return:
        :rtype:
        """
        subscriber_g = ProvenanceSystemSettingsAccountManagementSubscriberGroupAccount.objects.filter(
            STATUS_IS_DELETE='0', ID_SUBSCRIBER=self.subscriber_id, STATUS_IS_EFFECTIVE=1).values(
            'ID_SUBSCRIBER_GROUP')
        if subscriber_g.exists():
            for son_id in subscriber_g:
                self._subscriber_group.add(son_id["ID_SUBSCRIBER_GROUP"])

    def _def_subscriber_group_role(self):
        """
        用户组拥有的角色
        :return:
        :rtype:
        """
        for g_id in self._subscriber_group:
            role_group_id = ProvenanceSystemSettingsAccountManagementRoleSubscriberGroup.objects.filter(
                STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_SUBSCRIBER_GROUP=g_id
            ).values('ID_ROLE')
            if role_group_id.exists():
                for subscriber_group_id in role_group_id:
                    self._role_subscriber_group.add(subscriber_group_id["ID_ROLE"])

    def _def_subscriber_group_role_son(self, p_id):
        """
        根据用户组拥有的角色，寻找到所有子集角色
        :return:
        :rtype:
        """
        role_id = ProvenanceSystemSettingsAccountManagementRole.objects.filter(
            STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PARENT=p_id).values('id', 'NAME', 'ID_PARENT')
        if role_id.exists():
            for r_id in role_id:
                self._def_subscriber_group_role_son(r_id['id'])
                self._role_son_subscriber_group.add(r_id['id'])

    def _def_subscriber_group_son(self, p_id):
        """
        当前所属用户组的所有下级用户组
        :return:
        :rtype:
        """
        group_id = ProvenanceSystemSettingsAccountManagementSubscriberGroup.objects.filter(
            STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PARENT=p_id
        ).values('id')
        if group_id.exists():
            for g_id in group_id:
                self._def_subscriber_group_son(g_id['id'])
                self._subscriber_group_son.add(g_id['id'])

    def _def_subscriber_group_son_role(self):
        """
        下级用户组拥有的角色
        :return:
        :rtype:
        """
        g_id_son = ProvenanceSystemSettingsAccountManagementRoleSubscriberGroup.objects.filter(
            STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_SUBSCRIBER_GROUP_id__in=self._subscriber_group_son
        ).values('ID_ROLE')
        if g_id_son.exists():
            for g_id in g_id_son:
                self._role_subscriber_group_son.add(g_id["ID_ROLE"])

    def _def_subscriber_group_son_role_son(self, p_id):
        """
        下级用户组角色的下级角色
        :return:
        :rtype:
        """
        son_id = ProvenanceSystemSettingsAccountManagementRole.objects.filter(
            STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PARENT=p_id
        ).values('id')
        if son_id.exists():
            for s_id in son_id:
                self._def_subscriber_group_son_role_son(s_id["id"])
                self._role_son_subscriber_group_son.add(s_id["id"])

    def _def_subscriber_permission(self):
        """
        查看当前用户所有权限
        :return:
        :rtype:
        """
        permission = ProvenanceSystemSettingsAccountManagementPermissionResults.objects.filter(
            STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_SUBSCRIBER=self.subscriber_id
        ).values('ID_AUTHORITY')
        if permission.exists():
            for id_a in permission:
                self._permission_subscriber.add(id_a["ID_AUTHORITY"])

    def _def_subscriber_permission_son(self, p_id):
        """
        查看当前用户所有权限的子权限
        :param p_id:
        :type p_id:
        :return:
        :rtype:
        """
        son_id = ProvenanceSystemSettingsAccountManagementAuthority.objects.filter(
            STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PARENT=p_id
        ).values('id')
        if son_id.exists():
            for s_id in son_id:
                self._def_subscriber_permission_son(s_id["id"])
                self._permission_subscriber_son.add(s_id["id"])

    def _def_group_permission(self):
        """
        查看当前用户组所有权限
        :return:
        :rtype:
        """
        permission = ProvenanceSystemSettingsAccountManagementPermissionResults.objects.filter(
            STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_SUBSCRIBER_GROUP_id__in=self.group_id
        ).values('ID_AUTHORITY')
        if permission.exists():
            for id_a in permission:
                self._permission_group.add(id_a["ID_AUTHORITY"])

    def _def_group_permission_son(self, p_id):
        """
        查看当前用户组所有权限的子权限
        :param p_id:
        :type p_id:
        :return:
        :rtype:
        """
        son_id = ProvenanceSystemSettingsAccountManagementAuthority.objects.filter(
            STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PARENT=p_id
        ).values('id')
        if son_id.exists():
            for s_id in son_id:
                self._def_group_permission_son(s_id["id"])
                self._permission_group_son.add(s_id["id"])

    def _def_role_permission(self):
        """
        查看当前角色所有权限
        :return:
        :rtype:
        """
        permission = ProvenanceSystemSettingsAccountManagementPermissionResults.objects.filter(
            STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_ROLE_id__in=self.role_id
        ).values('ID_AUTHORITY')
        if permission.exists():
            for id_a in permission:
                self._permission_role.add(id_a["ID_AUTHORITY"])

    def _def_role_permission_son(self, p_id):
        """
        查看当前用户组所有权限的子权限
        :param p_id:
        :type p_id:
        :return:
        :rtype:
        """
        son_id = ProvenanceSystemSettingsAccountManagementAuthority.objects.filter(
            STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PARENT=p_id
        ).values('id')
        if son_id.exists():
            for s_id in son_id:
                self._def_role_permission_son(s_id["id"])
                self._permission_role_son.add(s_id["id"])

    def _def_permission_son(self, p_id):
        """
        总的权限：获得所有下级
        :param p_id:
        :type p_id:
        :return:
        :rtype:
        """
        p_all = ProvenanceSystemSettingsAccountManagementAuthority.objects.filter(
            STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PARENT=p_id
        ).values('id')
        if p_all.exists():
            for s_id in p_all:
                self._def_permission_son(s_id["id"])
                self._permission_son.add(s_id["id"])

    @property
    def run(self):
        if self.subscriber_id:
            # 用户自己的角色
            self._def_subscriber_role()
            if self._role_subscriber:
                for r_id in self._role_subscriber:
                    self._def_subscriber_role_son(r_id)

            # 用户组
            self._def_subscriber_group()
            if self._subscriber_group:
                self._def_subscriber_group_role()  # 用户组-角色：用户组拥有的角色
                if self._role_subscriber_group:
                    for g_id in self._role_subscriber_group:
                        self._def_subscriber_group_role_son(g_id)
                for g_i in self._subscriber_group:
                    self._def_subscriber_group_son(g_i)
                    if self._subscriber_group_son:
                        self._def_subscriber_group_son_role()
                        if self._role_subscriber_group_son:
                            for i in self._role_subscriber_group_son:
                                self._def_subscriber_group_son_role_son(i)

            self._def_subscriber_permission()
            if self._permission_subscriber:
                for i_id in self._permission_subscriber:
                    self._def_subscriber_permission_son(i_id)
            self.group_id = set.union(
                self._subscriber_group,
                self._subscriber_group_son
            )
            if self.group_id:
                self._def_group_permission()
                if self._permission_group:
                    for i_id in self._permission_group:
                        self._def_group_permission_son(i_id)
            self.role_id = set.union(
                self._role_subscriber,
                self._role_son_subscriber,
                self._role_subscriber_group,
                self._role_son_subscriber_group,
                self._role_subscriber_group_son,
                self._role_son_subscriber_group_son,
            )
            if self.role_id:
                self._def_role_permission()
                if self._permission_role:
                    for r_id in self._permission_role:
                        self._def_role_permission_son(r_id)

            self.permission_id = set.union(
                self._permission_subscriber,
                self._permission_subscriber_son,
                self._permission_group,
                self._permission_group_son,
                self._permission_role,
                self._permission_role_son,
            )
            if self.permission_id:
                for per_id in self.permission_id:
                    self._def_permission_son(per_id)
            self.permission_id.update(self._permission_son)

            return {self.subscriber_id: self.permission_id if self.permission_id else None}

        return None


class MenuShowNode(object):
    def __init__(self, menu_id, s_p=None):
        self.s_p = s_p
        self.menu_id = menu_id  # 菜单ID
        self._permission = set()  # 菜单权限
        self.children = []  # 树的孩子结点
        self.parent = None  # 树的父结点
        self.data = []
        self.display = False
        self.mark = self._get_particulars()

    def _get_particulars(self):
        menu_ancestry = ProvenanceSystemSettingsMenuManagementMenu.objects.filter(
            STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, id=self.menu_id
        ).values(
            'ID_PARENT', 'NAME',
            'provenancesystemsettingsmenumanagementmenuparameter__APP_URL_NAME',
            'provenancesystemsettingsmenumanagementmenuparameter__URL_NAME',
            'provenancesystemsettingsmenumanagementmenuparameter__ICON',
        )
        if menu_ancestry.exists():
            for menu in menu_ancestry:
                self._name = menu["NAME"]
                self._p_id = menu["ID_PARENT"]
                self._url_app = menu["provenancesystemsettingsmenumanagementmenuparameter__APP_URL_NAME"]
                self._url = menu["provenancesystemsettingsmenumanagementmenuparameter__URL_NAME"]
                self._icon = menu["provenancesystemsettingsmenumanagementmenuparameter__ICON"]
                permission = ProvenanceSystemSettingsMenuManagementMenuPermission.objects.filter(
                    STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_MENU=self.menu_id
                ).values('ID_AUTHORITY', "ID_AUTHORITY__CODE")
                if permission.exists():
                    for permission_id in permission:
                        p_id = permission_id["ID_AUTHORITY"]
                        if p_id in self.s_p:
                            self.display = True
                        self._permission.add(p_id)
                    if self.display:
                        return False
                else:
                    self.display = True
            return True
        return False

    def add_child(self, child):
        if self.display:
            # permission = self._permission
            # self._permission.update(child._permission)  # 代表上级权限给到下级 但是从本系统角度来讲，不合理。
            child.parent = self  # 要添加的父结点是self
            self.children.append(child)  # 父结点self的children添加child
            self.data.append(child.dict)
            # self._permission.update(permission)
            return True
        # 如果不展示，则父节点不添加任何东西，
        return False

    @property
    def dict(self):
        if self.display:
            data = {
                "menu_id": self.menu_id,
                "_permission": list(self._permission),
                "_p_id": self._p_id,
                "_name": self._name,
                "_url_app": self._url_app,
                "_url": self._url,
                "_icon": self._icon,
                "data": self.data
            }
            return data
        return None


class MenuPermissionTree(object):
    def __init__(self, subscriber_id=None, permission=None):
        self.subscriber_id = subscriber_id
        self.permission = permission
        self.data = []
        self._mark = self._get_ancestry()

    def _get_ancestry(self):
        """
        获取主菜单
        :return:
        :rtype:
        """
        menu_ancestry = ProvenanceSystemSettingsMenuManagementMenu.objects.filter(
            STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PARENT=None
        ).values('id')
        if menu_ancestry.exists():
            for menu in menu_ancestry:
                menu_f = MenuShowNode(menu["id"], self.permission)
                if menu_f.display:
                    if menu_f.mark:
                        self._get_subordinate(menu["id"], menu_f)
                        self.data.append(menu_f.dict)
            return True

        return False

    def _get_subordinate(self, m_id, node):
        """
        获取下级菜单，以及节点信息
        :param m_id:
        :type m_id:
        :param node:
        :type node:
        :return:
        :rtype:
        """
        menu_s = ProvenanceSystemSettingsMenuManagementMenu.objects.filter(
            STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PARENT=m_id
        ).values('id')
        if menu_s.exists():
            for i in menu_s:
                me_s = MenuShowNode(i["id"], self.permission)
                if me_s.display:
                    node.add_child(me_s)
                    self._get_subordinate(i["id"], me_s)

    @property
    def dict(self):
        import json

        data = {
            'data': self.data,
            '_mark': self._mark,
            'subscriber_id': self.subscriber_id,
            'permission': list(self.permission),
        }
        return json.dumps(data, ensure_ascii=False)


class SubscriberRoleMenuNode(object):
    def __init__(self, menu_id, role_id):
        print('            开始初始化')
        self.menu_id = menu_id  # 菜单ID
        self.role_id = role_id  # 菜单所有的角色 set()
        self.children = []  # 树的孩子结点
        self.parent = None  # 树的父结点

    def add_child(self, child):
        print('                添加树信息')
        child.parent = self  # 要添加的父结点是self
        self.children.append(child.dict)  # 父结点self的children添加child
        print('                添加完毕')
        return True

    @property
    def dict(self):
        data = {
            "menu": self.menu_id,
            "role": list(self.role_id),
            "children": self.children,
        }
        return data


class SubscriberExist(object):
    """判断用户是否存在"""

    def __init__(self, subscriber_id):
        self.subscriber_id = self.subscriber_exist(subscriber_id)

    def subscriber_exist(self, subscriber_id):
        if subscriber_id:
            return None if not ProvenanceSystemSettingsAccountManagementSubscriber.objects.filter(
                STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID=subscriber_id
            ).exists() else subscriber_id
        return None


class SubscriberRoleMenu(SubscriberExist):
    """
    返回展示的菜单
    """

    def __init__(self, subscriber_id=None):
        super().__init__(subscriber_id)
        self.role_id = set()
        self.group_id = None
        self._subscriber_group = set()  # 用户组：用户所属的用户组
        self._subscriber_group_son = set()  # 用户组_下级：根据用户所属用户组，找到所有下级用户组
        self._role_subscriber = set()  # 用户_角色：用户拥有的角色
        self._role_son_subscriber = set()  # 用户_角色_下级：根据用户拥有的角色找到的下级角色
        self._role_subscriber_group = set()  # 用户组_角色：用户组拥有的角色
        self._role_son_subscriber_group = set()  # 用户组-角色-下级角色：用户组拥有的下级角色
        self._role_subscriber_group_son = set()  # 用户组_下级用户组_角色：所有的下级用户组，找到对应的角色
        self._role_son_subscriber_group_son = set()  # 用户组_下级用户组_角色_下级角色：所有的下级用户组角色的下级角色
        self.menu_tree = []
        if self.subscriber_id:
            self._def_subscriber()
        else:
            self.role_id.add(18)

    @property
    def dict(self):
        data = {
            'subscriber': self.subscriber_id,
            'group': list(self.group_id if self.group_id else []),
            'role': list(self.role_id if self.role_id else []),
            'menu_tree': list(self.menu_tree),
        }
        return data

    def _def_subscriber(self):
        """用户角色"""
        self._def_subscriber_role()
        if self._role_subscriber:
            for r_id in self._role_subscriber:
                self._def_subscriber_role_son(r_id)
        self._def_subscriber_group()
        if self._subscriber_group:
            self._def_subscriber_group_role()
            if self._role_subscriber_group:
                for g_id in self._role_subscriber_group:
                    self._def_subscriber_group_role_son(g_id)
            for g_i in self._subscriber_group:
                self._def_subscriber_group_son(g_i)
                if self._subscriber_group_son:
                    self._def_subscriber_group_son_role()
                    if self._role_subscriber_group_son:
                        for i in self._role_subscriber_group_son:
                            self._def_subscriber_group_son_role_son(i)
        self.group_id = set.union(self._subscriber_group, self._subscriber_group_son)
        self.role_id = set.union(
            self._role_subscriber, self._role_son_subscriber, self._role_subscriber_group,
            self._role_son_subscriber_group, self._role_subscriber_group_son, self._role_son_subscriber_group_son,
        )

    def _def_subscriber_role(self):
        """
        用户的角色
        :return:
        :rtype:
        """
        role_s = ProvenanceSystemSettingsAccountManagementRoleSubscriber.objects.filter(
            STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_SUBSCRIBER__ID=self.subscriber_id
        ).values('ID_ROLE')
        if role_s.exists():
            for role_id in role_s:
                self._role_subscriber.add(role_id["ID_ROLE"])

    def _def_subscriber_role_son(self, p_id):
        """
        当前所属用户角色的所有下级角色
        :return:
        :rtype:
        """
        group_id = ProvenanceSystemSettingsAccountManagementRole.objects.filter(
            STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PARENT=p_id
        ).values('id')
        if group_id.exists():
            for g_id in group_id:
                self._def_subscriber_role_son(g_id['id'])
                self._role_son_subscriber.add(g_id['id'])

    def _def_subscriber_group(self):
        """
        用户所属的用户组
        :return:
        :rtype:
        """
        s_g = ProvenanceSystemSettingsAccountManagementSubscriberGroupAccount.objects.filter(
            STATUS_IS_DELETE='0', ID_SUBSCRIBER=self.subscriber_id, STATUS_IS_EFFECTIVE=1).values(
            'ID_SUBSCRIBER_GROUP')
        if s_g.exists():
            for son_id in s_g:
                self._subscriber_group.add(son_id["ID_SUBSCRIBER_GROUP"])

    def _def_subscriber_group_role(self):
        """
        用户组拥有的角色
        :return:
        :rtype:
        """
        for g_id in self._subscriber_group:
            r_id = ProvenanceSystemSettingsAccountManagementRoleSubscriberGroup.objects.filter(
                STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_SUBSCRIBER_GROUP=g_id
            ).values('ID_ROLE')
            if r_id.exists():
                for subscriber_group_id in r_id:
                    self._role_subscriber_group.add(subscriber_group_id["ID_ROLE"])

    def _def_subscriber_group_role_son(self, p_id):
        """
        根据用户组拥有的角色，寻找到所有子集角色
        :return:
        :rtype:
        """
        role_id = ProvenanceSystemSettingsAccountManagementRole.objects.filter(
            STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PARENT=p_id).values('id', 'NAME', 'ID_PARENT')
        if role_id.exists():
            for r_id in role_id:
                self._def_subscriber_group_role_son(r_id['id'])
                self._role_son_subscriber_group.add(r_id['id'])

    def _def_subscriber_group_son(self, p_id):
        """
        当前所属用户组的所有下级用户组
        :return:
        :rtype:
        """
        group_id = ProvenanceSystemSettingsAccountManagementSubscriberGroup.objects.filter(
            STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PARENT=p_id
        ).values('id')
        if group_id.exists():
            for g_id in group_id:
                self._def_subscriber_group_son(g_id['id'])
                self._subscriber_group_son.add(g_id['id'])

    def _def_subscriber_group_son_role(self):
        """
        下级用户组拥有的角色
        :return:
        :rtype:
        """
        g_id_son = ProvenanceSystemSettingsAccountManagementRoleSubscriberGroup.objects.filter(
            STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_SUBSCRIBER_GROUP_id__in=self._subscriber_group_son
        ).values('ID_ROLE')
        if g_id_son.exists():
            for g_id in g_id_son:
                self._role_subscriber_group_son.add(g_id["ID_ROLE"])

    def _def_subscriber_group_son_role_son(self, p_id):
        """
        下级用户组角色的下级角色
        :return:
        :rtype:
        """
        son_id = ProvenanceSystemSettingsAccountManagementRole.objects.filter(
            STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PARENT=p_id
        ).values('id')
        if son_id.exists():
            for s_id in son_id:
                self._def_subscriber_group_son_role_son(s_id["id"])
                self._role_son_subscriber_group_son.add(s_id["id"])

    def __def_menu_recursion(self, p_id=None, node=None):
        menu_son = ProvenanceSystemSettingsMenuManagementMenu.objects.filter(
            STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PARENT=p_id
        ).exclude(provenancesystemsettingsmenumanagementmenuroledisplay__ID=None).values('id').distinct()
        if menu_son.exists():
            for menu_id in menu_son:
                menu_role_id = ProvenanceSystemSettingsMenuManagementMenu.objects.filter(
                    STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PARENT=p_id, id=menu_id["id"]
                ).exclude(
                    provenancesystemsettingsmenumanagementmenuroledisplay__ID=None
                ).values('provenancesystemsettingsmenumanagementmenuroledisplay__ID_ROLE').distinct()
                if menu_role_id.exists():
                    distinct_role = set()
                    for role_id in menu_role_id:
                        distinct_role.add(role_id["provenancesystemsettingsmenumanagementmenuroledisplay__ID_ROLE"])
                    if self.role_id & distinct_role:
                        menu_mode = SubscriberRoleMenuNode(menu_id["id"], distinct_role)
                        if node:
                            node.add_child(menu_mode)
                        else:
                            self.menu_tree.append(menu_mode.dict)
                        self.__def_menu_recursion(menu_id["id"], menu_mode)

    @property
    def run(self):
        import json
        self.__def_menu_recursion()
        return json.dumps(self.dict, ensure_ascii=False)
