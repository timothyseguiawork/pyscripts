#C:\Users\tseguia\Desktop\INCIDENTS\INC3873667recs
#Python Program used to create an excel sheet for SSI Calendarp-\
#Need to replace spaces with replace "-" for scheduled-run
#Created by Timothy Seguia, 01/04/2022
from pathlib import Path
import datetime
import xlsxwriter

#CREATE A GLOBAL VARIABLE COUNT
count = 0

#C:\\Users\\tseguia\\Documents\\SSI CALENDAR\\firstquarter2021

# C:\Users\tseguia\OneDrive - New York State Office of Information Technology Services\Documents\SSI CALENDAR\2022\secquarter2022
cDrive = "C:\\Users\\tseguia\\OneDrive - New York State Office of Information Technology Services\\desktop\\" #CHANGE WITH EACH QUARTER #CHANGE

textFile = "pcprgen" #pcpr gen for ECL
# textFile = "filegen"
txtFilePath = cDrive + textFile + ".txt"
workbookFP = cDrive 

notCataloguedFile = "new 10"
notCataloguedFilePath = cDrive + notCataloguedFile + ".txt"

needsCatalogue = "new 11"
needsCataloguePath = cDrive + needsCatalogue + ".txt"

dateCheck ="052324"
dateCheckPath = cDrive + dateCheck + ".txt"

pullPR = cDrive + "cDriveGen.txt"

lineList = []
notCataloguedFileList = []
cataloguedFileList = []
dateCheckList = []

fullString = ""
count = 0
with open(pullPR) as fP:
    for line in fP: 
        line = line.replace("\n","")
        line = line.replace("/P","")
        line = line.replace(","," ")
        line = line.split(" ")
        lineList.append(line)

# print(lineList[0][1][2:])
# print(int(lineList[0][1][2:]))
# grab 1140, 1260, 1470, 1550 for the first jobs
numberList = [] 
for i in lineList:
    # print(i[1])
    if int(i[1][2:]) == 1140 or int(i[1][2:]) == 1260 or int(i[1][2:]) == 1470 or int(i[1][2:]) == 1550:
         numberList.append(i[1])
         lineList.remove(i)

count = 0
temp = int(lineList[count][1][2:])
next = 1
tempObj = lineList[count][1]
#print(lineList[count][1][2:])

for i in lineList:
    if next >= len(lineList):
        break
    else: 
        if temp < int(lineList[next][1][2:6]):
            numberList.append(tempObj)
            temp = int(lineList[next][1][2:6])
            tempObj = lineList[next][1]
        else:
            numberList.append(lineList[count][1])
    
    # if next > len(lineList):
    #     break 
    
    # print(int(lineList[count][1][2:]))
    # if int(lineList[count][1][2:]) > temp:
    #     temp = int(lineList[count][1][2:])
    #     tempObj = lineList[count][1]
    #     #print(tempObj)

    # if temp < int(lineList[next][1][2:]):
    #     numberList.append(tempObj)
    #     temp = lineList[count][1][2:]
    #     tempObj = lineList[count][1]
    #     # print(tempObj)
    # else:
    #     numberList.append(lineList[count][1])

    count += 1
    next = count + 1

print(numberList)

for i in numberList: 
    print(i)

# with open(notCataloguedFilePath) as fP:
#     for line in fP:
#         line = line.replace("[","")
#         line = line.replace("]","")
#         line = line.replace("\'","")
#         line = line.replace(","," ")
#         line = line.replace("\n","")
#         #print(line.split("  "))
#         line = line.split("  ")
#         notCataloguedFileList.append(line)
# fP.close()


# This is for filegen.txt
# with open(txtFilePath) as fP:
#     for line in fP:
#         line = line.replace("\n","")
#         line = line.replace(","," ")
#         temp = line.split(" ")
#         if temp[0] != "\n":
#             # print(temp[0])
#             lineList.append(temp)
#         else:
#             continue
# fP.close()

# this is to get the list to generate @CAT,P
# count = 1 
with open(needsCataloguePath) as fP:
    for line in fP:
        line = line.replace("\n","")
        line = line.replace(","," ")
        line = line.split(" ")
        if len(line) > 2: 
            #print(line)
            if line[1] == "VTAPE":
                #print("@CAT,P " + line[0][0:18] + ".,VTAPE," + line[2])
                # print(str(count) + " @CAT,P " + line[0][0:18] + ".,VTAPE," + line[2])
                count += 1
            # else:
            #     print(str(count) + " " + str(line))



# with open(dateCheckPath) as fP:
#     for line in fP:
#         line = line.replace("\n","")
#         line = line.split(" ")
#         print(line)
        # if len(line) > 2:
        #     if line[1] == "VTAPE" or line[2] == "NOT":
        #         print(line[0][6:12])
            # if line[1] == "VTAPE":
            #     #  print("@CAT,P " + line[0][0:18] + ".,VTAPE," + line[2])
            #     # print("VTAPE " + line[0][0:18])
            #     print("VTAPE " + line[0])
            # if line[0] == "CAT:":
            #     # print(line)
            #     if 
            #     print("CAT: " + line[1] + ", " + line[2] + " LAST, REF: " + line[5] + " " + line[6])
            # if line[2] == "NOT":
            #     print(line[0] + " is not catalogued or assigned")
# fP.close()
        #print(line)

# this is ger pcprgen
# @PC*U.PCPR-LOAD LT1070,V73920/p,2081
# LT1070 PR@000LT1070 05/17/24 21:57:56 13 V73920 2081 3 V81508
# 0      1            2        3        4  5      6    7 8
# pcprGenList = []
# with open(txtFilePath) as fP:
#     for line in fP:
#         line = line.replace("\n","")
#         temp = line.split(" ")
#         if len(temp) > 4:
#             # print(temp[0][0:2])
#             if temp[0][0:2] == "LT":
#                 print("@PC*U.PCPR-LOAD " + temp[0] + "," + temp[5] + "/P," + temp[6])
                
# print(pcprGenList)

# this is for filegen to generate what is and isn't cataloged
# for i in lineList:
#     if len(i) > 2:
#         # if i[2] == "NOT":
#         #     print(i)
#         if i[1] == "VTAPE":
#             print(i)
#     else:
#         continue

# working with pcprGenList and notCataloguedFileList
# for i in pcprGenList:
#     print(i[0])
# count = 0
# for i in notCataloguedFileList:
#     # print(i[0])
#     temp = i[0]
#     ecl = temp[6:12]
#     for j in pcprGenList:
# # @PC*U.PCPR-LOAD LT1070,V73920/p,2081
# # LT1070 PR@000LT1070 05/17/24 21:57:56 13 V73920 2081 3 V81508
# # 0      1            2        3        4  5      6    7 8
#         if ecl == j[0]:
#             print("@PC*U.PCPR-LOAD " + ecl + "," + j[5] + "/P," + j[6])
    
# @PC*U.PCPR-LOAD LT1090,V73920/P,2083
# @PC*U.PCPR-LOAD LT1160,V86346/P,10
# @PC*U.PCPR-LOAD LT1260,V73920/P,2049
# @PC*U.PCPR-LOAD LT1230,V86346/P,27
# @PC*U.PCPR-LOAD LT1280,V86346/P,31
# @PC*U.PCPR-LOAD LT1250,V86346/P,29
# @PC*U.PCPR-LOAD LT1270,V86346/P,30
# @PC*U.PCPR-LOAD LT1290,V86346/P,32
# @PC*U.PCPR-LOAD LT1320,V86346/P,225
# @PC*U.PCPR-LOAD LT1370,V86346/P,231
# @PC*U.PCPR-LOAD LT1340,V86346/P,227
# @PC*U.PCPR-LOAD LT1350,V86346/P,228
# @PC*U.PCPR-LOAD LT1410,V86346/P,240
# @PC*U.PCPR-LOAD LT1440,V86346/P,244
# @PC*U.PCPR-LOAD LT1450,V86346/P,245
# @PC*U.PCPR-LOAD LT1510,V86346/P,250
# @PC*U.PCPR-LOAD LT1540,V86346/P,253
# @PC*U.PCPR-LOAD LT1570,V86346/P,255