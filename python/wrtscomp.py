#wrts comparison python prog
#W:\csprod\psdxwmwrts
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

def lineBreakup(line): 
#Setup for lineBreakup in original prog 
#print("Record " + str(count) + ": Excel Count " + str(excelCount))
#print(line[33:41] + ": LAST_TRANSACTION_DT (8)") # LAST_TRANSACTION_DT 9
#print(line[5:7] + ": TRANSACTION_CD (2)") # TRANSACTION_CD 3 
#print(line[31:33] + ": LAST_TRANSACTION_TYPE_CD (2)") # LAST_TRANSACTION_TYPE_CD 3
#print(line[30] + ": SSI_MASTER_RECORD_TYPE_CD (1)") # SSI_MASTER_RECORD_TYPE_CD (1)
#print(line[0:3] + ": TRANSFER_COUNTY_CD (3)") # TRANSFER_COUNTY_CD (3)
#print(line[3] + ": TRANSFER_CD (1)") # TRANSFER_CD (1)
#print(line[616:619] + ": WIN_COUNTY_CD (3)")
#print(line[619:622] + ": WIN_INSTITUTION_CD (3)")
#print(line[622:625] + ": WIN_CASE_NBR (3)")
#print(line[639:661] + ": ESSENTIAL_PERSON_WIN_ID") #ESSENTIAL_PERSON_WIN_ID
#print(line[1538:1541] + ": SDX_LAST_PAYMENT_STATUS_CD")#SDX_LAST_PAYMENT_STATUS_CD
#print(line[30:31] + ": SDX_WMS_IND")#SDX_WMS_IND
#print(line[15:23] + ": RECORD_PROCESS_DT")#RECORD_PROCESS_DT
#print(line[670:692] + ": ELIGIBLE_SPOUSE_WIN_ID")#ELIGIBLE_SPOUSE_WIN_ID
#print(line[43:52] + ": SSN_ID (9)")
    A = line[33:41].replace(" ","-")
    B = line[5:7].replace(" ","-")
    C = line[31:33].replace(" ","-")
    D = line[30].replace(" ","-")
    E = line[0:3].replace(" ","-")
    F = line[3].replace(" ","-")
    G = line[616:619].replace(" ","-")
    H = line[619:622].replace(" ","-")
    I = line[622:625].replace(" ","-")
    J = line[639:661].replace(" ","-")
    K = line[1538:1541].replace(" ","-")
    L = line[30:31].replace(" ","-")
    M = line[15:23].replace(" ","-")
    N = line[670:692].replace(" ","-")
    O = line[42:51].replace(" ","-") #SSN
    return A,B,C,D,E,F,G,H,I,J,K,L,M,N,O

def createExcel(workbookFP, lineList):
    workbook = xlsxwriter.Workbook(workbookFP)
    worksheet = workbook.add_worksheet()

    worksheet.set_column('A:A', 30) #Merge File
    worksheet.set_column('B:B', 30) #Merge Date
    worksheet.set_column('C:C', 30) #Scheduled Run
    worksheet.set_column('D:D', 30) #Run Number
    worksheet.set_column('E:E', 30) #Date
    worksheet.set_column('F:F', 30) #File
    worksheet.set_column('G:G', 30) #DoF
    worksheet.set_column('H:H', 30) #Proc
    worksheet.set_column('I:I', 30) #Drop
    worksheet.set_column('J:J', 30) #Drop
    worksheet.set_column('K:K', 30) #Drop
    worksheet.set_column('L:L', 30) #Drop
    worksheet.set_column('M:M', 30) #Drop
    worksheet.set_column('N:N', 30) #Drop
    worksheet.set_column('O:O', 30) #Drop

    # Add a BOLD format to use to highlight cells.
    bold = workbook.add_format({'bold': True})

# LAST_TRANSACTION_DT A
# TRANSACTION_CD B
# LAST_TRANSACTION_TYPE_CD C
# SSI_MASTER_RECORD_TYPE_CD D
# TRANSFER_COUNTY_CD E
# TRANSFER_CD F
# WIN_COUNTY_CD G
# WIN_INSTITUTION_CD H
# WIN_CASE_NBR I
# ESSENTIAL_PERSON_WIN_ID J
# SDX_LAST_PAYMENT_STATUS_CD K
# SDX_WMS_IND L
# RECORD_PROCESS_DT M
# ELIGIBLE_SPOUSE_WIN_ID N
# SSN_ID O

    # Write Column Headers.
    worksheet.write('A1', 'LAST_TRANSACTION_DT', bold)
    worksheet.write('B1', 'TRANSACTION_CD', bold)
    worksheet.write('C1', 'LAST_TRANSACTION_TYPE_CD', bold)
    worksheet.write('D1', 'SSI_MASTER_RECORD_TYPE_CD', bold)
    worksheet.write('E1', 'TRANSFER_COUNTY_CD', bold)
    worksheet.write('F1', 'TRANSFER_CD', bold)
    worksheet.write('G1', 'WIN_COUNTY_CD', bold)
    worksheet.write('H1', 'WIN_INSTITUTION_CD', bold)
    worksheet.write('I1', 'WIN_CASE_NBR', bold)
    worksheet.write('J1', 'ESSENTIAL_PERSON_WIN_ID', bold)
    worksheet.write('K1', 'SDX_LAST_PAYMENT_STATUS_CD', bold)
    worksheet.write('L1', 'SDX_WMS_IND', bold)
    worksheet.write('M1', 'RECORD_PROCESS_DT', bold)
    worksheet.write('N1', 'ELIGIBLE_SPOUSE_WIN_ID', bold)
    worksheet.write('O1', 'SSN_ID', bold)

    count = 2
    for i in range(len(lineList)): 
        excelCount = str(count)

        aCol = 'A' + excelCount
        bCol = 'B' + excelCount
        cCol = 'C' + excelCount
        dCol = 'D' + excelCount
        eCol = 'E' + excelCount
        fCol = 'F' + excelCount
        gCol = 'G' + excelCount
        hCol = 'H' + excelCount
        iCol = 'I' + excelCount
        jCol = 'J' + excelCount
        kCol = 'K' + excelCount
        lCol = 'L' + excelCount
        mCol = 'M' + excelCount
        nCol = 'N' + excelCount
        oCol = 'O' + excelCount

        for j in range(len(lineList[i])):
            print(lineList[i][j])
            if j == 0:
                worksheet.write(aCol,lineList[i][j])
            if j == 1:
                worksheet.write(bCol,lineList[i][j])
            if j == 2:
                worksheet.write(cCol,lineList[i][j])
            if j == 3:
                worksheet.write(dCol,lineList[i][j])
            if j == 4:
                worksheet.write(eCol,lineList[i][j])
            if j == 5:
                worksheet.write(fCol,lineList[i][j])
            if j == 6:
                worksheet.write(gCol,lineList[i][j])
            if j == 7:
                worksheet.write(hCol,lineList[i][j])
            if j == 8:
                worksheet.write(iCol,lineList[i][j])
            if j == 9:
                worksheet.write(jCol,lineList[i][j])
            if j == 10:
                worksheet.write(kCol,lineList[i][j])
            if j == 11:
                worksheet.write(lCol,lineList[i][j])
            if j == 12:
                worksheet.write(mCol,lineList[i][j])
            if j == 13:
                worksheet.write(nCol,lineList[i][j])
            if j == 14:
                worksheet.write(oCol,lineList[i][j])

        count += 1
        horiLine()
    workbook.close()

#C:\\Users\\tseguia\\Documents\\marilyn\\sdxmaster
#W:\\csprod\\psdwmwrts
cDrive = "W:\\csprod\\psdwmwrts" 
#textFile = "sdxmaster.txt" 

txtFilePath = cDrive 

lineList = []

with open(txtFilePath) as fP:
    for line in fP:
        if "063723130" in line:
            print(line)
            break
        #horiLine()

#createExcel(workbookFP, lineList)
