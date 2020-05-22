from chapter3.city_weather import HeFeng
from chapter3.city_weather_db import HefengDb

def save_all_weather():
    hefeng=HeFeng()
    weathers=hefeng.get_all_weathers(50)
    hefengDb=HefengDb()
    hefengDb.save_all(weathers)
    hefengDb.show_all()
    #p49页3.3



if __ == '__name__':
    #save_all_weather()
    hefengDb=HefengDb()
    hefengDb.show_all()
    for each in  hefengDb.find({'HeWeather6.basic.city':'北京'}):
        print(each)
    print('==================晴天=================================')
    for each in hefengDb.find({'HeWeather6.basic.now.cond_txt':'晴'}):
        print(each['HeWeather6'][0]['basic']['localtion'])
    print('======================温度大于26========================')
    for each in HefengDb.find({'HeWeather6.now.tmp':{'$gt':'26'}}):
        print(each)