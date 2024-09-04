#C:\Users\tseguia\Desktop\BatchWithdrawal\mssi
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

def createExcel(workbookFP, year):
    workbook = xlsxwriter.Workbook(workbookFP)
    worksheet = workbook.add_worksheet()

    worksheet.set_column('A:A', 20) #BWB070 Date
    worksheet.set_column('B:B', 30) #BWB070 Count
    worksheet.set_column('C:C', 20) #PWA023 Date
    worksheet.set_column('D:D', 30) #PWA023 Count
    worksheet.set_column('E:E', 20) #Full Count Date
    worksheet.set_column('F:F', 30) #Full Count Total

    # Add a BOLD format to use to highlight cells.
    bold = workbook.add_format({'bold': True})

    # Write Column Headers.
    worksheet.write('A1', 'BWB070 Date', bold)
    worksheet.write('B1', 'BWB070 Count', bold)
    worksheet.write('C1', 'PWA023 Date', bold)
    worksheet.write('D1', 'PWA023 Count', bold)
    worksheet.write('E1', 'Full Count Date', bold)
    worksheet.write('F1', 'Full Count Total', bold)

    workbook.close()

#C:\\Users\\tseguia\\Documents\\SSI CALENDAR\\firstquarter2021
#C:\\Users\\tseguia\\Desktop\\BatchWithdrawal\\mssi
cDrive = "C:\\Users\\tseguia\\Desktop\\BatchWithdrawal\\mssi" #CHANGE WITH EACH QUARTER #CHANGE

workbookFP = cDrive 

year = "2021" #CHANGE WITH YEAR #CHANGE

workbookFP = workbookFP + year + ".xlsx" 

createExcel(workbookFP, year)