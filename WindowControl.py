from tkinter import *


class WindowControl:

    def __init__(self):
        pass

    @staticmethod
    def createWindow(w, h):
        root = Tk()
        root.title('Sorting')
        rootWidth = w
        rootHeight = h
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        xCoordinate = (ws / 2) - (rootWidth / 2)
        yCoordinate = (hs / 2) - (rootHeight / 2)
        root.geometry('%dx%d+%d+%d' % (rootWidth, rootHeight, xCoordinate, yCoordinate))
        return root

