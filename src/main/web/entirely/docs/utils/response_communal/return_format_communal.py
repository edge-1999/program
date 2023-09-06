class JsonResponsePostJsonBasic(object):
    def __init__(self):
        self.appCode = None  # 状态码
        self.appMessage = None  # 返回信息
        self.data = []  # 数据
        self.expandKeys = None  # 扩展
        self.success = False  # 是否成功

    @property
    def dict(self):
        return self.__dict__


class ResponseJsonBasic(object):
    def __init__(self):
        self.status = False
        self.detail = None
        self.data = None

    @property
    def dict(self):
        return self.__dict__
