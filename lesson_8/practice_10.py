import openpyxl

name = input('Enter your name: ')
surname = input('Enter your surname: ')
age = int(input('Enter your age: '))

wb = openpyxl.Workbook()
sheet = wb.active
sheet['A1'] = 'name'
sheet['B1'] = 'surname'
sheet['C1'] = 'age'
sheet['A2'] = name
sheet['B2'] = surname
sheet['C2'] = age

wb.save('example_practice_10.xlsx')
