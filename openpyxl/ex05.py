import openpyxl as op

wb = op.load_workbook("test.xlsx")
ws = wb.active

#1. 셀 데이터 가져와서 확인하기
data1 = ws.cell(3,3).value
data2 = ws["C3"].value

print("Cell Data :",data1)
print("Range Data :",data2)

#범위로 가져오기
rng = ws["A1":"B1"]
print(rng)

rng = ws["a1:c3"]
for row in rng:
    for cell in row:
        print(cell.value, end="\t")
    print()