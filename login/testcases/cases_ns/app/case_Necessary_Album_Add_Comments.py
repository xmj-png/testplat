#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/10 14:38
# @Author  : caozhuo
# @FileName: case_Necessary_Search_Album.py
# @Software: PyCharm
"""
评论

"""
import json
import unittest
from time import sleep

from login.templates.admin.book.Book_Operation import get_albumn_by_pay_type
from login.templates.app.account.Get_Logon_Token import get_app_login_token
from login.templates.utils import getconf, httputils
from login.templates.utils.utils import get_json_value_by_key, check_keyword_in_list, ranstr, random_chinese


class case_Necessary_Album_Add_Comments(unittest.TestCase):

    def test_Album_Add_Comments(self):
        """节目添加评论test"""
        # 登录并获取token
        token = get_app_login_token()
        # 第一次请求获取资源筛选数据
        data = {
            'token': token,
            'checkType': '0',
            'commentContent': random_chinese(4)+ranstr(2),
            'commentStar': '5',
            'entityType': '2',
            'fatherId': '0',
            'srcEntityId': get_albumn_by_pay_type(1, 1),
            'mode': '0'
        }
        # 首次请求资源筛选页数据
        r = httputils.get_app(getconf.get_global_conf('apinames', 'AddComment.action'), data)
        sleep(0.1)
        print(r.text)
        commentId = json.loads(r.text)['commentId']
        self.assertTrue(commentId > 0)

if __name__ == '__main__':
    unittest.main()
