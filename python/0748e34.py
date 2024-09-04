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
filePath = "C:\\Users\\tseguia\\Documents\\0748\\04132020"
caseFilePath = "C:\\Users\\tseguia\\Documents\\0748\\03162020edit"


caseNumber = ""
#make sure current date matches yymmdd
#if you were to do 02/04/2020 = 200204
#currentDate = "200203"
procDate = ""
fileReadFlag = "SHAUNA"
#fileReadFlag = "KRINTIN"

# USE FIND
# 1275514:00019047130A2002032220980010191910030227060107000200010003000120034*SDN*04F15 132023501E0748
# 0-12, case#
# SHAUNA
# this is for 0748cases
if fileReadFlag == "SHAUNA":
    shauna(filePath)
    
# KRINTIN
# this is for krintin
if fileReadFlag == "KRINTIN":
    krintin(caseFilePath)

excelCount = 1
excelString = ""


# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook('C:\\Users\\tseguia\\Documents\\0748\\04132020.xlsx')
worksheet = workbook.add_worksheet()

# Widen the first column to make the text clearer.
worksheet.set_column('A:A', 30)
worksheet.set_column('B:B', 30)
worksheet.set_column('C:C', 30)
worksheet.set_column('D:D', 30)
worksheet.set_column('E:E', 30)

# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': True})

# Write some simple text.
worksheet.write('A1', 'Case Number', bold)
worksheet.write('B1', 'File Date', bold)
worksheet.write('C1', 'Processed Date', bold)
worksheet.write('D1', 'Batch', bold)
worksheet.write('E1', 'Error#', bold)

with open(filePath) as fP:
    for line in fP:
        #batchNumber = line[75:80]
        batchNumber = "*SDN*"
        errorNum = "0748"
        #if batchNumber == "*SDN*":
        if "*SDN*" in line:
            #printInfo(line)
            excelCount = excelCount + 1
            caseNumber = line[10:20]
            fileDate = line[20:26]
            procDate = line[38:44]
            #errorNum = line[95:]
            excelString = str(excelCount)
            print(excelString)
            caseColumn = "A" + excelString
            fileDateColumn = "B" + excelString
            procDateColumn = "C" + excelString
            batchColumn = "D" + excelString
            errorColumn = "E" + excelString
            print(caseColumn + " " + caseNumber + " " + 
                  fileDateColumn + " " + dateFormat(fileDate) + " " +
                  procDateColumn + " " + dateFormat(procDate) + " " +
                  batchColumn + " " + batchNumber + " " +
                  errorColumn + " "  + errorNum)
            worksheet.write(caseColumn,caseNumber)
            worksheet.write(fileDateColumn,dateFormat(fileDate))
            worksheet.write(procDateColumn,dateFormat(procDate))
            worksheet.write(batchColumn,batchNumber)
            worksheet.write(errorColumn,errorNum)
# Text with formatting.
#worksheet.write('A2', 'World', bold)

# Write some numbers, with row/column notation.
#worksheet.write(2, 0, 123)
#worksheet.write(3, 0, 123.456)

# Insert an image.
#worksheet.insert_image('B5', 'logo.png')

workbook.close()

