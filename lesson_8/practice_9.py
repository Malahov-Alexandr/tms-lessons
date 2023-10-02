import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active

sheet['A1'] = 'name'
sheet['B1'] = 'sername'
sheet['C1'] = 'age'
sheet['A2'] = 'Alexander'
sheet['B2'] = 'Malahov'
sheet['C2'] = 35

wb.save('example.xlsx')