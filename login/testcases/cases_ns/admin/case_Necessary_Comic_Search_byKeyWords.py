#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/10 14:38
# @Author  : caozhuo
# @FileName: case_Admin_Necessary_Book_Search_byKeyWords.py
# @Software: PyCharm
"""
后台书籍搜索

"""
import json
import random
import unittest
from time import sleep

from login.templates.admin.account.adminlogin import login_admin
from login.templates.platform.common.operate_mysql import select
from login.templates.utils import getconf, httputils, dbutil
from login.templates.utils.confutils import getcurrentPath, getAdminName


class case_Necessary_Admin_Comic_Search_byKeyWords(unittest.TestCase):

    def test_necessary_admin_necessary_comic_search_by_keywords(self):
        """admin书籍搜索"""
        # 登录并获取token
        admin_token = login_admin()
        # 获取上架漫画
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
        # 获取上架漫画列表的admin接口url以及上架漫画列表的前端页面的url
        comic_book_list = getAdminName('comic_book_list')
        comic_list = getcurrentPath('comic_list')
        # 请求admin听友会列表接口
        r = httputils.getadmin(comic_book_list, data, admin_token, comic_list)
        sleep(1)
        # json字符串转换成字典
        res = json.loads(r.text)
        comic_book_name = []
        comic_book_id = []
        for comic_dict in res['list']:
            comic_book_name.append(comic_dict.get('bookName'))
            comic_book_id.append(comic_dict.get('id'))
        print('漫画书籍名称:',comic_book_name)
        print('漫画书籍id:',comic_book_id)
        choosed_comic_name = random.choice(comic_book_name)
        choosed_comic_id = random.choice(comic_book_id)
        # 1、通过漫画名称搜索
        data1 = {
            'searchType': 1,
            'keyword': choosed_comic_name,
            'pageNo': 1,
            'pageSize': 20
        }
        r1 = httputils.getadmin(getAdminName('comic_book_list'),data1,admin_token,getcurrentPath('comic_list'))
        res1 = json.loads(r1.text)
        search_comic_name = res1['list'][0].get('bookName')
        self.assertTrue(res1['status']==0 and choosed_comic_name in search_comic_name)
        #2、通过漫画id搜索
        data2 = {
            'searchType': 2,
            'keyword': choosed_comic_id,
            'pageNo': 1,
            'pageSize': 20
        }
        r2 = httputils.getadmin(getAdminName('comic_book_list'), data2, admin_token, getcurrentPath('comic_list'))
        res2 = json.loads(r2.text)
        search_comic_id = res2['list'][0].get('id')
        self.assertTrue(res2['status'] == 0 and choosed_comic_id == search_comic_id)


    if __name__ == '__main__':
        unittest.main()
