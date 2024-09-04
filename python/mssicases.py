#Python program for scanning the file that's sent by Shauna.
#Created by Timothy Seguia, 02/05/20
from pathlib import Path
import datetime
import xlsxwriter

#CREATE A GLOBAL VARIABLE COUNT
count = 1

def newLine():
    print()
    
def horiLine():
    print("--------------------------------------")
    
def time():
    return datetime.datetime.now()

def dateFormat(date):
    dd = date[4:]
    yy = date[0:2]
    mm = date[2:4]
    dateString = mm+"/"+dd+"/"+yy
    return dateString

def printInfo(line):
    #batchNumber = line[75:80]
    batchNumber = "*SDN*"
    if "*SDN*" in line:
        caseNumber = line[10:20]
        fileDate = line[20:26]
        procDate = line[38:44]
        print("#" + str(count) + ": " +
              caseNumber + " " +
              batchNumber + " " +
              str(dateFormat(procDate)))
        print(" Case#: " + caseNumber) 
        print(" Batch Transaction: " + batchNumber)
        print(" Date of Error Report: " + dateFormat(fileDate))
        #print(" Case Processed: " + dateFormat(fileDate))
        dateInfo(procDate)
        horiLine()
        
def dateInfo(procDate):
    dd = procDate[4:]
    yy = procDate[0:2]
    mm = procDate[2:4]
    print(" Case Processed = " + dateFormat(procDate))

def realDate(procDate):
    dd = procDate[4:]
    yy = procDate[0:2]
    mm = procDate[2:4]
    print(" Case Processed = " + dateFormat(procDate))
     

def caseList(line):
    global count
    if line[0] == "#":
        print(str(count) + " " + line[4:15])
        count = count + 1
    if "Case Processed" in line:
        print(line)
        horiLine()
            
def shauna(filePath):
    with open(filePath) as fP:
        global count
        for line in fP:
            printInfo(line)
            count = count + 1
            
def krintin(caseFilePath):
    with open(caseFilePath) as fP:
        for line in fP:
            caseList(line)

    
#when you get a new file from shauna, be sure to change the filepath to the
#date you saved that new file
filePath = "W:\wms\dupes"
#fileWritePath = 'C:\Users\tseguia\Desktop\tonymorton.txt'
fileWritePath = "C:\\Users\\tseguia\\Desktop\\tonymorton07232020.txt"
#fileWritePath = "C:\\Users\\tseguia\\Desktop\\07IndividualStatus"
#fileWritePath = "C:\\Users\\tseguia\\Desktop\\01IndividualStatus"


caseNumber = {}
caseCount = 0
#make sure current date matches yymmdd
#if you were to do 02/04/2020 = 200204
#currentDate = "200203"


# USE FIND
# 1275514:00019047130A2002032220980010191910030227060107000200010003000120034*SDN*04F15 132023501E0748
# 0-12, case#
# SHAUNA
# this is for 0748cases
#if fileReadFlag == "SHAUNA":
#    shauna(filePath)
    
# KRINTIN
# this is for krintin
#if fileReadFlag == "KRINTIN":
#    krintin(caseFilePath)

with open(filePath) as fP:
    for line in fP:
        caseCount += 1
        if line.rstrip("\n") not in caseNumber:
            caseNumber[line.rstrip("\n")] = 1
        elif line.rstrip("\n") in caseNumber:
            caseNumber[line.rstrip("\n")] = caseNumber.get(line.rstrip("\n"))+1
        #print(line.rstrip("\n"))
        #print(caseNumber.get(line.rstrip("\n")))

print("Written to: C:\\Users\\tseguia\\Desktop\\tonymorton07232020")
#print("Written to: C:\\Users\\tseguia\\Desktop\\07IndividualStatus")
#print("Written to: C:\\Users\\tseguia\\Desktop\\01IndividualStatus")
print("Total Cases: " + str(caseCount))
print("Case Count#: SSN : no. of open cases")
fWP = open(fileWritePath,'w+')
fWP.write("Written to: C:\\Users\\tseguia\\Desktop\\tonymorton07232020.txt\n")
fWP.write("01-060-CASE-TYPE OF CASE-LINK (CASE-TYPE) \"22\"\n")
fWP.write("03-201-ACCT-NO OF CLIENT: (SSN) \"108785922\"\n")
fWP.write("Total Cases: " + str(caseCount) + "\n")
fWP.write("Case# : ............ : no. of open cases" + "\n")
fWP.write("\n")
caseCount = 0
for i in caseNumber:
    caseCount += 1
    print(str(caseCount) + "#: " + i + " : " + str(caseNumber.get(i)))
    fWP.write("Case# : " + i + " : " + str(caseNumber.get(i)) + "\n")
    #if caseNumber.get(i) > 2:
        #print(str(caseCount) + "#: " + i + ": " + str(caseNumber.get(i)))
        #fWP.write("SSN: " + i + ": " + str(caseNumber.get(i)) + "\n")
#print(caseNumber)
fWP.close()
            
          
