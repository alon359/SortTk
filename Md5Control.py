import hashlib
from XmlHandler import *


class Md5Control:
    def __init__(self):
        self.xmlControl = XmlHandler()

    def encodeMd5(self, st):
        res = hashlib.md5(str(st).encode())
        return res.hexdigest()

    def validator(self, mdstr):
        pass
