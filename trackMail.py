# import dependencies
import sys, requests, os, time
from bs4 import BeautifulSoup
from tkinter import *

# scrape the current status of a package by tracking number, returns status string
def fetchStatus(trackingNumber):
    
    # setup browser object
    with requests.session() as browser:
        browser.headers['user-agent'] = 'Mozilla/5.0'
        url = "https://wwu.sclintra.com/Mail/search/show?query=" + trackingNumber
        r = browser.get(url)

        # parse output
        soup = BeautifulSoup(r.text, 'html.parser')
        quotes = str(soup).split("\"")

        # find status element
        for i in range(0,len(quotes)):
            if (quotes[i] == "Status"):
                return(quotes[i+2])

# check for correct number of command line arguments
if (len(sys.argv) > 2):
    print("You need to specifiy the tracking number of the package!")
    print("trackMail.py -help for more info")
    sys.exit()

# check for help command
if (sys.argv[1] == "-help"):
    print("mailTrack.py")
    print("A simple python script for checking the status of packages at WWU")
    print("Usage:")
    print("trackMail.py <tracking number> [<tracking number>]...")
    sys.exit()

# fetch the status the first time
status = fetchStatus(sys.argv[1])

# check to make sure that the package is in the system
if(str(status) != "None"):

    # until the package arrives, wait a few seconds and try again
    while (status == "Arrival Scan" or status == "Departure Scan" or status == "Transferred To Hall" or status == "Desk Scan" or status == "Desk Accepted"):
        status = fetchStatus(sys.argv[1])
        sys.stdout.write('\r' + str(status) + 20*" ")
        sys.stdout.flush()
        time.sleep(5)

    # if the package arrives, create a simple tkinter popup window
    top = Tk()
    text = Text(top)
    text.insert(INSERT, str(status))
    text.pack()
    top.minsize(width=200, height=50)
    top.maxsize(width=200, height=50)
    top.title("Package Status")
    top.focus_force()
    top.mainloop()

# if the package could not be found, throw an error
else:
    print("Sorry, that package could not be located!")