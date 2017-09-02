"""
天气查询，
输入城市名，获取该城市最新天气情况；
点击「帮助」，获取帮助信息；
点击「历史」，获取历史查询信息。
"""


import ssl
import json
from urllib import request, parse
from WeatherJSONObject import WeatherJSONObject


KEY = 'vmhsqcauskfenhyy'  # API key
UID = "U176BC49D2"  # 用户ID

LOCATION = 'foshan'  # 所查询的位置，可以使用城市拼音、v3 ID、经纬度等
API = 'https://api.seniverse.com/v3/weather/now.json'  # API URL，可替换为其他 URL
UNIT = 'c'  # 单位
LANGUAGE = 'zh-Hans'  # 查询结果的返回语言
gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)


def fetch_weather(location):
    """ 天气查询 """
    params = parse.urlencode({
        'key': KEY,
        'location': location,
        'language': LANGUAGE,
        'unit': UNIT
    })
    req = request.Request('{api}?{params}'.format(api=API, params=params))

    response = request.urlopen(req, context=gcontext).read().decode('UTF-8')

    return response


def format_weather(city):
    """ 显示天气信息 """
    result = fetch_weather(city)
    weather_info = json.loads(
        result, object_hook=WeatherJSONObject)

    weather_data = {'city': weather_info.results[0].location.name, 'text': weather_info.results[0].now.text, 'temperature': weather_info.results[0].now.temperature,
                    'wind_direction': weather_info.results[0].now.wind_direction}
    return weather_data
