#C:\Users\tseguia\Desktop\INCIDENTS\INC3873667recs
#WILL MAKE THIS EASIER TO DIGEST TOMORROW 10/06/2020
#Python Program used to put case numbers and CINs in an excel sheet
#Created by Timothy Seguia, 02/05/20
from pathlib import Path
import datetime
import xlsxwriter
from datetime import date 

#CREATE A GLOBAL VARIABLE COUNT
count = 1

def newLine():
    print()
    
def horiLine():
    print("--------------------------------------")
    
def time():
    return(date.today())

def dateFormat(date):
    #20011217
    if not date.isspace():
        dd = date[6:8]
        yy = date[0:4]
        mm = date[4:6]
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

filePath = "W:\\wms\\lqsnap2"

caseNo = ""                #a
office = ""                #b
name = ""                  #c
cin = ""                   #d
dob = ""                   #e
ssn = ""                   #f
appDate = ""               #g
regDate = ""               #h
caseStatus = ""            #i

time()
# Create an new Excel file and add a worksheet.
excelFP = "C:\\Users\\tseguia\\Desktop\\INCIDENTS\\lqsnap2\\" + str(time()) + ".xlsx"
txtFP = "C:\\Users\\tseguia\\Desktop\\INCIDENTS\\lqsnap2\\" + str(time()) + ".txt"
print(excelFP)
workbook = xlsxwriter.Workbook(excelFP)
worksheet = workbook.add_worksheet()

# Widen the first column to make the text clearer.
# ignore ssn
worksheet.set_column('A:A', 30)
worksheet.set_column('B:B', 30)
worksheet.set_column('C:C', 30)
worksheet.set_column('D:D', 30)
worksheet.set_column('E:E', 30)
worksheet.set_column('F:F', 30)
worksheet.set_column('G:G', 40)
worksheet.set_column('H:H', 30)
worksheet.set_column('I:I', 30)

# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': True})

#00019677410D F46 WMCJT SUPONNA          NFN         KK08747E 20060918 ######### 20200928                  09 01 09  
## Write some simple text.

#NO APP REG DATE BECAUSE THESE ARE APPLICATIONS

#01-052-CASE-NO OF CASE                  A
#1-01-020-LOCAL-OFFICE OF CASE           B
#1-01-040-RESP-WORKER OF CASE            C
#03-030-NAME OF CLIENT                   D
#03-010-RECIP-ID OF CLIENT               E
#03-060-DOB OF CLIENT                    F
#03-201-ACCT-NO OF CLIENT                G
#01-090-APPLCTN-DATE-Y2K OF SUFFIX       H
#01-100-AUTH-PERIOD-Y2K OF SUFFIX        
#2-02-090-CASE-STATUS OF SUFFIX          I

worksheet.write('A1', 'SSN', bold)
worksheet.write('B1', 'CIN', bold)
worksheet.write('C1', 'Case Number', bold)
worksheet.write('D1', 'Center', bold)
worksheet.write('E1', 'Process', bold)
worksheet.write('F1', 'Application Date', bold)
worksheet.write('G1', 'Name', bold)
worksheet.write('H1', 'Date Of Birth', bold)
worksheet.write('I1', 'Case Status', bold)

ssnDict = {}
lineList = []
ssnList = [] 
dupeSSN = 0
dupeApp = 0
printCount = 1

with open(filePath) as fP:
    for line in fP:
# FILE FORMAT
#00019677410D F46 WMCJT SUPONNA          NFN         KK08747E 20060918 687113695 20200928                  09 01 09  
       # Strings for excel placement
       caseNo = line[0:12] #A, 0
       office = line[13:16] #B, 1
       worker = line[17:23] #C, 2
       name = line[23:51] #D, 3
       cin = line[52:59] #E, 4
       dob = dateFormat(line[61:69]) #F, 5
       ssn = line[70:79] #G, 6
       appDate = dateFormat(line[80:88]) #H, 7
       ###regDate = line[89:95] # ignore
       caseStatus = "01" #I, 8

       formatInfo = ssn, cin, caseNo, office, worker, appDate, name, dob, caseStatus
       ssnInfo = cin, caseNo, office, worker, appDate, name, dob, caseStatus
       if(ssn != "         "):
              lineList.append(formatInfo)
              ssnList.append(ssnInfo)
              if (ssn not in ssnDict.keys()):
                  ssnDict[ssn] = ssnList
              else: #This is to catch duplicates 
                  ssnDict[ssn].append(ssnInfo)
       ssnList = []

#print("Duplicates: ", dupeSSN)
print("SSN Dict Keys: ", len(ssnDict.keys()))
print("SSN Dict Vals: ", len(ssnDict.values()))

tWP = open(txtFP,'w+')
tWP.write("C:\\Users\\tseguia\\Desktop\\INCIDENTS\\lqsnap2\\" + str(time()) + ".txt\n")
tWP.write("01-060-CASE-TYPE OF CASE-LINK (CASE-TYPE) \"31\"\n")
tWP.write("Total APPs reviewed: " + str(len(ssnDict.keys())) + "\n")
tWP.write("\n")
printCount = 1

count = 2 
for i in ssnDict.keys():
    #This takes SSN
    #This writes on text file/excel sheet
    if (len(ssnDict[i]) > 1):
        dupeSSN += 1
        #print(str(printCount), i, ssnDict[i])
        #write ssn to text file and excel sheet first
        excelLen = 0
        while (excelLen < len(ssnDict[i])):
            dupeApp += 1
            excelString = str(count)

            # For Column Placement
            ssnColumn = "A" + excelString
            cinColumn = "B" + excelString
            caseNoColumn = "C" + excelString
            centerColumn = "D" + excelString
            workerColumn = "E" + excelString
            appDateColumn = "F" + excelString
            nameColumn = "G" + excelString
            dobColumn = "H" + excelString
            caseStatusColumn = "I" + excelString
            
            if (excelLen == 0):
                worksheet.write(ssnColumn, i)

            worksheet.write(cinColumn, ssnDict[i][excelLen][0])
            worksheet.write(caseNoColumn,ssnDict[i][excelLen][1])
            worksheet.write(centerColumn,ssnDict[i][excelLen][2])
            worksheet.write(workerColumn,ssnDict[i][excelLen][3])
            worksheet.write(appDateColumn,ssnDict[i][excelLen][4])
            worksheet.write(nameColumn,ssnDict[i][excelLen][5])
            worksheet.write(dobColumn,ssnDict[i][excelLen][6])
            worksheet.write(caseStatusColumn,ssnDict[i][excelLen][7])
            excelLen += 1
            count += 1

        tWP.write(str(printCount) +" "+ i + ": "+"\n")
        j = 0
        while j < len(ssnDict[i]):
            #print(ssnDict[i][j])
            #j is the list
            #cin, caseNo, office, worker, name, dob, caseStatus
            k = 0
            #this iterates thru list items
            while k < len(ssnDict[i][j]):
                if k < 6:
                    tWP.write(ssnDict[i][j][k] + ", ")
                else: 
                    tWP.write(ssnDict[i][j][k])
                k += 1 
            tWP.write("\n")
            j += 1
        
        printCount += 1

tWP.write("\n")
print("Duplicate SSNs: ", dupeSSN)
tWP.write("Duplicate SSNs: " + str(dupeSSN) + "\n")
print("Duplicate APPs: ", dupeApp)
tWP.write("Duplicate APPs: " + str(dupeApp) + "\n")
workbook.close()
tWP.close()
print("Information Written to:\n", excelFP, "\n" ,txtFP)
#python lqsnap2.py