from openpyxl import Workbook

workbook = Workbook()
sheet = workbook.active

sheet['A1'] = 'samiwon'
sheet['A2'] = 'akter'
