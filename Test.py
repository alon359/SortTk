from EncriyptData import *
from WindowControl import *
from tkinter import *
from Md5Control import *



def main():
    # encrypt = EncryptData()
    # encrypt.start()
    window = WindowControl()
    root = window.createWindow(250, 200)

    root.mainloop()


if __name__ == '__main__':
    main()
