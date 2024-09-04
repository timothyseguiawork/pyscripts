#C:\Users\tseguia\Desktop\INCIDENTS\INC3873667recs
#Python Program used to create an excel sheet for SSI Calendar
#Need to replace spaces with replace "-" for scheduled-run
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

def partOne(monList, workbookFP, month, year):
    createExcel(monList, workbookFP, month, year)

def partTwo(monList, workbookFP, month, year):
    createExcel(monList, workbookFP, month, year)

def partThree(monList, workbookFP, month, year):
    createExcel(monList, workbookFP, month, year)

def createExcel(monList, workbookFP, month, year):
    workbook = xlsxwriter.Workbook(workbookFP)
    worksheet = workbook.add_worksheet()

    worksheet.set_column('A:A', 13) #Merge File
    worksheet.set_column('B:B', 13) #Merge Date
    worksheet.set_column('C:C', 40) #Scheduled Run
    worksheet.set_column('D:D', 15) #Run Number
    worksheet.set_column('E:E', 11) #Date
    worksheet.set_column('F:F', 15) #File
    worksheet.set_column('G:G', 6) #DoF
    worksheet.set_column('H:H', 6) #Proc
    worksheet.set_column('I:I', 6) #Drop

    # Add a BOLD format to use to highlight cells.
    bold = workbook.add_format({'bold': True})

    # Write Column Headers.
    worksheet.write('A1', 'MERGE-FILE', bold)
    worksheet.write('B1', 'MERGE-DATE', bold)
    worksheet.write('C1', 'SCHEDULED-RUN', bold)
    worksheet.write('D1', 'RUN-NUMBER', bold)
    worksheet.write('E1', 'DATE(JUL)', bold)
    worksheet.write('F1', 'FILE', bold)
    worksheet.write('G1', 'DoF', bold)
    worksheet.write('H1', 'Proc', bold)
    worksheet.write('I1', 'Drop', bold)

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
    workbook.close()

#C:\\Users\\tseguia\\Documents\\SSI CALENDAR\\firstquarter2020
filePath = "C:\\Users\\tseguia\\Documents\\SSI CALENDAR\\4thquarter2020\\4thquarter2020.txt" #CHANGE WITH EACH QUARTER #CHANGE

workbookFP = "C:\\Users\\tseguia\\Documents\\SSI CALENDAR\\4thquarter2020\\" #CHANGE WITH EACH QUARTER #CHANGE

year = "2020" #CHANGE WITH YEAR #CHANGE

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

with open(filePath) as fP:
    for line in fP:
        lineList = line.split()
        if printCount == 165:  #CHANGE TO END OF FILE #CHANGE
            break
        if not lineList:
            continue
        if lineList[0] in monList:
            monthCount += 1
            workMonList.append(lineList[0])
        if monthCount == 4:
            monListPartOne.append(lineList)
        if monthCount == 5:
            monListPartTwo.append(lineList)
        if monthCount == 6:
            monListPartThr.append(lineList)
        #print(lineList) #PEEP LISTS
        printCount += 1
#print(workMonList) #PEEP MONTH

monthOne = workMonList[0]
monthTwo = workMonList[1]
monthThr = workMonList[2]

workbookFP1 = workbookFP + monthOne + year + ".xlsx" 
workbookFP2 = workbookFP + monthTwo + year + ".xlsx"
workbookFP3 = workbookFP + monthThr + year + ".xlsx"

print (workbookFP1)
print (workbookFP2)
print (workbookFP3)

#PART ONE
partOne(monListPartOne, workbookFP1,monthOne, year)

#PART TWO
partTwo(monListPartTwo, workbookFP2, monthTwo, year)

#PART THREE
partThree(monListPartThr, workbookFP3, monthThr, year)