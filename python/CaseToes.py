#Python Program for calculating distribution list for cins and transactions
#Created by Timothy Seguia, 11/13/19
from pathlib import Path
import datetime

def newLine():
    print()
def horiLine():
    print("____________________________________")
def time():
    return datetime.datetime.now()


filePath = "C:\\Users\\tseguia\\Desktop\\MONITOR\\03-09-2020\\cases"
f = open("C:\\Users\\tseguia\\Desktop\\MONITOR\\03-09-2020\\workfile", "w")
progName = ""
parenthesisIndex = "0"
printerString = ""
fileName = ""
toeList = []
toeNum = "0"

# USE FIND
with open(filePath) as fP:
    print("Case Numbers:")
    for line in fP:
        if line[0:2] == "00":
            caseNumber = line[0:12]
            toe = line[10]
            if toe == toeNum:
                print(toeNum + " " + caseNumber)
            if toe not in toeList:
                toeList.append(toe)
            f.write(caseNumber + " " + toe + "\n")
            print(caseNumber + " " + toe)
    f.write("____________________________________")
    horiLine()
    
    #TOES NEEDED
    toeString = "["
    print(toeList)
    for i in toeList:
        toeString = toeString + " " + i 
        print(toeString)
    toeString = toeString + " ]"
    print(toeString)
    f.write("\n")
    newLine()
    f.write(toeString + "\n")
    print(toeList)
    f.write("____________________________________")
    horiLine()
    f.write("\n")
    newLine()

    #FILES REQUIRED
    print("Files required to restore:")
    print(" - For PEIZt0/EI1016")
    for i in toeList:
        f.write("CSPROD*PEIY"+i+"0PSSI"+i+"T" + "\n")
        print ("CSPROD*PEIY"+i+"0PSSI"+i+"T")
    f.write("\n")
    newLine()
    print(" - For PEIAt0/EI1026,EI1024")
    for i in toeList:
        f.write("CSPROD*PIY03"+i+"P0000"+i+ "\n")
        print ("CSPROD*PIY03"+i+"P0000"+i)    
    f.write("____________________________________")
    horiLine()

    for line in fP:
        toe = line[10]
        

f.close()
