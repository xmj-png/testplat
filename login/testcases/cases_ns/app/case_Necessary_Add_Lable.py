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

import requests

from login.templates.app.account.Get_Logon_Token import get_app_login_token
from login.templates.platform.settlement.get_CurrentTime import getCurrentTime
from login.templates.utils import getconf, httputils, dbutil
from login.templates.utils.getconf import get_global_conf
from login.templates.utils.httputils import post_app
from login.templates.utils.utils import securitycode


class case_Necessary_Add_Lable(unittest.TestCase):

    def test_client_add_lable(self):
        """关注标签"""
        #1、获取热门标签类别下的所有标签
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
        lable_id = []
        for lable_dict in lable_list:
            lable_id.append(lable_dict.get('id'))
        print(lable_id)
        #2、获取我的标签类别下已关注的标签
        #入参1
        data1 = {
            'id':-2,
            'showLocation':1,
            'token':token
        }
        r1 = httputils.get_app(get_global_conf('apinames','labelList'),data1)
        res1 = json.loads(r1.text)
        my_lable = []
        for lable_dict1 in res1['data']['list']:
            my_lable.append(lable_dict1.get('id'))
        print('my_lable:',my_lable)
        #3、关注未关注的标签
        lable_list = list(set(lable_id)-set(my_lable))
        #随机取一个标签名称
        choose_lable_id = choice(lable_list)
        print('choose_lable_id',choose_lable_id)
        #接口入参2
        data2 = {
                'token':token,
                'mode':0,
                'list':json.dumps({"list":[{"srcType":100,"srcEntityId":choose_lable_id,"opType":0,"folderId":-2,"createTime":getCurrentTime()}]})
        }
        r2 = post_app(get_global_conf('apinames','ClientAddConllection'),data2)
        res2 = json.loads(r2.text)
        print(res2)
        #断言
        self.assertEqual(res2.get('status'),0,'请求失败！！！')
        #4、数据还原
        #接口入参3
        data3 = {
                'token':token,
                'mode':0,
                'list':json.dumps({"list":[{"srcType":100,"srcEntityId":choose_lable_id,"opType":1}]})
        }
        #请求3
        r3 = post_app(get_global_conf('apinames','ClientAddConllection'),data3)
        res3 = json.loads(r3.text)
        print(type(r3.text))
        print(res3)
        if res3.get('status')==0:
            print('数据还原成功！！！')
        else:
            print('数据还原失败!!!')

if __name__ == '__main__':
    unittest.main()
