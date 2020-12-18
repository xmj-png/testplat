#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/10 14:38
# @Author  : caozhuo
# @FileName: case_Necessary_Search_Album.py
# @Software: PyCharm

import json
import unittest
from random import choice
from time import sleep

from login.templates.admin.account.adminlogin import login_admin
from login.templates.app.account.Get_Logon_Token import get_app_login_token
from login.templates.utils import getconf, httputils, dbutil
from login.templates.utils.confutils import getApiName, getAdminName, getcurrentPath
from login.templates.utils.utils import get_json_value_by_key, check_keyword_in_list


class case_Necessary_Search_Book(unittest.TestCase):

    def test_Search_Book(self):
        '''有声书搜索'''
        # 数据准备
        #调用admin接口，获取在线的书籍
        data1 = {'pageNum': 3,
                'sort': 'new_time',
                'bstateKey': 0,
                'contentLevel': 0,
                'censorFlag': 0,
                'pageSize': 20}
        r1 = httputils.getadmin(getAdminName('bookList'),data1,login_admin(),getcurrentPath('bookList'))
        #遍历各个书籍的名称
        book_names = []
        for book_object in json.loads(r1.text)['list']:
            book_names.append(book_object.get('bookName'))
        print('书籍names',book_names)
        #选择一本在线书籍
        if book_names:
            search_word = choice(book_names)
        print('搜索关键字：',search_word)
        # 获取一本在线书籍
        data = {'type': '0',
                'pageNum': '1',
                'pageSize': '5',
                'token': get_app_login_token(),
                'keyWord': search_word}
        r = httputils.get_app(getApiName('BookSearch'), data)
        sleep(0.5)
        # 状态校验
        self.assertEqual(r.status_code, 200, '请求失败')
        self.assertEqual(json.loads(r.text)['status'], 0, '请求失败')
        # 返回值校验
        rs1 = json.loads(r.text)
        print(rs1)
        rec = get_json_value_by_key(rs1, 'name')  # 获取name
        print("name值：", rec)
        self.assertTrue(check_keyword_in_list(search_word, rec), '搜索结果为null')


if __name__ == '__main__':
    unittest.main()
