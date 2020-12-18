#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/10 14:38
# @Author  : caozhuo
# @FileName: case_Admin_Necessary_Listeners_Useful_Check.py
# @Software: PyCharm

import json
import unittest
from login.templates.admin.account.adminlogin import login_admin
from login.templates.utils import httputils
from login.templates.utils.confutils import getcurrentPath, getAdminName


class case_Necessary_Admin_Listeners_Useful_Check(unittest.TestCase):

    def test_necessary_admin_listeners_useful_check(self):
        """admin听友会列表页面，数据正常返回"""
        # 登录并获取token
        admin_token = login_admin()
        # 第一次请求获取资源筛选数据
        data = {
            'listType': '0',
            'typeCode': '2',
            'groupStatus': '1',
            'pageNum': '1',
            'pageSize': '20'
        }
        # 请求admin听友会列表页
        response = httputils.getadmin(getAdminName('GroupList'), data, admin_token,
                                      getcurrentPath('GroupList'))
        print(response.text)
        json_res = json.loads(response.text)
        self.assertTrue(len(json_res["list"]) > 0 and json_res["status"] == 0)

    if __name__ == '__main__':
        unittest.main()
