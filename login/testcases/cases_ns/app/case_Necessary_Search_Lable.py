#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/10 14:38
# @Author  : caozhuo
# @FileName: case_Necessary_Search_Album.py
# @Software: PyCharm
"""
正常搜索

"""
import json
import unittest
from random import choice

from login.templates.app.account.Get_Logon_Token import get_app_login_token
from login.templates.utils import getconf, httputils, dbutil
from login.templates.utils.getconf import get_global_conf


class case_Necessary_search_lable(unittest.TestCase):

    def test_client_search_lable(self):
        """搜索标签"""
        # 登录并获取token
        token = get_app_login_token()
        # 入参
        data = {
            'id':-1,
            'showLocation':1,
            'token':token,
            'mode': '0'
        }
        # 请求热门类别下的标签
        r = httputils.get_app(get_global_conf('apinames', 'labelList'), data)
        print(r.text)
        res = json.loads(r.text)
        #获取热门类别下的所有标签
        lable_list = res['data']['list']
        lable_name = []
        for lable_dict in lable_list:
            lable_name.append(lable_dict.get('name'))
        print(lable_name)
        #随机取一个标签名称
        choose_lable_name = choice(lable_name)
        print(choose_lable_name)
        #搜索接口入参
        data1 = {
            'keyWord':choose_lable_name,
            'token':token,
            'mode':0
        }
        #请求搜索接口，搜索标签
        r1 = httputils.get_app(get_global_conf('apinames','label'),data1)
        res1 = json.loads(r1.text)
        print(res1)
        #对响应结果进行遍历，找到和搜索关键字完全匹配的标签名称
        search_result = False
        for search_lable in res1['list']:
            if search_lable.get('name')==choose_lable_name:
                search_result = True
                break
            else:
                pass
        #断言
        self.assertTrue(res1['status'] == 0 and search_result )

if __name__ == '__main__':
    unittest.main()
