import requests
from bs4 import  BeautifulSoup

url="http://www.cntour.cn"
response=requests.get(url)

 # print(response.text)

soup=BeautifulSoup(response.text,'lxml')
data=soup.select("#main > div > div.mtop.firstMod.clearfix > div.leftBox > div:nth-child(3) > ul > li:nth-child(2) > a")
print(data)
for item in data
      result={
          'title':item.get_text(),
          'link':itme.get('herf')
      }
      print(result)