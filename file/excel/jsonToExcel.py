#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json
import tablib
import requests


def get_data(page_num=1):
    url = 'http://xxx.xxx.com/abcdefg?pageNum=%s&startDate=2021-09-30&endDate=2021-10-08' % page_num
    print('url', url)
    res = requests.get(url)
    json_text = res.text
    # test_01 = json.dumps(json_text)  # 操作数据流
    text2 = json.loads(json_text)
    # getData(text_data)
    # test_03=json.loads(text_data)
    return text2['data']


def get_json_data(test0):
    test_01 = json.loads(test0)  # 操作数据流
    test_json = test_01['encryptInfo']['records']
    # print("请求得到数据",test_json)
    return test_json


def get_total():
    json_total = json.loads(get_data(1))['totalCount'] // 100 + 1
    print('请求得到条数', json_total)
    return json_total


def write_excel(test_json):
    header = tuple([i for i in test_json[0].keys()])

    data = []
    # 循环里面的字典，将value作为数据写入进去
    for row in test_json:
        body = []
        for v in row.values():
            body.append(v)
        data.append(tuple(body))

    data = tablib.Dataset(*data, headers=header)

    open('文件名.xls', 'wb').write(data.xls)


if __name__ == '__main__':
    # get_tatal()
    list = []
    for i in range(get_total()):
        my_data = get_data(i + 1)
        datas = get_json_data(my_data)
        # print(len(datas))
        for o in datas:
            # print(o)
            list.append(o)
        print(len(list))
        write_excel(list)
# 获取ｊｓｏｎ数据

# with open('demo.json', 'r', encoding='utf-8') as f:
#     dict_json = json.load(f)  # 操作文件流
#
#     print(dict_json)
#     test0 = dict_json['data']
#     test_01 = json.loads(test0)  # 操作数据流
#     test_json = test_01['encryptInfo']['records']

# 将json中的key作为header, 也可以自定义header（列名）
