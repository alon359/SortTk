from WindowControl import *
from tkinter import *
import xml.etree.ElementTree as ET


def main():
    root = WindowControl.createWindow(250, 200)
    WindowControl.putObjectsOnTheWindow(root)
    root.mainloop()


if __name__ == '__main__':
    main()
