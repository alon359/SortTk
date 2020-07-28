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
        length = len(sequence)
        if length <= 1:
            return sequence
        else:
            pivot = sequence.pop()
        items_greater = []
        items_lower = []
        for item in sequence:
            if item > pivot:
                items_greater.append(item)
            else:
                items_lower.append(item)
        return self.quickSort(items_lower) + [pivot] + self.quickSort(items_greater)
