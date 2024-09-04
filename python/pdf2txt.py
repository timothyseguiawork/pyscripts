#C:\Users\tseguia\Desktop\INCIDENTS\INC3873667recs
#Python Program used to create an excel sheet for SSI Calendarp-\
#Need to replace spaces with replace "-" for scheduled-run
#Created by Timothy Seguia, 01/04/2022
from pathlib import Path
import datetime
import xlsxwriter

def populateList(monList):
    count = 0
    fileNameList = []
    for items in monList:
        for index in monList[count]:
            if "RECONCILIATION" in index:
                continue
            if "*" in index or "RECON" in index:
                fileNameList.append(index)
        count += 1
    return fileNameList

def createMonDict(monList):
    count = 0
    tempDate = ""
    tempFileName = ""
    fileDict = {}
    for listItem in monList:
        # count = 0
        for index in monList[count]:
            if "/" in index and "0" in index:
                # print(index)
                tempDate = index
            if "*" in index or "RECON" in index or "COLA" or "TREAS**" in index:
                # print(index)
                tempFileName = index
            if tempDate != "" and tempFileName != "":
                fileDict.update({tempDate:tempFileName})
        count += 1
        tempDate = ""
        tempFileName = ""
        
    return fileDict

def createFP(workbookFP, text):
    tempWorkbookFP = workbookFP + text + ".xlsx" 
    return tempWorkbookFP

def createBook(workbookFP, monthOne, monthTwo, monthThr, monListPartOne, monListPartTwo, monListPartThr):
    workbook = xlsxwriter.Workbook(workbookFP)
    worksheet1 = workbook.add_worksheet(monthOne)
    worksheet2 = workbook.add_worksheet(monthTwo)
    worksheet3 = workbook.add_worksheet(monthThr)
    createSheet(monListPartOne, workbook, worksheet1)
    createSheet(monListPartTwo, workbook, worksheet2)
    createSheet(monListPartThr, workbook, worksheet3)
    workbook.close()

#CREATE A GLOBAL VARIABLE COUNT
count = 0
def createSheet(monList, workbook, worksheet):
    worksheet.set_column('A:A', 20) #merge file
    worksheet.set_column('B:B', 20) #merge count
    worksheet.set_column('C:C', 20) #merge date
    worksheet.set_column('D:D', 15) #File
    worksheet.set_column('E:E', 20) #PSDXA0 Name
    worksheet.set_column('F:F', 10) #DoF
    worksheet.set_column('G:G', 10) #Proc
    worksheet.set_column('H:H', 10) #Drop
    worksheet.set_column('I:I', 20) #Counts
    worksheet.set_column('J:J', 20) #events

    # Add a BOLD format to use to highlight cells.
    bold = workbook.add_format({'bold': True})

    # Write Column Headers.
    worksheet.write('A1', 'MERGE-FILE', bold)
    worksheet.write('B1', 'MERGE-COUNT', bold)
    worksheet.write('C1', 'MERGE-DATE', bold)
    worksheet.write('D1', 'FILE', bold)
    worksheet.write('E1', 'PSDXA Name', bold)
    worksheet.write('F1', 'DoF', bold)
    worksheet.write('G1', 'Proc', bold)
    worksheet.write('H1', 'Drop', bold)
    worksheet.write('I1', 'Counts', bold)
    worksheet.write('J1', 'Events', bold)

    excelCount = 2
    # for lineList in monList: 
    #     fileColumn = "D" + str(excelCount)
    #     worksheet.write(fileColumn,lineList)
    #     excelCount += 1

    # for item in monDict: 
    #     fileColumn = "D" + str(excelCount)
    #     worksheet.write(fileColumn,monDict.get(item))
    #     dofColumn = "F" + str(excelCount)
    #     worksheet.write(dofColumn,item)
    #     psdxaColumn= "E" + str(excelCount)
    #     if "RECON" in monDict.get(item):
    #         tempPSDXAName = monDict.get(item)[0:2] + monDict.get(item)[2:4] + "RECN"
    #     else: 
    #         tempPSDXAName = "PSDXA0" + monDict.get(item)[2:4] + monDict.get(item)[0:2] + monDict.get(item)[6] + monDict.get(item)[4]
    #     worksheet.write(psdxaColumn,tempPSDXAName)
    #     excelCount += 1

    for item in monList: 
        if len(item) == 4:
            fileDate = item[2]
            fileName = item[3]
            if "TREAS" in fileName: 
                psdxa0yymmu = "PSDXA0" + item[3][2:4] + item[3][0:2] + "TR"
            else: 
                psdxa0yymmu = "PSDXA0" + item[3][2:4] + item[3][0:2] + item[3][6] + "U"
            fileColumn = "D" + str(excelCount)
            worksheet.write(fileColumn,fileName)
            dofColumn = "F" + str(excelCount)
            worksheet.write(dofColumn,fileDate)
            psdxaColumn= "E" + str(excelCount)
            worksheet.write(psdxaColumn,psdxa0yymmu)
            excelCount += 1

#C:\\Users\\tseguia\\Documents\\SSI CALENDAR\\firstquarter2021

# C:\Users\tseguia\OneDrive - New York State Office of Information Technology Services\Documents\SSI CALENDAR\2022\secquarter2022
cDrive = "C:\\Users\\tseguia\\OneDrive - New York State Office of Information Technology Services\\Documents\\SSI CALENDAR\\2024\\3rd_Quarter_2024\\" #CHANGE WITH EACH QUARTER #CHANGE

textFile = "3rd_Quarter_2024" #CHANGE WITH EACH QUARTER #CHANGE
txtFilePath = cDrive + textFile + ".txt"
workbookFP = createFP(cDrive, textFile)

year = "2024" #CHANGE WITH YEAR #CHANGE

monList = ["JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"]
monDate = ["01/", "02/", "03/", "04/", "05/", "06/", "07/", "08/", "09/", "10/", "11/", "12/"]

lineList = []
workMonList = []

monthCount = 0

monthOne = ""
monthTwo = ""
monthThr = ""

monListPartOne = []
monListPartTwo = []
monListPartThr = []

with open(txtFilePath) as fP:
    for line in fP:
        lineList = line.split()
        for month in monList:
            if month in lineList and year in lineList:
                if lineList[0] not in workMonList:
                    workMonList.append(lineList[0])
                    monthCount += 1
        if monthCount == 1:
            monListPartOne.append(lineList)
        if monthCount == 2:
            monListPartTwo.append(lineList)
        if monthCount == 3:
            monListPartThr.append(lineList)

# print(monListPartOne)
for i in monListPartOne:
    if len(i) == 4:
        if "*" in i[3]:
            fileDate = i[2]
            fileName = i[3]
            psdxa0yymmu = "PSDXA0" + i[3][2:4] + i[3][0:2] + "U"
            print(fileDate)
            print(fileName)
            print(psdxa0yymmu)

# fileDictOne = createMonDict(monListPartOne)
# fileDictTwo = createMonDict(monListPartTwo)
# fileDictThr = createMonDict(monListPartThr)

 # print (fileDictOne)
    


monthOne = workMonList[0]
monthTwo = workMonList[1]
monthThr = workMonList[2]


createBook(workbookFP, monthOne, monthTwo, monthThr, monListPartOne, monListPartTwo, monListPartThr)

