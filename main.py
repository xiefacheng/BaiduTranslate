from BaiduTranslate.baiduts import get_translate_info
from BaiduTranslate.excel_data import ExcelLoad


exl = ExcelLoad(excel_path=r'C:\Users\Administrator\Documents\GitHub\BaiduTranslate\百度翻译.xlsx')
sheet = exl.write_data('Sheet1')
word = ''
while True:
    word = input('输入查询单词：')
    if word == '!q':
        break
    else:
        select_word = get_translate_info(word)
        print('查询的结果为：{}'.format(select_word))
        