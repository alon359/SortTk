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

    @staticmethod
    def putObjectsOnTheWindow(root):
        userLbl = Label(root, text="username").grid(row=0, column=0)
        passLbl = Label(root, text="password").grid(row=1, column=0)
        entryUser = Entry(root, width=20, borderwidth=5).grid(row=0, column=1, columnspan=3)
        entryPass = Entry(root, width=20, borderwidth=5).grid(row=1, column=1)
        btnEnter = Button(root, text='Enter').grid(row=2, column=1, columnspan=3)

