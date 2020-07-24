from cryptography.fernet import Fernet
import xml.etree.ElementTree as ET
import _md5
import xml.dom.minidom as DOM


class EncryptData:
    countKey = 1

    def __init__(self):
        self.dataFile = open('Data.xml')
        self.tree = ET.parse(self.dataFile)
        self.root = self.tree.getroot()
        self.key = Fernet.generate_key()

    def start(self):
        self._saveKey(self.key)

        self.dataFile.close()

    def encrypt(self, data):
        pass

    def decrypt(self):
        pass

    def _saveKey(self, key):
        sub = ET.SubElement(self.root, 'Key')
        count = self.root[0].text
        x = int(count)
        x = x+1
        self.root[0].text = str(x)
        sub.set('id', str(x))
        sub.text = str(self.key)
        self.tree.write('Data.xml')

    def __reFormatXML(self):
        pass
