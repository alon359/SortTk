from tkinter import *
from Md5Control import *


class WindowControl:

    def __init__(self):
        self.md = Md5Control()
        self.userLbl = None
        self.passLbl = None
        self.entryUser = None
        self.entryPass = None
        self.btnEnter = None
        self.root = None

        pass

    def createWindow(self, w, h):
        self.root = Tk()
        self.root.title('Sorting')
        rootWidth = w
        rootHeight = h
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        xCoordinate = (ws / 2) - (rootWidth / 2)
        yCoordinate = (hs / 2) - (rootHeight / 2)
        self.root.geometry('%dx%d+%d+%d' % (rootWidth, rootHeight, xCoordinate, yCoordinate))
        self._putObjectsOnTheWindow(self.root)
        return self.root

    def _putObjectsOnTheWindow(self, root):
        self.userLbl = Label(root, text="username").grid(row=0, column=0)
        self.passLbl = Label(root, text="password").grid(row=1, column=0)
        self.entryUser = Entry(root, width=20, borderwidth=5)
        self.entryUser.grid(row=0, column=1, columnspan=3)
        self.entryPass = Entry(root, width=20, borderwidth=5)
        self.entryPass.grid(row=1, column=1)
        self.btnEnter = Button(root, text='Enter', command=self._enterClick).grid(row=2, column=1, columnspan=3)

    def _enterClick(self):
        user = self.entryUser.get()
        password = self.entryPass.get()
        userEncode = self.md.encodeMd5(user)
        passEncode = self.md.encodeMd5(password)
        if self.md.validate(userEncode) and self.md.validate(passEncode):
            ObjectsList = self.root.grid_slaves()
            for i in ObjectsList:
                i.destroy()
            self._createSecondWindow()

    def _createSecondWindow(self):
        self.entryUser = Entry(self.root).grid(row=0)
