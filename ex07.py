import openpyxl as op 

wb=op.load_workbook("test.xlsx")

ws=wb['자']

num=2
for row in range(1,10):
    ws.cell(column=1, row=row).value=num
    num*=2
wb.save("test.xlsx")