from BaiduTranslate.baiduts import get_translate_info
from BaiduTranslate.excel_data import ExcelLoad
from os import path

d = path.dirname(__file__)
# excel_path = d+'/百度翻译.xlsx'
# print(excel_path)
exl = ExcelLoad(excel_path=r'C:\Users\Administrator\Documents\GitHub\BaiduTranslate\百度翻译.xlsx')
sheet = exl.write_data('Sheet1')
word = ''
row = 2
while True:
    word = input('输入查询单词：')
    if word == '!q':
        break
    else:
        select_word = get_translate_info(word)
        print('查询的结果为：{}'.format(select_word))
        rows = sheet.max_row  # 获取表格最大行数
        if sheet.cell(rows, 2).value is not None:
            row = rows + 1
            sheet.cell(row, 1, row - 1)
            sheet.cell(row, 2, word)
            sheet.cell(row, 3, select_word)
        # else:
        #     sheet.cell(rows, 1, row - 1)
        #     sheet.cell(rows, 2, word)
        #     sheet.cell(rows, 3, select_word)
        exl.wb.save('百度翻译.xlsx')
