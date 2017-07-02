#coding:utf-8

from xml.dom import minidom
import xlrd, json

def covert_xls_to_xml(filename):
    # excel
    book = xlrd.open_workbook(filename)
    table = book.sheets()[0]
    data  = {}
    for row in xrange(table.nrows):
        for col in xrange(table.ncols):
            if col == 0:
                data[table.cell(row, 0).value] = []
            else:
                data[table.cell(row, 0).value].append(table.cell(row, col).value)
    # xml
    xml = minidom.Document()
    root = xml.createElement('root')
    xml.appendChild(root)
    student = xml.createElement(table.name)
    root.appendChild(student)
    comment = xml.createComment(u'\n学生信息表\n"id" : [名字, 数学, 语文, 英文]')
    student.appendChild(comment)
    student_info = xml.createTextNode(json.dumps(data, ensure_ascii=False))
    student.appendChild(student_info)
    with open(filename.split('.')[0]+'.xml', 'w') as f:
        f.write(xml.toprettyxml(encoding='utf-8'))



if __name__ == '__main__':
    covert_xls_to_xml('student.xls')