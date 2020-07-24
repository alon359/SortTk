import xml.etree.ElementTree as ET


class XmlHandler:

    def __init__(self):
        self.tree = ET.parse('mdData')
        self.root = self.tree.getroot()


