#READ ME!
#AutoPy is designed to be used on WINDOWS only. It won't work on mac or linux (sorry!)


#Code (c) Pixl8 2021
cv = "1.0.0"


from tkinter import *
from tkinter import messagebox
import urllib.request  # the lib that handles the url
from termcolor import colored # colours!
import sys
import webbrowser
from time import sleep
print("AutoPy v1.0.0 by Pixl8")

window = Tk()
window.withdraw()




def printslow(text):
    for char in text:
        sleep(0.03)
        sys.stderr.write(char)

printslow("Checking for AutoPy updates...")
        
def checkupdate(currentVersion, domain, downloadFileName):
    tms = 0
    print("\n Checking for updates...")
    updateRequest = urllib.request.urlopen(domain + "/v.txt")
    for line in updateRequest:
        if tms < 1:
            updateResult = print(line)
            tms += 1
    tms = 0
    if updateResult == "b'" + currentVersion + "'":
        print("No update necessary.")
    elif updateResult != currentVersion:
        print("Update needed. New version is: " + str(line) + " Current version is: " + currentVersion)
        messagebox.showwarning("Update", "A new update is available. Press OK to install it. It won't take long...")
        webbrowser.open(domain + "/" + downloadFileName)
        sleep(5) #this is the time to wait for the download
        open("C://Users/" + getpass.getuser() + "/Downloads/" + downloadFileName)


checkupdate(cv, "https://autopyupdatenetwork.netlify.app", "") #AutoPy uses AutoPy to update AutoPy!
