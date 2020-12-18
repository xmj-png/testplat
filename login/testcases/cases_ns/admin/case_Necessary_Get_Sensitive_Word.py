#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/10/27 11:08
# @Author : yuhao
# @Site : 
# @File : case_Necessary_Get_Sensitive_Word.py
# @Software: PyCharm

"""
后台进入审核管理-》敏感词库：筛选敏感词
"""

import unittest
import time
from login.templates.utils import httputils
from login.templates.admin.account.adminlogin import login_admin
from login.templates.utils.confutils import getcurrentPath, getAdminName
import json


class case_Necessary_Admin_Get_Sensitive_Word(unittest.TestCase):

    def test_necessary_admin_get_sensitive_word(self):
        """admin敏感词库：筛选敏感词，数据正常返回"""
        # 登录并获取token
        admin_token = login_admin()
        #获取当前时间,请求拼接
        t = time.time()
        ms = int(round(t * 1000))
        #type=1&pageNum=1&_=1603785116033
        data = {
            "type": "1",
            "pageNum": "1",
            "_": ms
        }
        print(type(data))
        #get请求获取敏感词库
        response = httputils.getadmin(getAdminName("lexiconList"), data, admin_token, getcurrentPath('LexiconList'))
        #断言判断返回
        print(response.text)
        json_res = json.loads(response.text)
        self.assertTrue(len(json_res["list"]) > 0 and json_res["status"] == 0)


if __name__ == '__main__':
    unittest.main()

