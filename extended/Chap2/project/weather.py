"""
天气查询，
输入城市名，返回该城市最新的天气数据；
输入指令，获取帮助信息（一般使用 h 或 help）；
输入指令，获取历史查询信息（一般使用 history）；
输入指令，退出程序的交互（一般使用 quit 或 exit）；
"""

import os
import ssl
import sys
import json
import time
import dateutil.parser as par_d
from urllib import request, parse
from simplejson import loads

from urllib.error import URLError, HTTPError
from WeatherJSONObject import *
from tinydb import TinyDB, Query, where

KEY = 'vmhsqcauskfenhyy'  # API key
UID = "U176BC49D2"  # 用户ID

LOCATION = 'foshan'  # 所查询的位置，可以使用城市拼音、v3 ID、经纬度等
API = 'https://api.seniverse.com/v3/weather/now.json'  # API URL，可替换为其他 URL
UNIT = 'c'  # 单位
LANGUAGE = 'zh-Hans'  # 查询结果的返回语言

tiny_db = TinyDB(os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), os.pardir, 'resource',
        'weather_info.json')))

gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)

help_mesg = """
1. 输入城市名，返回该城市的天气数据；
2. 输入help或h，打印帮助文档;
3. 输入history,打印查询历史;
4. 输入quit或exit，退出程序.
"""


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


def search_histories(input_str):
    """ 查询历史天气信息 """
    input_list = input_str.split()
    input_len = len(input_list)
    weathers = Query()

    if input_len == 1:
        def today_func(d): return d.startswith(
            time.strftime('%Y-%m-%d', time.localtime()))

        result_weathers = tiny_db.search(
            weathers.results[0].last_update.test(today_func))
        disply_seach(result_weathers)

    elif input_len == 2:
        try:
            date_str = par_d.parse(
                input_list[1]).strftime('%Y-%m-%d')

            def date_func(d): return d.startswith(date_str)
            result_weathers = tiny_db.search(
                weathers.results[0].last_update.test(date_func))
            disply_seach(result_weathers)
        except ValueError as ex:
            result_weathers = tiny_db.search(
                weathers.results[0].location.name == input_list[1])
            disply_seach(result_weathers)
    elif input_len == 3:
        date_str = par_d.parse(
            input_list[2]).strftime('%Y-%m-%d')

        def date_func(d): return d.startswith(date_str)
        result_weathers = tiny_db.search(
            (weathers.results[0].last_update.test(date_func)) & (weathers.results[0].location.name == input_list[1]))
        disply_seach(result_weathers)
    else:
        print('命令有误或没有符合的历史信息，请重新输入！')


def disply_seach(seachs):
    if len(seachs) == 0:
        print('没有符合查询条件的历史信息，请重新输入！')
    else:
        print('历史查询信息：')
        print('*' * 10)
        for result_weather in seachs:
            print(result_weather.get('results')[0].get('location').get('name') + '天气: ' + result_weather.get('results')[0].get('now').get('text')
                  + ', 温度(摄氏度): ' + result_weather.get('results')[0].get('now').get(
                  'temperature') + ', 相对湿度%: ' + result_weather.get('results')[0].get('now').get('humidity')
                  + ',发布时间: ' + result_weather.get('results')[0].get('last_update'))


def disply_weather(weather_info):
    """ 显示天气信息 """
    print(weather_info.results[0].location.name + '天气: ' +
          weather_info.results[0].now.text + ', 温度(摄氏度): ' + weather_info.results[0].now.temperature + ', 相对湿度%: ' + weather_info.results[0].now.humidity + ',发布时间: ' + weather_info.results[0].last_update)


def save_histories(save_weather):
    """ 保存历史天气信息 """
    dict_weather = loads(save_weather)

    weathers = Query()

    results = tiny_db.search((weathers.results[0].location.id == dict_weather['results'][0]['location']['id']) & (
        weathers.results[0].last_update == dict_weather['results'][0]['last_update']))
    results_len = len(results)
    if results_len == 0:
        tiny_db.insert(dict_weather)


if __name__ == '__main__':
    """ main """

    print(help_mesg)

    while True:
        input_str = input('>')

        if input_str in ['h', 'help']:
            print(help_mesg)
        elif input_str.startswith('history'):
            search_histories(input_str)
        elif input_str in ['quit', 'exit']:
            search_histories('history')
            sys.exit(0)
        else:
            try:
                result = fetch_weather(input_str)
                weather_info = json.loads(
                    result, object_hook=WeatherJSONObject)

                save_histories(result)
                disply_weather(weather_info)

            except HTTPError as ex:
                print('HTTPError: ', ex.code)
