#C:\Users\tseguia\Desktop\INCIDENTS\INC3873667recs
#Python Program used to put case numbers and CINs in an excel sheet
#Created by Timothy Seguia, 02/05/20
from pathlib import Path
import datetime
import xlsxwriter

#CREATE A GLOBAL VARIABLE COUNT
count = 2

def newLine():
    print()
    
def horiLine():
    print("--------------------------------------")
    
def time():
    return datetime.datetime.now()

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
        
#filePath = "C:\\Users\\tseguia\\Desktop\\INCIDENTS\\INC3873667recs\\caselist"
#filePath = "C:\\Users\\tseguia\\Desktop\\INCIDENTS\\INC3825277records\\caselist"
#W:\
filePath = "W:\\csprodny\\wdcasesp"
cin = ""
ssn = ""
caseNo = ""
indStat = ""

# Create an new Excel file and add a worksheet.
#C:\\Users\\tseguia\\Desktop\\INCIDENTS\\INC3873667recs
#"C:\\Users\\tseguia\\Desktop\\INCIDENTS\\INC3825277records\\caselist"
#"C:\\Users\\tseguia\\Desktop\\INCIDENTS\\DOH2503\\aurora.xlsx"
#"C:\\Users\\tseguia\\Desktop\\INCIDENTS\\INC3718432\\INC3718432.xlsx"
#"C:\\Users\\tseguia\\Desktop\\INCIDENTS\\INC3718432\\INC3718432tonycopy.xlsx"
workbook = xlsxwriter.Workbook("C:\\Users\\tseguia\\Desktop\\INCIDENTS\\WDCASESP\\07232020.xlsx")
worksheet = workbook.add_worksheet()


#PRINT 01-052-CASE-NO OF CASE                                              &
#     1-01-020-LOCAL-OFFICE OF CASE                                       &
#     1-01-040-RESP-WORKER OF CASE                                        &
#     1-02-090-CASE-STATUS OF SUFFIX                                      &
#     2-02-090-CASE-STATUS OF SUFFIX                                      &
#     3-02-090-CASE-STATUS OF SUFFIX                                      &
#     01-090-APPLCTN-DATE-Y2K OF SUFFIX                                   &
#     01-048-APP-REG-DATE-Y2K OF SUFFIX                                   &
#     03-010-RECIP-ID OF CLIENT-LINK                                      &

# Widen the first column to make the text clearer.
# ignore ssn
worksheet.set_column('A:A', 30)
worksheet.set_column('B:B', 30)
worksheet.set_column('C:C', 30)
worksheet.set_column('D:D', 30)
worksheet.set_column('E:E', 30)
worksheet.set_column('F:F', 30)
worksheet.set_column('G:G', 30)
worksheet.set_column('H:H', 30)
worksheet.set_column('I:I', 30)

# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': True})

# Write some simple text.
worksheet.write('A1', 'Case Number', bold)
worksheet.write('B1', 'Local Office', bold)
worksheet.write('C1', 'Worker Response', bold)
worksheet.write('D1', 'PA Case Status', bold)
worksheet.write('E1', 'FS Case Status', bold)
worksheet.write('F1', 'MA Case Status', bold)
worksheet.write('G1', 'Application Date', bold)
worksheet.write('H1', 'Application Register Date', bold)
worksheet.write('I1', 'CIN', bold)

caseDict = {}
lineList = []
printCount = 1

with open(filePath) as fP:
    
    for line in fP:
        # For Column Placement
        excelString = str(count)
        caseNoColumn = "A" + excelString
        officeColumn = "B" + excelString
        workerColumn = "C" + excelString
        casePAColumn = "D" + excelString
        caseFSColumn = "E" + excelString
        caseMAColumn = "F" + excelString
        appDateColumn = "G" + excelString
        regDateColumn = "H" + excelString
        cinColumn = "I" + excelString

# A, caseNo
# B, office
# C, worker
# D, casePA
# E, caseFS
# F, caseMA
# G, appDate
# H, regDate
# I, CIN 

# FILE FORMAT
#00024446950I 500 SDX   09 09 01 20190630 20200625 VK69190X  
#00024446950I 500 SDX 09 09 01 20190630 20200625 VK69190X
#py wdcasesp.py
#00024228120C 500 SDX  9
        # Strings for excel placement
        caseNo = line[0:12] #A
        office = line[13:16] #B
        worker = line[17:20] #C
        casePA = line[23:25] #D
        caseFS = line[26:28] #E
        caseMA = line[29:31] #F
        appDate = dateFormat(line[32:40]) #G
        regDate = dateFormat(line[41:49]) #H
        cin = line[50:58] #I
        #print (dateFormat(txDate))
        formatInfo = caseNo, office, worker, casePA, caseFS, caseMA, appDate, regDate, cin
        lineList.append(formatInfo)
        #print (caseNo, office, worker, casePA, caseFS, caseMA, appDate, regDate, cin)
        
        #worksheet.write(cinColumn,cin)
        #caseNo, office, worker, casePA, caseFS, caseMA, appDate, regDate, cin
        worksheet.write(caseNoColumn,caseNo)
        worksheet.write(officeColumn,office)
        worksheet.write(workerColumn,worker)
        worksheet.write(casePAColumn,casePA)
        worksheet.write(caseFSColumn,caseFS)
        worksheet.write(caseMAColumn,caseMA)
        worksheet.write(appDateColumn,appDate)
        worksheet.write(regDateColumn,regDate)
        worksheet.write(cinColumn,cin)

        count += 1
        
#for i in caseDict:
#    print (i + str(caseDict[i]))
for i in lineList: 
            print(printCount,"# Writing to excel sheet: ", i)
            printCount += 1
workbook.close()
