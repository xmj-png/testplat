#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/10/6 14:38
# @Author  : zhoushichuan
# @FileName: case_Necessary_Announcer_List.py
# @Software: PyCharm

import json
import unittest
from time import sleep

from login.templates.admin.account.adminlogin import login_admin
from login.templates.utils import httputils
from login.templates.utils.confutils import getcurrentPath, getAdminName


class case_Necessary_Admin_Member_Resource_List(unittest.TestCase):

    def test_necessary_admin_member_resource_list(self):
        """admin会员资源管理列表页，数据正常返回"""
        # 登录并获取token
        admin_token = login_admin()
        # 入参
        data = {'mapType': 'VIP_LIBRARY',
                'selectSearchType': 'selectByPay'}
        #获取会员资源管理列表页接口以及会员资源管理列表前端页面的地址
        memberResourceList = getAdminName('memberResourceList')
        memberResourceList_page=getcurrentPath('memberResourceList')
        # 请求admin会员资源管理列表
        r = httputils.getadmin(memberResourceList, data, admin_token,memberResourceList_page)
        sleep(1)
        print(r.text)
        # json字符串转换成字典
        res = json.loads(r.text)
        #断言
        self.assertTrue(len(res["list"]) > 0 and res["status"] == 0)

if __name__ == '__main__':
    unittest.main()
