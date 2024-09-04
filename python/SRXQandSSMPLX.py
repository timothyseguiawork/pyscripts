#Python Program for calculating distribution list for cins and transactions
#Created by Timothy Seguia, 11/13/19
from pathlib import Path
import datetime
import xlsxwriter


def newLine():
    print()
def horiLine():
    print("____________________________________")
def time():
    return datetime.datetime.now()

filePath = "C:\\Users\\tseguia\\Documents\\SRXQ.txt"
progName = ""
parenthesisIndex = 0
printerString = ""
fileName = ""

# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook('C:\\Users\\tseguia\\Documents\\sdxprintedreports.xlsx')
worksheet = workbook.add_worksheet()

# Widen the first column to make the text clearer.
worksheet.set_column('A:A', 40)
worksheet.set_column('B:B', 40)
worksheet.set_column('C:C', 40)
worksheet.set_column('D:D', 40)

# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': True})

# Write some simple text.
worksheet.write('A1', 'ECL/Job', bold)
worksheet.write('B1', 'Filename', bold)
worksheet.write('C1', 'Report Name', bold)
worksheet.write('D1', 'Printer', bold)
excelCount = 1
excelString = ""

# USE FIND
with open(filePath) as fP:
    for line in fP:
        #fileName = line[0:20]
        #progName = line[14:20]
        #parenthesisIndex = line.find(")") + 2
        #printerString = line[parenthesisIndex:]
        #print(fileName + " " + progName + " " + printerString[0:5])
        if ("@SYM" in line):
            #print(fileName + " " + progName + " " + eclStatement)
            #print(line)
            if ("psdx" in line) and ("@ . " not in line):
                jobName = line[14:20]
                #print(line)
                stripLine = line.strip()
                stripLine = stripLine.replace(" ","")
                endParenthesis = stripLine.find(")")
                #print(endParenthesis)
                #print(stripLine)
                #print(stripLine[endParenthesis:32])
                endParenthesisNum = stripLine.find("U") + 1
                #print(stripLine.find("U"))
                endFileNameNum = stripLine.find(".")
                print(endFileNameNum)
                print(stripLine[endParenthesisNum:])
                

                if ("SRXQ" in line):
                    excelCount += 1
                    #print("line " + line[(endFileNameNum +11):])
                    reportName = line[(endFileNameNum +11):]
                    
                    excelCountString = str(excelCount)
                    jobCountString = "A" + excelCountString
                    fileCountString = "B" + excelCountString
                    reportNameString = "C" + excelCountString
                    printerCountString = "D" + excelCountString
                    print(excelCountString)
                    
                    print(jobCountString + " Job: " + jobName)
                    print(fileCountString + " File Name: "+ stripLine[endParenthesisNum:endFileNameNum])
                    print(reportNameString + " Report Name: " + reportName)
                    print(printerCountString + " Printer Name: SRXQ")

                    worksheet.write(jobCountString,jobName)
                    worksheet.write(fileCountString,stripLine[endParenthesisNum:endFileNameNum])
                    worksheet.write(reportNameString,reportName)
                    worksheet.write(printerCountString,"SRXQ")
                    
                    horiLine()
                    
                elif ("SSMPLX" in line):
                    excelCount += 1
                    #print("line " + line[(endFileNameNum +13):])
                    reportName = line[(endFileNameNum +13):]
                    
                    excelCountString = str(excelCount)
                    jobCountString = "A" + excelCountString
                    fileCountString = "B" + excelCountString
                    reportNameString = "C" + excelCountString
                    printerCountString = "D" + excelCountString
                    print(excelCountString)
                    
                    print(jobCountString + " Job: " + jobName)
                    print(fileCountString + " File Name: "+ stripLine[endParenthesisNum:endFileNameNum])
                    print(reportNameString + " Report Name: " + reportName)
                    print(printerCountString + " Printer Name: SSMPLX")
                   
                    worksheet.write(jobCountString,jobName)
                    worksheet.write(fileCountString,stripLine[endParenthesisNum:endFileNameNum])
                    worksheet.write(reportNameString,reportName)
                    worksheet.write(printerCountString,"SSMPLX")
                    
                    horiLine()    
                elif ("SSTOCK" in line):
                    excelCount += 1
                    
                    #print("line " + line[(endFileNameNum +11):])
                    reportName = line[(endFileNameNum +13):]
                    
                    excelCountString = str(excelCount)
                    jobCountString = "A" + excelCountString
                    fileCountString = "B" + excelCountString
                    reportNameString = "C" + excelCountString
                    printerCountString = "D" + excelCountString
                    print(excelCountString)
                    
                    print(jobCountString + " Job: " + jobName)
                    print(fileCountString + " File Name: "+ stripLine[endParenthesisNum:endFileNameNum])
                    print(reportNameString + " Report Name: " + reportName)
                    print(printerCountString + " Printer Name: SSTOCK")


                    worksheet.write(jobCountString,jobName)
                    worksheet.write(fileCountString,stripLine[endParenthesisNum:endFileNameNum])
                    worksheet.write(reportNameString,reportName)
                    worksheet.write(printerCountString,"SSTOCK")
                    
                    horiLine()
workbook.close()
