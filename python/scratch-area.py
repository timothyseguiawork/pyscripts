
def multiply(x,y,result):
    #print(x)
    #print(y) 
    result = x*y
    return result

cDrive = "C:\\Users\\tseguia\\OneDrive - New York State Office of Information Technology Services\\Documents\\" #CHANGE WITH EACH QUARTER #CHANGE
textFile = "scratch-area" #CHANGE WITH EACH QUARTER #CHANGE

txtFilePath = cDrive + textFile + ".txt"

sum = 0
result = 0
lineNum = 1

with open(txtFilePath) as fP:
    for line in fP:
        lineList = line.split()
        if not lineList: #BLANKS
            print(str(lineNum) + ": EMPTY LINE")
            lineNum += 1
            continue
        if len(lineList) < 2 or lineList[0] != "PIC": #St
            print(str(lineNum) + ": " + str(lineList) + " SKIPPED")
            lineNum += 1
            continue
        else:
            character = lineList[1]
        if len(character) == 3:
            #print("num: " + str(character[1]))
            sum += int(character[1])
            print (str(lineNum) + ": " + str(character))
            lineNum += 1
        if len(character) > 3: #this is for (10) or (2).
            character = character[1:]
            parenthRemove = character.replace("(","")
            parenth2Remove = parenthRemove.replace(")","")
            periodRemove = parenth2Remove.replace(".","")
            sum += int(periodRemove)
            print (str(lineNum) + ": " + str(periodRemove))
            lineNum += 1
            #print(periodRemove)
        
        #grabCharNum = 
        #sum += charToNum

#print(str(multiply(sum,12,result)))
print("sum = " + str(sum))
print("lines = " + str(lineNum-1))
