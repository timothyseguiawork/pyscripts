#Python Program for calculating distribution list for cins and transactions
#Created by Timothy Seguia, 11/13/19
from pathlib import Path
import datetime

def newLine():
    print()
def horiLine():
    print("____________________________________")
def percentage(num, whole):
    result = (num/whole)*100.0
    return result
def time():
    return datetime.datetime.now()


cinLastTwo = ""
cin = ""
cnt = 1
transactionDate = ""
prtCINFormat = ""
prtPercentFormat = ""
dictOfLastTwoNumbers = {}
dictOfPercentage = {}

print("This is a program to identify the # of cins found!")
filePath = 'W:\wms\louisfindf'
print("louisfindf Opened!")
with open(filePath) as fP:
    for line in fP:
        cin = line[0:9]
        cinLastTwo = line[6:8]
        transactionDate = line[9:]
        prtCINFormat = "{0} CIN:{1}, LAST 2:{2}, TRX:{3}".format(cnt, cin, cinLastTwo, transactionDate) 
        if (cinLastTwo not in dictOfLastTwoNumbers.keys()) or (cinLastTwo not in dictOfPercentage.keys()):
            if not transactionDate.strip():
                transactionDate = "EMPTY"
            else:   
                dictOfLastTwoNumbers[cinLastTwo] = 1
                dictOfPercentage[cinLastTwo] = percentage(dictOfLastTwoNumbers.get(cinLastTwo),cnt)
        else:
            dictOfLastTwoNumbers[cinLastTwo] = dictOfLastTwoNumbers.get(cinLastTwo) + 1
            dictOfPercentage[cinLastTwo] = percentage(dictOfLastTwoNumbers.get(cinLastTwo),cnt)
            


        horiLine()
        print(time())
        print(prtCINFormat)
        print("Dictionary of CINS")
        print(dictOfLastTwoNumbers)
        print("Dictionary of Percentages")
        print(dictOfPercentage)
        horiLine()
        newLine()
        newLine()
        cnt += 1
print("Records: %d" % cnt)

