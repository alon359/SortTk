class SortControl:
    def __init__(self):
        self.text = None
        self.numbersList = None

    def putTestInNumbersList(self, text):
        self.text = text
        self.numbersList = str(self.text).split(',')
        print(self.numbersList)
        for i in range(0, len(self.numbersList)):
            self.numbersList[i] = int(self.numbersList[i])
        print(self.numbersList)

