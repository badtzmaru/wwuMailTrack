import sys, requests, os, time
from bs4 import BeautifulSoup
from Tkinter import *

# scrape the current status of a package by tracking number, returns status string
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

# fetch the status the first time
status = fetchStatus(sys.argv[1])

# until the package arrives, wait a few seconds and try again
while (status == "Arrival Scan" or status == "Departure Scan" or status == "Transferred To Hall" or status == "Desk Scan" or status == "Desk Accepted"):
    status = fetchStatus(sys.argv[1])
    sys.stdout.write('\r' + str(status) + 20*" ")
    sys.stdout.flush()
    time.sleep(5)

# if the package arrives, create a simple tkinter popup window
top = Tk()
text = Text(top)
text.insert(INSERT, status)
text.pack()
top.minsize(width=200, height=50)
top.maxsize(width=200, height=50)
top.title("Package Status")
top.mainloop()