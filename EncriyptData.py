from cryptography.fernet import Fernet
import xml.etree.ElementTree as ET


class EncryptData:

    def __init__(self):
        self.dataFile = open('Data.xml')
        self.tree = ET.parse(self.dataFile)
        self.root = self.tree.getroot()
        self.key = Fernet.generate_key()
        self.__saveKey(self.key)
        pass

    def encrypt(self, data):
        pass

    def decrypt(self):
        pass

    def __saveKey(self, key):
        self.root[1].text = str(self.key)
        self.tree.write('Data.xml')
        # self.dataFile.close()
        print(self.root[0][0].tag)
        pass
