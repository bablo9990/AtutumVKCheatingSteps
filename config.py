from urllib import request
import json
import datetime

TOKEN = ''

StepsValue = ''
DistanceValue = 50000

user_agent = "VKAndroidApp/7.7-10445 (Android 11; SDK 30; arm64-v8a; Xiaomi M2003J15CS; ru; 2340x1080;"
date = datetime.today().strtime("%Y-%m-%d")
responce = request.urlopen(request.Request('https://api.vk.com/method/vkRun.setSteps?steps='+str(StepsValue)+ \
                                           '&distance='+str(DistanceValue)+'&date='+date+'&access_token='+TOKEN+'&v=5.131',
                                           headers={'User-Agent': user_agent})).read().decode('utf-8')
print(responce)
