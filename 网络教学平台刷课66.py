#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Jonathan
# datetime:2021/6/12 15:16
# software: PyCharm

import requests
import json

course_ids = [16055911892489, 16055911700596, 16055912594209, 16055911798397]  # 课程id
cookie = '951i9ukfit1q71pnq9bts6cdo4'  # 此处填写学生登录cookie
session = requests.Session()
for course_id in course_ids:
    code_list = []
    rawBody = {'clacode': course_id}
    headers = {'Origin': 'http://172.17.120.66', 'Accept': 'application/json, text/javascript, */*; q=0.01',
               'X-Requested-With': 'XMLHttpRequest', 'Connection': 'close',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10; W0W64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 FCBrowser/2.3.5.20',
               'Referer': 'http://172.17.120.66/courseinfo/detail/clacode/16055911892489',
               'Accept-Encoding': 'gzip, deflate', 'fcpos': '100911', 'Accept-Language': 'zh-CN,zh;q=0.9',
               'Content-Type': 'application/json'}
    cookies = {'PHPSESSID': cookie, 'CNZZDATA1259863527': '1492198656-1623475429-%7C1623480836',
               'UM_distinctid': '179fef426026f4-0dd01e65fbb1cb-476e4771-fa000-179fef426036cc'}
    response = session.post('http://172.17.120.66/Courseinfo/getPlayLogList', json=rawBody, headers=headers,
                            cookies=cookies)

    clist = json.loads(response.text)
    for i in clist:
        code_list.append(i['ExpCode'])

    for cwid in code_list:
        for skillpoints in [122, 112, 111]:  # 此列表为课程完成点标识
            rawBody = {'cwid': cwid, 'cid': course_id, 'starttime': '2021-06-17 20:23:28',
                       'stoptime': '2021-06-17 22:13:39', 'skillpoints': skillpoints, 'errorcount': '0'}
            headers = {'Origin': 'http://172.17.120.66', 'Content-type': 'application/x-www-form-urlencoded',
                       'Accept': '*/*', 'Connection': 'close',
                       'User-Agent': 'Mozilla/5.0 (Windows NT 10; W0W64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 FCBrowser/2.3.5.20',
                       'Referer': 'http://172.17.120.66/Learn/oc/clacode/16055911892489/expfilekey/1553839344315/expcode/16055911896464',
                       'fcpos': '100911', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9'}
            cookies = {'PHPSESSID': cookie,
                       'CNZZDATA1259863527': '1492198656-1623475429-%7C1623480836',
                       'UM_distinctid': '179fef426026f4-0dd01e65fbb1cb-476e4771-fa000-179fef426036cc'}
            response = session.post('http://172.17.120.66/Learn/setexplog', json=rawBody, headers=headers,
                                    cookies=cookies)
            print(response.text)
