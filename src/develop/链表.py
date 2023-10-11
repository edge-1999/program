class Node:  # 链表的节点类
    def __init__(self, data, _prev=None, _next=None):
        self.prev = _prev  # 指针域 指向的是当前节点的前一个节点
        self.data = data  # 数据域
        self.next = _next  # 指针域 指向的是当前节点的下一个节点


class DoubleLinkList:
    def __init__(self):
        self.head = None  # 头结点
        self._length = 0  # 长度

    def is_empty(self):
        # 链表是否为空
        return self._length == 0

    def length(self):
        # 链表长度
        return self._length

    def nodes_list(self):
        # 返回链表中的所有节点的值组成的列表
        ls = []
        cur = self.head
        while cur != None:  # cur = None时找到尾结点
            ls.append(cur.data)
            cur = cur.next  # 链表不为空时继续向后
        return ls  # 返回链表

    def add(self, data):
        # 向链表的头部添加一个节点 data
        node = Node(data)  # 新建一个节点
        if self.is_empty():  # 链表为空
            self.head = node
        else:  # 链表不为空
            self.head.prev = node  # 1 让链表中原本得头结点prev指向新建节点
            # 如果链表为空时self.head = None 无法调用None.prev
            node.next = self.head  # 2让node指向当前链表中的头结点
            self.head = node  # 3再让链表的head指向当前node节点
        self._length += 1  # 添加节点 链表长度+1

    def append(self, data):
        # 向链表的尾部添加一个节点， 值为data
        # 新建一个节点node, 值为data
        node = Node(data)
        if self.head != None:  # 链表不为空 有元素
            cur = self.head
            # 链表为空时，self.head 为None  无法执行循环中的.next         while cur.next != None: #cur.next = None时找到尾结点

            # 找到链表的尾节点
            # 从头结点开始，遍历链表中所有的结点
            # 每次判断当前节点的next是否为空
            # 为空说明当前节点就是尾结点
            # 不为空时，通过当前节点得next去访问下一个节点
            while cur.next != None:  # cur.next = None时找到尾结点cur
                cur = cur.next
            # 让当前的尾节点得指针域指向node
            node.prev = cur  # 让node的prev指向原本的尾节点
            cur.next = node  # 让原本的尾节点的next去指向新建的节点
            # 添加完毕，链表的长度+1

        else:  # 空链表
            self.head = node
        self._length += 1

    def insert(self, pos, data):
        # 向指定位置添加节点，值为data
        # 异常情况 超出边界
        if pos <= 0:
            self.add(data)
        elif pos >= self._length:
            self.append(data)
        else:
            node = Node(data)  # 1
            cur = self.head
            n = 0  # 2找链表中索引为pos-1的节点（0,1,2）， cur = cur.next 执行pos-1步
            while n < pos - 1:
                cur = cur.next
                n = n + 1
            # 到这里cur指向的是索引为pos-1 的节点

            # 1新的节点node的prev指向索引为pos -1的节点
            node.prev = cur

            # 2链表中原本索引为pos的节点prev指向新的节点node
            cur.next.prev = node

            # 3新的节点node的next指向链表中原本索引为pos的节点
            node.next = cur.next  # cur.next 为pos的节点

            # 4让索引为pos-1的节点得next指向node
            cur.next = node

            self._length += 1  # 5 长度+1

    def remove(self, data):
        # 删除链表中第一个值为data的节点
        cur = self.head
        while cur:
            if cur.data == data:  # 找到要删的节点
                # 如果前驱节点为空， 说明我们要删除的节点是第一个节点
                if cur == self.head:  # 删的是第一个结点
                    self.head = cur.next  # 指向第二个节点
                    self.head.prev = None
                else:  # 要删除的不是第一个节点
                    cur.prev.next = cur.next  # 要删除节点的前一节点的next指向要删除节点的后一个节点
                    # 如要删除的节点为最后一个节点，只需执行这一步
                    if cur.next != None:  # 判断cur.next是否存在
                        cur.next.prev = cur.prev  # 要删除节点的下一节点的prev指向要删除节点的前一个节点
                self._length -= 1
                return 0  # 找到
            cur = cur.next  # 继续向后
        return -1  # 没有找到

    def modify(self, pos, data):
        # 修改链表中指定位置的节点
        if pos < 0 or pos >= self._length:
            print("位置不正确")  # 位置不正确
        else:
            cur = self.head
            n = 0  # 找链表中索引为pos的节点（0,1,2）， cur = cur.next 执行pos-1步
            while n < pos:
                cur = cur.next
                n = n + 1
            cur.data = data

    def search(self, data):
        # 查找链表中是否有节点的值为data
        cur = self.head
        while cur:
            if cur.data == data:
                return True  # 找到
            cur = cur.next  # 继续向后
        return False  # 没有找到


if __name__ == "__main__":
    l1 = DoubleLinkList()  # 新建一个链表类

    print(l1.nodes_list())

    l1.add(1)
    print(l1.nodes_list())

    l1.add(2)
    print(l1.nodes_list())

    l1.append(3)
    print(l1.nodes_list())

    l1.insert(1, 7)
    print(l1.nodes_list())

    l1.insert(5, 5)
    print("插入")
    print(l1.nodes_list())

    l1.remove(2)
    print(l1.nodes_list())

    l1.modify(0, 0)
    print(l1.nodes_list())

    print("查找")
    print(l1.search(5))
