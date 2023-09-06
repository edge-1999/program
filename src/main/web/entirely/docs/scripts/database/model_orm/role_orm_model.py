# from menu_management.models import ProvenanceSystemSettingsMenuManagementMenu, \
#     ProvenanceSystemSettingsMenuManagementMenuPermission
#
#
# class NodeCommunal(object):
#     def __init__(self, item):
#         self.item = item  # 数据域
#         self.next = None  # 指针域：指向下一个节点
#         self.prev = None  # 指针域：指向上一个节点
#
#
# class MenuPermission(object):
#     """
#     如果用户在当前菜单有【查看】其他权限，那么该菜单前的菜单一定能查看，但是没有其他的权限。其他的权限根据具体情况继承
#     所以采用链表的方式处理菜单，双向链表  头尾呼应暂不确定是否可取
#     """
#
#     def __init__(self):
#         self.head = None
#
#     def is_empty(self):
#         """
#         判断链表是否为空
#         :return: self.head == None  self.head is None
#         :rtype: bool
#         """
#         return self.head is None
#
#     def i_size(self) -> int:
#         """
#         返回链表中元素数量
#         :return:
#         :rtype:
#         """
#         s = 0
#         m = self.head
#         while m.next:
#             s += 1
#             m = m.next
#         return s
#
#     def i_add(self, item):
#         """
#         在链表头部添加元素item
#         :param item:
#         :type item:
#         :return:
#         :rtype:
#         """
#         t = NodeCommunal(item)
#         m = self.head
#         if m is None:
#             self.head = t
#         else:
#             t.next = m
#             m.prev = t
#             self.head = t
#
#     def i_append(self, item):
#         """
#         在链表尾部添加元素item
#         :param item:
#         :type item:
#         :return:
#         :rtype:
#         """
#         t = NodeCommunal(item)
#         m = self.head
#         # if m == None:
#         if m is None:
#             self.head = t
#             return
#         else:
#             while m.next:
#                 m = m.next
#             m.next = t
#             t.prev = m
#
#     def i_insert(self, index, item):
#         """
#         在链表索引index处添加元素item
#                 if pos <= 0:
#             self.add(data)
#             需要考虑索引 比如列表索引 -1 的话应该在最后一个位置添加
#         :param index:
#         :type index:
#         :param item:
#         :type item:
#         :return:
#         :rtype:
#         """
#         t = NodeCommunal(item)
#         m = self.head
#         length = self.i_size()
#         index = index if index >= 0 else length - abs(index) + 1
#         if m is None:
#             self.head = t
#         elif index + 1 > length:
#             self.i_append(item)
#         else:
#             i = 0
#             while i < index:
#                 m = m.next
#                 i += 1
#             t.next = m
#             t.prev = m.prev
#             if i == 0:
#                 m.prev = t
#                 self.head = t
#             else:
#                 m.prev.next = t
#                 m.prev = t
#
#     def d_delete(self, item):
#         """
#         删除链表中第一个值为item元素的节点
#         :param item:
#         :type item:
#         :return:
#         :rtype:
#         """
#         m = self.head
#         if m is None:
#             return
#         elif m.next is None:
#             self.head = None
#         else:
#             while m.item != item:
#                 m = m.next
#             if m.next is None:
#                 m.prev.next = None
#             elif m.prev is None:
#                 self.head = m.next
#             else:
#                 m.next.prev = m.prev
#                 m.prev.next = m.next
#                 del m
#
#     def d_pop(self):
#         """
#         删除链表尾部的元素，并取出。
#         :return:
#         :rtype:
#         """
#         m = self.head
#         if m is None:
#             return
#         while m.next.next:
#             m = m.next
#         r = m.next
#         m.next = None
#         return r.item
#
#     def u_modify(self, pos, item) -> bool:
#         """
#         修改链表中指定位置的节点
#         :param pos:
#         :type pos: int
#         :param item:
#         :type item:
#         :return:
#         :rtype:
#         """
#         length = self.i_size()
#         index = pos if pos >= 0 else length - abs(pos) + 1
#         if index < 0 or index >= length:
#             return False
#         else:
#             cur = self.head
#             n = 0  # 找链表中索引为pos的节点（0,1,2）， cur = cur.next 执行pos-1步
#             while n < index:
#                 cur = cur.next
#                 n = n + 1
#             cur.item = item
#         return True
#
#     def s_find(self, item):
#         """
#         查找链表中item的索引位置
#         :param item:
#         :type item:
#         :return:
#         :rtype:
#         """
#         m = self.head
#         s = 0
#         while m:
#             if m.item == item:
#                 s += 1
#             m = m.next
#         return s
#
#     def s_search(self, item):
#         """
#         查找链表中是否有节点的值为data
#         :param item:
#         :type item:
#         :return:
#         :rtype:
#         """
#         cur = self.head
#         while cur:
#             if cur.item == item:
#                 return True  # 找到
#             cur = cur.next  # 继续向后
#         return False  # 没有找到
#
#     def printall(self):
#         """
#         遍历所有节点
#         :return:
#         :rtype:
#         """
#         m = self.head
#         while m:
#             print(m.item, end="\n ")
#             m = m.next
#
#
# class MenuPermissionTreeNode(object):
#     def __init__(self, menu_id, s_p=None):
#         self.s_p = s_p
#         self.menu_id = menu_id  # 菜单ID
#         self._permission = set()  # 菜单权限
#         self.children = []  # 树的孩子结点
#         self.parent = None  # 树的父结点
#         self.data = []
#         self.mark = self._get_particulars()
#
#     def _get_particulars(self):
#         menu_ancestry = ProvenanceSystemSettingsMenuManagementMenu.objects.filter(
#             STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, id=self.menu_id
#         ).values(
#             'ID_PARENT', 'NAME',
#             'provenancesystemsettingsmenumanagementmenuparameter__APP_URL_NAME',
#             'provenancesystemsettingsmenumanagementmenuparameter__URL_NAME',
#             'provenancesystemsettingsmenumanagementmenuparameter__ICON',
#         )
#         if menu_ancestry.exists():
#             for menu in menu_ancestry:
#                 self._name = menu["NAME"]
#                 self._p_id = menu["ID_PARENT"]
#                 self._url_app = menu["provenancesystemsettingsmenumanagementmenuparameter__APP_URL_NAME"]
#                 self._url = menu["provenancesystemsettingsmenumanagementmenuparameter__URL_NAME"]
#                 self._icon = menu["provenancesystemsettingsmenumanagementmenuparameter__ICON"]
#                 permission = ProvenanceSystemSettingsMenuManagementMenuPermission.objects.filter(
#                     STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_MENU=self.menu_id
#                 ).values('ID_AUTHORITY', "ID_AUTHORITY__CODE")
#                 if permission.exists():
#                     for permission_id in permission:
#                         self._permission.add(permission_id["ID_AUTHORITY"])
#                     # self._permission.add(permission_id["ID_AUTHORITY"] for permission_id in permission)
#                 # self._permission.add(
#                 #     permission_id["ID_AUTHORITY"] for permission_id in permission if permission.exists())
#             return True
#         return False
#
#     def add_child(self, child):
#         # permission = self._permission
#         # self._permission.update(child._permission)  # 代表上级权限给到下级 但是从本系统角度来讲，不合理。
#         child.parent = self  # 要添加的父结点是self
#         self.children.append(child)  # 父结点self的children添加child
#         self.data.append(child.dict)
#         # self._permission.update(permission)
#
#     @property
#     def dict(self):
#         data = {
#             "menu_id": self.menu_id,
#             "_permission": list(self._permission),
#             "_p_id": self._p_id,
#             "_name": self._name,
#             "_url_app": self._url_app,
#             "_url": self._url,
#             "_icon": self._icon,
#             "data": self.data
#         }
#         return data
#
#
# class MenuPermissionTree(object):
#     def __init__(self, subscriber_id=None, permission=None):
#         self.subscriber_id = subscriber_id
#         self.permission = permission
#         self.data = []
#         self._mark = self._get_ancestry()
#
#     def _get_ancestry(self):
#         """
#         获取主菜单
#         :return:
#         :rtype:
#         """
#         menu_ancestry = ProvenanceSystemSettingsMenuManagementMenu.objects.filter(
#             STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PARENT=None
#         ).values('id')
#         if menu_ancestry.exists():
#             for menu in menu_ancestry:
#                 menu_f = MenuPermissionTreeNode(menu["id"], self.permission)
#                 if menu_f.mark:
#                     self._get_subordinate(menu["id"], menu_f)
#                     self.data.append(menu_f.dict)
#             return True
#
#         return False
#
#     def _get_subordinate(self, m_id, node):
#         """
#         获取下级菜单，以及节点信息
#         :param m_id:
#         :type m_id:
#         :param node:
#         :type node:
#         :return:
#         :rtype:
#         """
#         menu_s = ProvenanceSystemSettingsMenuManagementMenu.objects.filter(
#             STATUS_IS_DELETE='0', STATUS_IS_EFFECTIVE=1, ID_PARENT=m_id
#         ).values('id')
#         if menu_s.exists():
#             for i in menu_s:
#                 me_s = MenuPermissionTreeNode(i["id"], self.permission)
#                 node.add_child(me_s)
#                 self._get_subordinate(i["id"], me_s)
#
#     @property
#     def dict(self):
#         import json
#
#         data = {
#             'data': self.data,
#             '_mark': self._mark,
#             'subscriber_id': self.subscriber_id,
#             'permission': list(self.permission),
#         }
#         return json.dumps(data, ensure_ascii=False)
