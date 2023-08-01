""" GUI tool to open browser """

import webbrowser
from tkinter import *

gui = Tk( )

gui.title('Open Browser')
gui.geometry('250x100')


def google():

    webbrowser.open('www.google.com')


Button(gui, text='Open Google', command=google, background='lightblue').pack(pady=20)
gui.mainloop()
