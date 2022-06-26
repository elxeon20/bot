
import currency
from currency import Currency
import openpyxl
from datetime import datetime
import pandas as pd
wb = openpyxl.load_workbook('db.xlsx')
ws = wb['data']

for i in range(9 + 1):
    ws.append([132,132,654])

wb.save(filename="db.xlsx")
wb.close()