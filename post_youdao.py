import requests

url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
form_data={
    'i': '我和你都是中国',
    'from': 'zh-CHS',
    'to': 'en',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': '15860628873889',
    'sign': '16bfeef8bfe1bab0f14a688e05092703',
    'ts': '1586062887388',
    'bv': 'a9c3483a52d7863608142cc3f302a0ba',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTlME',
}
response=requests.post(url,form_data)
print(response.text)
