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


class case_Necessary_Client_Get_Book_Type(unittest.TestCase):

    def test_client_get_book_type(self):
        """分类页-查看更多页数据正常返回"""
        # 登录并获取token
        token = get_app_login_token()
        # 入参
        data = {
            'fid':9000,
            'open':0,
            'sid':0,
            'token': token,
            'mode': '0'
        }
        # 请求客户端获取分类信息接口
        r = httputils.get_app(getconf.get_global_conf('apinames', 'ClientGetBookType'), data)
        print(r.text)
        res = json.loads(r.text)
        #断言
        self.assertTrue(res['status'] == 0 and len(res['list'])>0 )

if __name__ == '__main__':
    unittest.main()
