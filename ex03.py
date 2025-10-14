import openpyxl as op

wb = op.load_workbook("test.xlsx")
print(wb)

ws = wb.active
print(ws)

ws_list = wb.sheetnames
print(ws_list)

for ws_name in ws_list:
    print(ws_name, end="")
    ws = wb[ws_name]
    print(ws)
print()
