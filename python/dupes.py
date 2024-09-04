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
filePath = "W:\\wms\\dupes"
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
workbook = xlsxwriter.Workbook("C:\\Users\\tseguia\\Desktop\\INCIDENTS\\tony\\07232020.xlsx")
worksheet = workbook.add_worksheet()

# Widen the first column to make the text clearer.
# ignore ssn
worksheet.set_column('A:A', 30)
worksheet.set_column('B:B', 30)
worksheet.set_column('C:C', 30)
worksheet.set_column('D:D', 30)
worksheet.set_column('E:E', 30)

# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': True})

# Write some simple text.
worksheet.write('A1', 'CIN', bold)
worksheet.write('B1', 'Case Number', bold)
worksheet.write('C1', 'Case Type', bold)
worksheet.write('D1', 'Individual Status', bold)
worksheet.write('E1', 'Transaction Date', bold)

caseDict = {}
with open(filePath) as fP:
    for line in fP:
        # For Column Placement
        excelString = str(count)
        cinColumn = "A" + excelString 
        caseNoColumn = "B" + excelString
        caseTypeColumn = "C" + excelString
        indStatColumn = "D" + excelString
        txDateColumn = "E" + excelString
        # Strings for excel placement
        cin = line[0:8] #A
        #ssn = line[9:19]
        caseNo = line[20:31] #B
        caseType = line[32:34] #C
        indStat = line[35:37] #D
        txDate = line[38:46] #E
        #print (dateFormat(txDate))
        print (cin + " " + caseNo + " " + caseType + " " + indStat + " " + txDate)
        if cin not in caseDict and caseType == "22":
            caseDict[cin] = []
            worksheet.write(cinColumn,cin)
            if caseNo not in caseDict[cin]:
                caseDict[cin].append(caseNo)
                #worksheet.write(cinColumn,cin)
                worksheet.write(caseNoColumn,caseNo)
                worksheet.write(caseTypeColumn,caseType)
                worksheet.write(indStatColumn,indStat)
                worksheet.write(txDateColumn,dateFormat(txDate))
            count += 1  
        #elif caseNo not in caseDict[cin]:
        #    caseDict[cin].append(caseNo)
        #    worksheet.write(caseNoColumn,caseNo)
        #    worksheet.write(caseTypeColumn,caseType)
        #    worksheet.write(indStatColumn,indStat)
        #    worksheet.write(txDateColumn,dateFormat(txDate))    
            #worksheet.write(caseColumn,caseNumber)
          
        
for i in caseDict:
    print (i + str(caseDict[i]))

workbook.close()
