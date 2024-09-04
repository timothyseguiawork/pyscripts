#C:\Users\tseguia\Desktop\INCIDENTS\INC3873667recs
#Python Program used to create an excel sheet for SSI Calendar
#Created by Timothy Seguia, 01/04/2021
from pathlib import Path
import datetime
import xlsxwriter

#CREATE A GLOBAL VARIABLE COUNT
count = 0

def horiLine():
    print("--------------------------------------")
    
def time():
    return datetime.datetime.now()

# C:\\Users\\tseguia\\OneDrive - New York State Office of Information Technology Services\\Desktop
filePath = "C:\\Users\\tseguia\\OneDrive - New York State Office of Information Technology Services\\Desktop\\" 
fileName = "audit-file"
extName = ".txt"

fullPath = filePath + fileName + extName
print(fullPath)
with open(fullPath) as fP:
    header = fP.readline()
    for line in fP: 
        print(line[42:51] + " " + line[2000:2050])
    