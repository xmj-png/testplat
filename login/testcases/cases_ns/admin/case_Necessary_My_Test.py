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


class case_Necessary_Admin_My_Test(unittest.TestCase):

    def test_necessary_admin_my_test(self):
        """admin听友会列表页面，数据正常返回"""
        # 登录并获取token
        admin_token = login_admin()
        # 入参
        data = {
            'listType': '0',
            'typeCode': '2',
            'groupStatus': '1',
            'pageNum': '1',
            'pageSize': '20'
        }
        #获取听友会列表的admin接口url以及听友会列表的前端页面的url
        GroupList = getAdminName('GroupList') #听友会列表的admin接口url
        GroupList_page=getcurrentPath('GroupList') #听友会列表前端页面的url
        # 请求admin听友会列表接口
        response = httputils.getadmin(GroupList, data, admin_token,GroupList_page)
        print(response.text)
        # json字符串转换成字典
        res = json.loads(response.text)
        #断言
        self.assertTrue(len(res["list"]) > 0 and res["status"] == 0)

if __name__ == '__main__':
    unittest.main() #unitest.main()函数用来测试类中以 test 开头的测试用例
