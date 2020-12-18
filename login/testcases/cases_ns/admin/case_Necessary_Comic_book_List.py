#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/10 14:38
# @Author  : caozhuo
# @FileName: case_Admin_Necessary_Listeners_Useful_Check.py
# @Software: PyCharm

import json
import unittest
from time import sleep

from login.templates.admin.account.adminlogin import login_admin
from login.templates.utils import httputils
from login.templates.utils.confutils import getcurrentPath, getAdminName


class case_Necessary_Admin_Comic_Book_List(unittest.TestCase):

    def test_necessary_admin_comic_book_list(self):
        """admin上架漫画列表页，数据正常返回"""
        # 登录并获取token
        admin_token = login_admin()
        # 入参
        data = {
            'searchType': 0,
            'containSensitive': -1,
            'typeId': 0,
            'country': 0,
            'copyrightId': 0,
            'payLimit': -1,
            'bookStatus': 0,
            'onlineStatus': -1,
            'listOrder': 1,
            'pageNo': 1,
            'pageSize': 20
        }
        #获取上架漫画列表的admin接口url以及上架漫画列表的前端页面的url
        comic_book_list = getAdminName('comic_book_list')
        comic_list = getcurrentPath('comic_list')
        # 请求admin听友会列表接口
        r = httputils.getadmin(comic_book_list, data, admin_token,comic_list)
        sleep(1)
        # json字符串转换成字典
        res = json.loads(r.text)
        print(res)
        #断言
        self.assertTrue(len(res["list"]) > 0 and res["status"] == 0)

if __name__ == '__main__':
    unittest.main() #unitest.main()函数用来测试类中以 test 开头的测试用例
