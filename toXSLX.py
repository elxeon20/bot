import currency
import openpyxl
from datetime import datetime




def add_data_to_xlsx(asset, tradeType, payTypes):
    wb = openpyxl.load_workbook('db.xlsx')
    ws = wb['data']
    a = currency.Currency(asset, tradeType, payTypes).data_for_xlsx()
    #Добавление данных в экскль
    for i in range(9 + 1):
        ws.append(a[i])
        print(a[i])
    # подсчет кол-ва строк в экселе
    count_row = 0
    for row in ws.values:
        count_row += 1
    # добавление даты в строки
    current_datetime = datetime.now().date()
    data_row = count_row+1
    for i in range(10):
        ws.cell(row=data_row-1, column=4, value=current_datetime)
        data_row -= 1

    wb.save(filename="db.xlsx")
    wb.close()

add_data_to_xlsx("UAH", "BUY", ['PrivatBank'])