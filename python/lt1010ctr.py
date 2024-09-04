# lt1010 counter
count = 0
cDrive = "C:\\Users\\tseguia\\OneDrive - New York State Office of Information Technology Services\\DESKTOP\\" #CHANGE WITH EACH QUARTER #CHANGE
textFile = "lt1010.txt"
filePath = cDrive + textFile

with open(filePath, encoding='latin1') as f:
    lines = f.readlines()
for i in lines: 
    if "5000-PAYMENT-IGNORE" in i:
        # count += 1
        pass
    if "TEST-VALID-PAY-TYPE   = " in i: 
        # print(len())
        payCode = i[31:34]
        if payCode != "  " or payCode != " " or payCode != "\n" or payCode != "":
            print(payCode)
        # pass
    if "TEST-VALID-SPC-CLM-CD" in i: 
        # print(len(i))
        paySTR = i[31:34]
        if paySTR != "  " or paySTR != " " or paySTR != "\n" or payCode != "":
            print(paySTR)
# print(str(len(lines)))
# print(str(count))
f.close()

    