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

from login.templates.admin.book.Book_Operation import get_book_by_pay_type
from login.templates.app.account.Get_Logon_Token import get_app_login_token
from login.templates.users.Get_UserInfo_By_Token import get_userid_by_token
from login.templates.utils import getconf, httputils, dbutil
from login.templates.utils.utils import get_json_value_by_key, check_keyword_in_list, ranstr


class case_Necessary_Get_Buy_Book_List(unittest.TestCase):

    def test_get_buy_book_and_album_list(self):
        """获取我的页-购买的付费收听列表"""
        # 登录并获取token
        token = get_app_login_token()
        # 入参
        data = {
             'p':1,
             's':20,
             't':2,
             'token': token,
             'mode': '0'
        }
        # 请求我购买的书籍接口
        r = httputils.get_app(getconf.get_global_conf('apinames', 'getBuyBookList'), data)
        print(r.text)
        res = json.loads(r.text)
        #断言
        self.assertTrue(res['status'] == 0)
    def test_get_buy_readbook_list(self):
        """获取我的页-购买的电子阅读列表"""
        # 登录并获取token
        token = get_app_login_token()
        # 入参
        data = {
             'p':1,
             's':20,
             't':0,
             'token': token,
             'mode': '0'
        }
        # 请求我购买的书籍接口
        r = httputils.get_app(getconf.get_global_conf('apinames', 'getBuyBookList'), data)
        print(r.text)
        res = json.loads(r.text)
        #断言
        self.assertTrue(res['status'] == 0 )

if __name__ == '__main__':
    unittest.main()
