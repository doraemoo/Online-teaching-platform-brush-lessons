#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Jonathan
# datetime:2021/6/12 15:16
# software: PyCharm

import requests
import json

course_ids = [16085252813305, 16085252583983, 16085253156981, 16085252704530]  # 课程id
cookie = 'tk43o9u20g7vvkb44km5p1emi1'  # 此处填写学生登录cookie
session = requests.Session()
for course_id in course_ids:
    code_list = []
    rawBody = {'clacode': course_id}
    headers = {'Origin': 'http://172.17.120.88', 'Accept': 'application/json, text/javascript, */*; q=0.01',
               'X-Requested-With': 'XMLHttpRequest', 'Connection': 'close',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10; W0W64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 FCBrowser/2.3.5.20',
               'Referer': 'http://172.17.120.88/courseinfo/detail/clacode/16085252813305',
               'Accept-Encoding': 'gzip, deflate', 'fcpos': '100911', 'Accept-Language': 'zh-CN,zh;q=0.9',
               'Content-Type': 'application/json'}
    cookies = {'PHPSESSID': cookie, 'CNZZDATA1259863527': '1478194879-1623730963-%7C1623730963',
               'UM_distinctid': '17a0e2bce8a378-0bfe8903508096-476e4771-fa000-17a0e2bce8b344'}
    response = session.post('http://172.17.120.88/Courseinfo/getPlayLogList', json=rawBody, headers=headers,
                            cookies=cookies)
    clist = json.loads(response.text)
    for i in clist:
        code_list.append(i['ExpCode'])

    for cwid in code_list:
        for skillpoints in [122, 112, 111]:  # 此列表为课程完成点标识
            rawBody = {'cwid': cwid, 'cid': course_id, 'starttime': '2021-06-17 06:19:28',
                       'stoptime': '2021-06-17 08:37:39', 'skillpoints': skillpoints, 'errorcount': '0'}
            headers = {'Origin': 'http://172.17.120.88', 'Content-type': 'application/x-www-form-urlencoded',
                       'Accept': '*/*', 'Connection': 'close',
                       'User-Agent': 'Mozilla/5.0 (Windows NT 10; W0W64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 FCBrowser/2.3.5.20',
                       'Referer': 'http://172.17.120.88/Learn/oc/clacode/16085252813305/expfilekey/1553835936125/expcode/16085252818765',
                       'fcpos': '100911', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9'}
            cookies = {'PHPSESSID': cookie,
                       'CNZZDATA1259863527': '1478194879-1623730963-%7C1623730963',
                       'UM_distinctid': '17a0e2bce8a378-0bfe8903508096-476e4771-fa000-17a0e2bce8b344'}
            response = session.post('http://172.17.120.88/Learn/setexplog', json=rawBody, headers=headers,
                                    cookies=cookies)

            print(response.text)
