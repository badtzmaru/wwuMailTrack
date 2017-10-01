import sys, requests
from bs4 import BeautifulSoup
from tkinter import *
import tkMessageBox

def fetchStatus(trackingNumber):
    print(trackingNumber)
    with requests.session() as browser:
        browser.headers['user-agent'] = 'Mozilla/5.0'
        url = "https://wwu.sclintra.com/Mail/search/show?query=" + trackingNumber
        r = browser.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        quotes = str(soup).split("\"")
        for i in range(0,len(quotes)):
            if (quotes[i] == "Status"):
                tkMessageBox.showinfo("Package Status", quotes[i+2])


top = Tk()
L1 = Label(top, text="Tracking number")
L1.pack( side = LEFT)
E1 = Entry(top, bd = 5)
E1.pack(side = RIGHT)
B = Button(top, text ="Get Status", command = fetchStatus(E1.get()))
B.pack(side = LEFT)
top.mainloop()
