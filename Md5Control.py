import hashlib
from XmlHandler import *


class Md5Control:
    def __init__(self):
        self.xmlControl = XmlHandler()

    def encodeMd5(self, st):
        res = hashlib.md5(str(st).encode())
        return res.hexdigest()

    def validate(self, mdStr):

        if mdStr == self.xmlControl.getUserNameFromXml():
            return 'userOk'
        elif mdStr == self.xmlControl.getPassFromXml():
            return 'passOk'
        else:
            return False
