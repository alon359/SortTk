from tkinter import *
from Md5Control import *
from SortControl import *


class WindowControl:

    def __init__(self):
        self.md = Md5Control()
        self.sortControl = SortControl()
        self.userLbl = None
        self.passLbl = None
        self.entryUser = None
        self.entryPass = None
        self.btnEnter = None
        self.root = None
        self.input = None
        self.lbl = None
        self.input2 = None
        self.btnEnter2 = None
        self.lbl2 = None
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
                i.grid_forget()
            self._createSecondWindow()

    def _createSecondWindow(self):
        self.input2 = Entry(self.root, width=30, text='input2')
        self.input2.pack()
        print(type(self.input2))

        self.btnEnter2 = Button(self.root, text='Enter', command=self._executeSort)
        self.btnEnter2.pack()
        self.lbl2 = Label(self.root, width=38, text='Please enter numbers separate by comma')
        self.lbl2.pack()

    def _executeSort(self):
        numbersList = self.sortControl.putTestInNumbersList(self.input2.get())
