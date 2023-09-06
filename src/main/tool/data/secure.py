import base64
import lzma
import os


class DataSecureOperations(object):
    """数据加密"""

    def __init__(self, data):
        self.data = data
        self.identifying = False
        self.error_message = []

    @property
    def def_encryption_lzma_base64_bytes(self):
        """lzma+base64加密解密"""
        if isinstance(self.data, bytes):
            self.identifying = True
            return self.data

        elif isinstance(self.data, str):
            self.identifying = True
            return base64.b64encode(self.data.encode())

        self.identifying = False
        return b''

    @property
    def def_decrypt_lzma_base64_bytes(self):
        """返回解密数据"""
        if isinstance(self.data, str):
            self.identifying = True
            return lzma.decompress(base64.b64decode(self.data)).decode('utf-8')
        elif isinstance(self.data, bytes):
            self.identifying = True
            return lzma.decompress(base64.b64decode(self.data))
        else:
            self.identifying = False
            self.error_message.append(f'暂不支持 {type(self.data)} 此类数据解密')
            return None
