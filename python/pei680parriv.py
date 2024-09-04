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

filePath = "C:\\Users\\tseguia\\Documents\\PEI680PARRIV\\pei680parriv"
progName = ""
parenthesisIndex = 0
printerString = ""
fileName = ""

# USE FIND
with open(filePath) as fP:
    for line in fP:
        #print(line)
        if "@ASG,A" in line:
            print(line)
        #fileName = line[0:20]
        #progName = line[14:20]
        #parenthesisIndex = line.find(")") + 2
        #printerString = line[parenthesisIndex:]
        #eclStatement = printerString[0:5].strip()
        #print(fileName + " " + progName + " " + printerString[0:5])
        #if (eclStatement == "@SYM"):
            #print(fileName + " " + progName + " " + eclStatement)
            #print(line)
            #if ("psdx" in progName): 
                #if ("SRXQ" in printerString):
                    #print(line)
                    #print(progName + " SRXQ")
                    #horiLine()
                #elif ("SSMPLX" in printerString):
                    #print(line)
                    #print(progName + " SSMPLX")
                    #horiLine()    
