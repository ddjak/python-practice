#Chapter 12

#Excel

import openpyxl

wb = openpyxl.load_workbook('./automate_online-materials/example.xlsx')

#print(wb.get_sheet_names())

sheet3 = wb['Sheet3']

#print(sheet3.title)

currentSheet = wb.active
cell = currentSheet['A1']
#print(currentSheet)

#print(currentSheet['A1'].value)

#print(currentSheet['B1'].value)

#print('Row ' + str(cell.row) + ', Column ' + str(cell.column) + ' is ' + str(cell.value))

#print('Cell ' + str(cell.coordinate) + ' is ' + str(cell.value))

sheet = wb['Sheet1']
sheet['D1'] = 'Hello'
print(sheet['D1'].value)

wb.save("./automate_online-materials/example.xlsx")
