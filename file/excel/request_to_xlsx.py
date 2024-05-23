# -*- coding: utf-8 -*-
import json
import requests
import openpyxl


# 获取请求数据
def get_data(page_num=1):
    url = 'http://xxx.com/ahdkhfkahfkhahfk?pageNum=%s&startDate=2021-09-30&endDate=2021-10-08' % page_num
    print('url', url)
    res = requests.get(url)
    json_text = res.text
    req_data = json.loads(json_text)
    return req_data['data']


# 获取总页数
def get_total():
    total = json.loads(get_data(1))['totalCount']
    json_total = total / 100
    if isinstance(json_total, int):
        pass
    else:
        json_total = total // 100 + 1
    print('请求得到总页数: ', json_total)
    return json_total


# 操作数据流
def get_json_data(data):
    data_json = json.loads(data)
    data_dict = data_json['encryptInfo']['records']
    return data_dict


# 获取表格抬头list
def get_excel_title():
    list_title = []
    dict_title = get_json_data(get_data(1))
    for k in dict_title[0].keys():
        list_title.append(k)
    print("获取到表格抬头: ", list_title)
    return list_title


# xlsx写入excel
def write_excel_xlsx(path, sheet_name, my_list):
    index = len(my_list)
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = sheet_name
    for i in range(0, index):
        for j in range(0, len(my_list[i])):
            sheet.cell(row=i + 1, column=j + 1, value=str(my_list[i][j]))
    workbook.save(path)
    print("xlsx格式表格写入数据成功！")


if __name__ == '__main__':
    list_all = []
    list_title = get_excel_title()
    for i in range(get_total()):
        my_data = get_data(i + 1)
        datas = get_json_data(my_data)
        for j in datas:
            list_tmp = []
            for v in j.values():
                list_tmp.append(v)
            list_all.append(list_tmp)
        print("已获取数据行数", len(list_all))
    list_all.insert(0, list_title)
    write_excel_xlsx(r'D:\aaa.xlsx', 'aaa_data', list_all)
