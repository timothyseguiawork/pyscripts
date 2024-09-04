#C:\Users\tseguia\Desktop\INCIDENTS\INC3873667recs
#Python Program used to create an excel sheet for SSI Calendar
#Need to replace spaces with replace "-" for scheduled-run
#Created by Timothy Seguia, 01/04/2022
from pathlib import Path
import datetime
import xlsxwriter

#CREATE A GLOBAL VARIABLE COUNT
count = 0

def horiLine():
    print("--------------------------------------")
    
def time():
    return datetime.datetime.now()

def getList(monList): 
    return monList

def createBook(workbookFP, monthOne, monthTwo, monthThr, monListPartOne, monListPartTwo, monListPartThr):
    workbook = xlsxwriter.Workbook(workbookFP)
    worksheet1 = workbook.add_worksheet(monthOne)
    worksheet2 = workbook.add_worksheet(monthTwo)
    worksheet3 = workbook.add_worksheet(monthThr)
    createSheet(worksheet1, workbook, monListPartOne)
    createSheet(worksheet2, workbook, monListPartTwo)
    createSheet(worksheet3, workbook, monListPartThr)
    workbook.close()

def createSheet(worksheet, workbook, monList):

    worksheet.set_column('A:A', 15) #Merge File
    worksheet.set_column('B:B', 15) #Merge Count
    worksheet.set_column('C:C', 40) #Scheduled Run
    worksheet.set_column('D:D', 15) #Run Number
    worksheet.set_column('E:E', 11) #Date
    worksheet.set_column('F:F', 15) #File
    worksheet.set_column('G:G', 10) #DoF
    worksheet.set_column('H:H', 10) #Proc
    worksheet.set_column('I:I', 10) #Drop
    worksheet.set_column('J:J', 20) #Counts

    # Add a BOLD format to use to highlight cells.
    bold = workbook.add_format({'bold': True})

    # Write Column Headers.
    worksheet.write('A1', 'MERGE-FILE', bold)
    worksheet.write('B1', 'MERGE-COUNT', bold)
    worksheet.write('C1', 'SCHEDULED-RUN', bold)
    worksheet.write('D1', 'RUN-NUMBER', bold)
    worksheet.write('E1', 'DATE(JUL)', bold)
    worksheet.write('F1', 'FILE', bold)
    worksheet.write('G1', 'DoF', bold)
    worksheet.write('H1', 'Proc', bold)
    worksheet.write('I1', 'Drop', bold)
    worksheet.write('J1', 'Counts', bold)

    count = 0
    for lineList in monList: 
        excelCount = str(count)
        #sorting out lists
        #if 2 SCHEDULED-RUN + DATE(JUL)
        #if 3 SCHEDULED-RUN + RUN-NUMBER + DATE(JUL)
        #if 4 SCHEDULED-RUN + RUN-NUMBER + DATE(JUL) + FILE

        schedColumn = "C" + excelCount
        runColumn = "D" + excelCount
        dateColumn = "E" + excelCount
        fileColumn = "F" + excelCount

        #skip first 2 lines
        if count >= 2: 
            if len(lineList) == 2:
                worksheet.write(schedColumn,lineList[0])
                worksheet.write(dateColumn,lineList[1])
            if len(lineList) == 3:
                worksheet.write(schedColumn,lineList[0])
                worksheet.write(runColumn,lineList[1])
                worksheet.write(dateColumn,lineList[2])
            if len(lineList) == 4: 
                worksheet.write(schedColumn,lineList[0])
                worksheet.write(runColumn,lineList[1])
                worksheet.write(dateColumn,lineList[2])
                worksheet.write(fileColumn,lineList[3])
        count += 1

def sortList (sortList): 
    return sortList

#C:\\Users\\tseguia\\Documents\\SSI CALENDAR\\firstquarter2021

# C:\Users\tseguia\OneDrive - New York State Office of Information Technology Services\Documents\SSI CALENDAR\2022\secquarter2022
cDrive = "C:\\Users\\tseguia\\OneDrive - New York State Office of Information Technology Services\\Documents\\SSI CALENDAR\\2024\\" #CHANGE WITH EACH QUARTER #CHANGE
folder = "3rd_Quarter_2024\\"
textFile = "3rd_Quarter_2024" #CHANGE WITH EACH QUARTER #CHANGE


txtFilePath = cDrive + folder + textFile + ".txt"
workbookFP = cDrive + folder

year = "2024" #CHANGE WITH YEAR #CHANGE

monList = ["JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"]

lineList = []
printCount = 0
monthCount = 0
writeCount = 2

workMonList = []

monthOne = ""
monthTwo = ""
monthThr = ""

monListPartOne = []
monListPartTwo = []
monListPartThr = []

monthCount = 0

with open(txtFilePath) as fP:
    for line in fP:
        lineList = line.split()
        if len(lineList) == 2 and lineList[0] in monList and lineList[0] not in workMonList:
            workMonList.append(lineList[0])
            monthCount += 1 
        if monthCount == 1:
            monListPartOne.append(lineList) # this chooses month list to add 
        if monthCount == 2:
            monListPartTwo.append(lineList)
        if monthCount == 3: 
            monListPartThr.append(lineList)
        
#print(workMonList)

monthOne = workMonList[0]
monthTwo = workMonList[1]
monthThr = workMonList[2]


for i in monListPartOne:
    print (i)

#for i in monListPartTwo:
#   print (i)

#for i in monListPartThr:
#   print (i)

workbookFP = workbookFP + textFile + ".xlsx" 
createBook(workbookFP, monthOne, monthTwo, monthThr, monListPartOne, monListPartTwo, monListPartThr)

#PART ONE
# partOne(monListPartOne, workbookFP1, monthOne, year)

#PART TWO
# partTwo(monListPartTwo, workbookFP2, monthTwo, year)

#PART THREE
# partThree(monListPartThr, workbookFP3, monthThr, year)
