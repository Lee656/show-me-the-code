#coding:utf-8
import xlwt

def write_xls():
    with open('numbers.txt', 'r') as f:
        data = eval(f.read())
    file = xlwt.Workbook()
    table = file.add_sheet('city')
    row = 0
    for v in data:
        for col, val in enumerate(v):
            table.write(row, col, val if type(val) != str else val.decode('gbk'))
        row += 1
    file.save('numbers.xls')

if __name__ == '__main__':
    write_xls()