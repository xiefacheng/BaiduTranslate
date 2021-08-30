import requests


def get_translate_info(word):
    url = 'https://fanyi.baidu.com/sug'
    # word = input("输入查询的单词")
    # 通过F12查看传参方式为post
    dat = {'kw': word}
    resp = requests.post(url, data=dat)
    # 获取翻译后的字段
    translate_info = resp.json()['data'][0]['v']
    return translate_info


# 调试功能是否正常
if __name__ == '__main__':
    w1 = get_translate_info('dog')
    print(w1)
