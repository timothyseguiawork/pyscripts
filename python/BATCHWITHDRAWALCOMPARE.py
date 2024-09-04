#wrts comparison python prog
#W:\csprod\psdxwmwrts
#Created by Timothy Seguia, 01/04/2021
from pathlib import Path
from time import sleep
import datetime
import xlsxwriter

#CREATE A GLOBAL VARIABLE COUNT
matchCount = 0
noMatchCount = 0

def horiLine():
    print("--------------------------------------")
    
def time():
    return datetime.datetime.now()

def returnList(filePath,index):
    PrintCount = 0
    blankList = []
    with open(filePath) as fP:
        for line in fP:
            #PWA023 ['RECORDS', 'DELETED', 'FOR', 'CASE:', '00024926460H']
            if line[0:25] == "RECORDS DELETED FOR CASE:" and filePath == "W:\\csprodny\\pwa023":
                blankList.append(line.split()[index])
            #BWB070-out ['00024926460H']
            if filePath == "W:\\csprodny\\bwb070-out" or filePath == "W:\\csprodny\\bwb072-out":
                blankList.append(line.split()[index])
    return blankList

#compare shit
#for i in bwb070OutList:
#    if i in pwa023List:
#        print("Match: " + i)
#        matchFile.write(i + "\n")
#    else:
#        print("No Match: " + i)
#        noMatchFile.write(i + "\n")

def compare(firstList, secondList, matchFile, noMatchFile):
    matchCount = 0
    noMatchCount = 0
    for i in firstList:
        if i in secondList:
            #print("Match: " + i)
            matchFile.write(i + "\n")
            matchCount += 1
        else:
            #print("No Match: " + i)
            noMatchFile.write(i + "\n")
            noMatchCount += 1
    matchFile.write("Count: " + str(matchCount) + "\n")
    noMatchFile.write("Count: " + str(noMatchCount) + "\n")
        

#datetime format CCYYDDMMHHMMSS
# CCYY = year
# DD = day
# MM = month
# HH = hour
# MM = minute
# SS = second
date = str(time())[0:10].replace("-","")
time = str(time())[11:19].replace(":","")

bwb070OutFP = "W:\\csprodny\\bwb070-out" #BWB070-OUT
bwb072OutFP = "W:\\csprodny\\bwb072-out" #BWB072-OUT
pwa023FP = "W:\\csprodny\\pwa023" #PWA023 OUT
pwa123FP = "W:\\csprodny\\pwa123" #PWA123 OUT
matchFP = "C:\\Users\\tseguia\\Desktop\\BatchWithdrawal\\matchfiles\\purge\\pwa023match"+date+time+".txt" 
noMatchFP = "C:\\Users\\tseguia\\Desktop\\BatchWithdrawal\\matchfiles\\purge\\pwa023noMatch"+date+time+".txt" 
outputMatchFP = "C:\\Users\\tseguia\\Desktop\\BatchWithdrawal\\matchfiles\\bwb070out\\bwb070match"+date+time+".txt"
noOutputMatchFP = "C:\\Users\\tseguia\\Desktop\\BatchWithdrawal\\matchfiles\\bwb070out\\bwb070noMatch"+date+time+".txt"

bwb070OutList = []
pwa023List = []

pwa023List = returnList(pwa023FP,4)
pwa123List = returnList(pwa123FP,4)
bwb070OutList = returnList(bwb070OutFP,0)
bwb072OutList = returnList(bwb072OutFP,0)

matchFile = open(matchFP,"w")
noMatchFile = open(noMatchFP,"w")
outputMatchFile = open(outputMatchFP,"w")
noOutputMatchFile = open(noOutputMatchFP,"w")

matchFile.write("Case Numbers in both BWB070-OUT and PWA023 (these have been purged)\n")
noMatchFile.write("Case Numbers in BWB070-OUT and not in PWA023 (these have not been purged?)\n")
outputMatchFile.write("Case Numbers in both BWB070-OUT and BWB072-OUT\n")
noOutputMatchFile.write("Case Numbers in BWB070-OUT and not in BWB072-OUT\n")


#compare bwb070 and deletions of that night
#compare(bwb070OutList,pwa023List,matchFile,noMatchFile)
#compare bwb070-outs in general 
#compare(bwb070OutList,bwb072OutList,outputMatchFile,noOutputMatchFile)

#print(date + time)

matchFile.close()
noMatchFile.close()
outputMatchFile.close()
noOutputMatchFile.close()