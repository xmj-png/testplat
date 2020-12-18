#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/10/6 14:38
# @Author  : zhoushichuan
# @FileName: case_Necessary_Announcer_List.py
# @Software: PyCharm

import json
import unittest
from login.templates.admin.account.adminlogin import login_admin
from login.templates.utils import httputils
from login.templates.utils.confutils import getcurrentPath, getAdminName


class case_Necessary_Admin_Announcer_List(unittest.TestCase):

    def test_necessary_admin_announcer_list(self):
        """admin主播列表页，数据正常返回"""
        # 登录并获取token
        admin_token = login_admin()
        # 入参
        data = {}
        #获取主播列表的接口以及主播列表前端页面的地址
        announcerList = getAdminName('announcerList')
        AnnouncerList_jsp=getcurrentPath('AnnouncerList_jsp')
        # 请求admin主播列表
        r = httputils.getadmin(announcerList, data, admin_token,AnnouncerList_jsp)
        print(r.text)
        # json字符串转换成字典
        res = json.loads(r.text)
        #断言
        self.assertTrue(len(res["list"]) > 0 and res["status"] == 0)

if __name__ == '__main__':
    unittest.main()
