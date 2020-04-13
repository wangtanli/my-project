import random

import requests

url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
content="我和你都是中国"

class Youdao():
    def __init__(self,content):
        self.url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
        self.ts=self.get_ts()
        self.salt=self.get_salt()
        self.sign=self.get_sign()


    def get_salt(self):
        s=str(random.randint(0,10))
        t=self.ts
        #print("random= ",s)
        #print("ts= ",t)
        # print("salt= "t+s)
        return  t+s
         #return '15860628873889'

    def get_md5(self,value):
         import hashlib
         m = hashlib.md5()
         m.update(value.encode("utf-8"))
         return m.hexdigest()

    def get_sign(self):
        i=self.salt
        e = self.content
        s="fanyideskweb" + e + i + "Nw(nmmbP%A-r6U3EUn]Aj"
        print("s= ",s, "md5= " ,get_md5(s))
        return self.get_md5(s)
        #'16bfeef8bfe1bab0f14a688e05092703'


    def get_ts(self):
        import time
        t = time.time()
        ts = str(int(round(t * 1000)))
        return ts
       #'1586068687933'

    def get_content(self):
         return content


    # def get_content(self):
      #     return '我和你都是中国'

    def yield_form_data(self):
        form_data={
            'i': self.content,
             'from': 'zh-CHS',
             'to': 'en',
             'smartresult': 'dict',
             'client': 'fanyideskweb',
             'salt': self.salt,
             'sign': self.sign,
             'ts': self.ts,
             'bv': 'a9c3483a52d7863608142cc3f302a0ba',
             'doctype': 'json',
             'version': '2.1',
             'keyfrom': 'fanyi.web',
             'action': 'FY_BY_REALTlME',
              }
        return form_data


    def get_headers(self):
        headers={
          'Cookie: OUTFOX_SEARCH_USER_ID=155979949@10.108.160.17; OUTFOX_SEARCH_USER_ID_NCOO=1811'
          'Referer: http://fanyi.youdao.com/'
          'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
        }
        return headers


    def fanyi(self):

         response = requests.post(self.url, date=self.yield_form_data(), headers=self.get_headers())
         return response.text

if __name__ == '__main__':
    youdao=Youdao('我们')
    print(youdao.fanyi())

