import sys, requests, os, time
from bs4 import BeautifulSoup
from tkinter import *

def fetchStatus(trackingNumber):
    with requests.session() as browser:
        browser.headers['user-agent'] = 'Mozilla/5.0'
        url = "https://wwu.sclintra.com/Mail/search/show?query=" + trackingNumber
        r = browser.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        quotes = str(soup).split("\"")
        for i in range(0,len(quotes)):
            if (quotes[i] == "Status"):
                return(quotes[i+2])

status = fetchStatus(sys.argv[1])

while (status == "Arrival Scan" or status == "Departure Scan" or status == "Desk Scan" or status == "Desk Accepted"):
    status = fetchStatus(sys.argv[1])
    sys.stdout.write('\r' + str(status))
    sys.stdout.flush()
    time.sleep(1)

top = Tk()
text = Text(top)
text.insert(INSERT, status)
text.pack()
top.minsize(width=200, height=50)
top.maxsize(width=200, height=50)
top.title("Package Status")
top.mainloop()