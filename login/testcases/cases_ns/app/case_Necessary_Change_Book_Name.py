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
from login.templates.admin.book.Book_Operation import get_book_info_dict, edit_book_info_approve, edit_book_info_by_dict
from login.templates.app.account.Get_Logon_Token import get_app_login_token
from login.templates.utils import httputils, dbutil
from login.templates.utils.confutils import getApiName, getAdminName, getcurrentPath
from login.templates.utils.utils import get_json_value_by_key, check_keyword_in_list


class case_Necessary_Change_Book_Name(unittest.TestCase):

    def test_change_book_name(self):
        '''修改书籍名称'''
        # 调用admin接口，获取在线的书籍
        data1 = {'pageNum': 3,
                 'sort': 'new_time',
                 'bstateKey': 0,
                 'contentLevel': 0,
                 'censorFlag': 0,
                 'pageSize': 20}
        r1 = httputils.getadmin(getAdminName('bookList'), data1, login_admin(), getcurrentPath('bookList'))
        # 遍历各个书籍的名称
        book_ids = []
        for book_object in json.loads(r1.text)['list']:
            book_ids.append(book_object.get('bookId'))
        print('书籍ids', book_ids)
        # 选择一本在线书籍
        if book_ids:
            book_id = choice(book_ids)
        print('书籍id：', book_id)
        #调用admin接口获取书籍信息
        book_info = get_book_info_dict(book_id)
        sleep(0.5)
        book_Name = book_info.get('bookName')
        #调用admin接口修改书籍信息
        change_book_name = book_Name+'Test01'
        book_info_dict = {'bookName':change_book_name}
        if book_info.get('fatherTypeId')==0 or book_info.get('sonTypeId'):
            book_info_dict['fatherTypeId'] = 1
            book_info_dict['sonTypeId'] = 11
            edit_book_info_by_dict(book_id,book_info_dict)
        else:
            edit_book_info_by_dict(book_id, book_info_dict)
        sleep(1)
        #调用api接口查看书籍的名称是否修改
        data = {'bookId':book_id,
                'token':get_app_login_token()
                }
        r = httputils.get_app(getApiName('bookDetailPage'), data)
        sleep(2)
        # 状态校验
        self.assertEqual(r.status_code, 200, '请求失败')
        self.assertEqual(json.loads(r.text)['status'], 0, '请求失败')
        # 返回值校验
        rs1 = json.loads(r.text)['data']['bookDetail']['name']
        print(rs1)
        print(change_book_name)
        self.assertEqual(rs1,change_book_name, '书籍名称修改未生效！！！')
        #数据还原
        origin_book_name = book_Name
        edit_book_info_by_dict(book_id, {'bookName': origin_book_name})


if __name__ == '__main__':
    unittest.main()
