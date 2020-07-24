import xml.etree.ElementTree as ET


class XmlHandler:

    def __init__(self):
        self.tree = ET.parse('mdData.xml')
        self.root = self.tree.getroot()

    def getUserNameFromXml(self):
        userName = self.root.find('userName')
        return str(userName.text)

    def getPassFromXml(self):
        password = self.root.find('password')
        return str(password.text)
