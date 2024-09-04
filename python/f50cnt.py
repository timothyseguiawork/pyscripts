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
fileName = "ssasdxupd1"
extName = ".txt"

fullPath = filePath + fileName + extName

print(fullPath)
var = 0
medEligCodeY = 0
medEligCodeB = 0

horiLine()
with open(fullPath) as fP:
    header = fP.readline()
    splitLine = header.split()
    headerString = "Header: " + str(splitLine[5])
    print(headerString)
    print("216-MEDICAID-ELIGIBILITY-CODE COUNTS")
    for line in fP:
        #print(len(line))
        #print(line[1537])

        #if var == 4:
            #break 
        if (var == 0) & (line[1537] == " "):
            #print("hit 0")
            print(var)
            var += 1
            continue
        elif line[1537] == "Y":
            #print("hit 1")
            #print(line[1537])
            medEligCodeY += 1
        elif line[1537] == " ":
            #print("hit 2")
            medEligCodeB += 1
        elif (var == 7743) & (line[1537] == " "):
            #print("hit 3")
            var += 1
            print(var)
            continue
        #print(var)
        var += 1
#print("END LOOP")        

horiLine()
print("Y = " + str(medEligCodeY))
print("Blank = " + str(medEligCodeB))
horiLine()
#    for line in fP:
#        if var == 1: #
#            print(var)
#            horiLine()
#            print(len(line))
#            horiLine()
#            var += 1
#        else:
#            break
#print("END PROG")
fP.close()