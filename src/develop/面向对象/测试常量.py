class SystemConstant:
    class ConstError(TypeError):
        pass

    class ConstCaseError(ConstError):
        pass

    def __setattr__(self, key, value):
        if self.__dict__.get(key):
            raise self.ConstError
        elif not key.isupper():
            raise self.ConstCaseError

        self.__dict__[key] = value


import sys
sys.modules[__name__] = SystemConstant()
