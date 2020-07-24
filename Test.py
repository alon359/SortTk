from WindowControl import *
from tkinter import *
import xml.etree.ElementTree as ET

root = WindowControl.createWindow(200, 200)
entry = Entry(root, width=30, borderwidth=5).grid(row=0, column=5, columnspan=3)
btnEnter = Button(root, text='Enter').grid(row=1, column=5, columnspan=3)

root.mainloop()
