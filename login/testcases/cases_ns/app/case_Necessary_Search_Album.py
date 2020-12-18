#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/10 14:38
# @Author  : caozhuo
# @FileName: case_Necessary_Search_Album.py
# @Software: PyCharm

import json
import unittest
from random import choice

from login.templates.admin.account.adminlogin import login_admin
from login.templates.app.account.Get_Logon_Token import get_app_login_token
from login.templates.utils import httputils, dbutil
from login.templates.utils.confutils import getApiName, getAdminName, getcurrentPath
from login.templates.utils.utils import get_json_value_by_key, check_keyword_in_list


class case_Necessary_Search_Album(unittest.TestCase):

    def test_search_normal_word(self):
        '''输入节目名称搜索节目'''
        # 数据准备
        # 调用admin接口，获取在线的节目
        data1 = {'type': 0,
                'pageNum': 3,
                'pageSize': 20,
                'ablumnStatus': 0}
        r1 = httputils.getadmin(getAdminName('albumList'), data1, login_admin(), getcurrentPath('AlbumList'))
        # 遍历各个节目的名称
        album_names = []
        for album_object in json.loads(r1.text)['list']:
            album_names.append(album_object.get('name'))
        print('节目names', album_names)
        # 选择一本在线节目
        if album_names:
            search_word = choice(album_names)
        print('搜索的关键字：', search_word)
        # 获取一本在线节目
        data = {'type': '0', 'pageNum': '1', 'pageSize': '5', 'token': get_app_login_token(),
                'keyWord': search_word,'mode':0}

        r = httputils.get_app(getApiName('searchAlbum'), data)
        # 状态校验
        self.assertEqual(r.status_code, 200, '请求失败')
        self.assertEqual(json.loads(r.text)['status'], 0, '请求失败')
        # 返回值校验
        rs1 = json.loads(r.text)
        print(rs1)
        res = get_json_value_by_key(rs1, 'name')  # 获取所有name的值
        print("name值：", res)
        self.assertTrue(check_keyword_in_list(search_word, res), '搜索结果为null')


if __name__ == '__main__':
    unittest.main()
