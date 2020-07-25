class SortControl:
    def __init__(self):
        self.text = None
        self.numbersList = None

    def putTestInNumbersList(self, text):
        self.text = text
        self.numbersList = str(self.text).split(',')
        for i in range(0, len(self.numbersList)):
            self.numbersList[i] = int(self.numbersList[i])
        return self.numbersList

    def quickSort(self, sequence):
        pass