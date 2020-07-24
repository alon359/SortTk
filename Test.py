from EncriyptData import *
from WindowControl import *
from tkinter import *


def main():
    encrypt = EncryptData()
    root = WindowControl.createWindow(250, 200)
    WindowControl.putObjectsOnTheWindow(root)
    encrypt.start()
    root.mainloop()


if __name__ == '__main__':
    main()
