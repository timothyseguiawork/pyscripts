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

date = str(time())[0:10].replace("-","")
time = str(time())[11:19].replace(":","")

#matchFP = "C:\\Users\\tseguia\\Desktop\\BatchWithdrawal\\matchfiles\\purge\\bwb070cmp\\bwb070match"+date+time+".txt" 
#noMatchFP = "C:\\Users\\tseguia\\Desktop\\BatchWithdrawal\\matchfiles\\purge\\bwb070cmp\\bwb070noMatch"+date+time+".txt" 
#matchFP = "C:\\Users\\tseguia\\Desktop\\BatchWithdrawal\\matchfiles\\purge\\pwa024\\pwa024match"+date+time+".txt" 
#noMatchFP = "C:\\Users\\tseguia\\Desktop\\BatchWithdrawal\\matchfiles\\purge\\pwa024\\pwa024noMatch"+date+time+".txt" 
matchFP = "C:\\Users\\tseguia\\OneDrive - New York State Office of Information Technology Services\\Desktop\\BatchWithdrawal\\matchfiles\\purge\\pwa023\\pwa023match"+date+time+".txt" 
noMatchFP = "C:\\Users\\tseguia\\OneDrive - New York State Office of Information Technology Services\\Desktop\\BatchWithdrawal\\matchfiles\\purge\\pwa023\\pwa023noMatch"+date+time+".txt" 

bwb070 = "W:\\csprodny\\bwb225" #bwb070 print$
#bwb070 = "W:\\csprodny\\bwb009" #bwb070 print$
#pwa024 = "W:\\csprodny\\bwb007" #bwb070 from 06/07/21
pwa023 = "W:\\csprodny\\pwa225" #pwa023 print$
#pwa024 = "W:\\csprodny\\pwa024" #pwa023 print$

bwb070List = []
pwa023List = []

filePath = bwb070
blankList = []
with open(filePath) as fP:
    for line in fP:
        #blankList.append(line.split())
        if line[0:3] == "000":
            #print("1:" + line[0:12]) #caseNo
            #print("2:" + line[12:26]) 
            #print("3:" + line[18:26]) #date 
            bwb070List.append(line[0:12])

filePath = pwa023
blankList = []
with open(filePath) as fP:
    for line in fP:
        #blankList.append(line.split())
        if "RECORDS" in line:
            #print(line.split()[4])
            pwa023List.append(line.split()[4])

match_count = 0
noMatch_count = 0
matchFile = open(matchFP,"w")
noMatchFile = open(noMatchFP,"w")

#matchFile.write("Case Numbers in both BWB070 print$ and PWA024 print$(these have been purged)\n")
#noMatchFile.write("Case Numbers in BWB070 print$ and PWA024 print$ (these have not been purged?)\n")
matchFile.write("Case Numbers in both BWB070 print$ and PWA023 print$(these have been purged)\n")
noMatchFile.write("Case Numbers in BWB070 print$ and PWA023 print$ (these have not been purged?)\n")

for i in bwb070List:
    if i in pwa023List:
        matchFile.write(i + "\n")
        match_count += 1 
    else:
        print(i + ": Not found")
        noMatchFile.write(i + "\n")
        noMatch_count += 1 
matchFile.write("Match Count: " + str(match_count) + "\n")
noMatchFile.write("No Match Count: " + str(noMatch_count) + "\n")

matchFile.close()
noMatchFile.close()