#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/9/23 10:45
# @Author : yuhao
# @Site : 
# @File : case_Necessary_FuliPage_Check.py
# @Software: PyCharm

import unittest
from login.templates.app.account.Get_Logon_Token import get_app_login_token
from login.templates.utils.confutils import getApiName
from login.templates.utils import httputils
import json


#类首字母需大写，驼峰原则
class Case_Necessary_FuliPage_Check(unittest.TestCase):

    def test_necessary_fuliPage_check(self):
        """福利页数据检查校验"""
        #登录并获取token
        token = get_app_login_token()
        #请求福利页所需参数---imei、nwt、q参数已加
        data = {
            'referID': '',
            'token': token,
            'mode': '0'
        }

        #请求接口获取返回
        response_return = httputils.get_app(getApiName('fuliPage'), data)
        print(response_return.text)
        #转换返回数据格式str->dict
        list = json.loads(response_return.text)['data']
        self.assertTrue(len(list) > 2)#referid与dayFuliActivity不是模块


if __name__ == '__main__':
    unittest.main()

