#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/10 14:38
# @Author  : caozhuo
# @FileName: case_Admin_Necessary_Book_Search_byKeyWords.py
# @Software: PyCharm

import json
import unittest
from login.templates.admin.account.adminlogin import login_admin
from login.templates.utils import httputils
from login.templates.utils.confutils import getcurrentPath, getAdminName


class case_Necessary_Admin_AlbumRank_Useful_Check(unittest.TestCase):

    def test_necessary_admin_albumrank_useful_check(self):
        """admin节目榜单列表可用检查"""
        # 登录并获取token
        admin_token = login_admin()
        # 入参
        data = {
            'rankType': '5'
        }
        # 请求admin节目榜单
        r = httputils.getadmin(getAdminName('rankingsList'), data, admin_token,
                                      getcurrentPath('AlbumRankingList'))
        print(r.text)
        json_res = json.loads(r.text)
        #断言
        self.assertTrue(len(json_res["list"]) > 0 and json_res["status"] == 0)

if __name__ == '__main__':
    unittest.main()
