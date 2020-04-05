import requests

url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"


def get_salt():
    return '15860628873889'


def get_sign():
    return '16bfeef8bfe1bab0f14a688e05092703'


def get_ts():
    import time
    t = time.time()
    ts = str(int(round(t * 1000)))
    return ts
      #'1586068687933'

form_data={
    'i': '我和你都是中国',
    'from': 'zh-CHS',
    'to': 'en',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': get_salt(),
    'sign': get_sign(),
    'ts': get_ts(),
    'bv': 'a9c3483a52d7863608142cc3f302a0ba',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTlME',
}
response=requests.post(url,form_data)
print(response.text)
