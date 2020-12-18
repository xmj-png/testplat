     #!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/10 14:38
# @Author  : caozhuo
# @FileName: case_Necessary_Search_Album.py
# @Software: PyCharm

import json
import unittest
import warnings
from random import choice
from login.templates.admin.account.adminlogin import login_admin
from login.templates.app.account.Get_Logon_Token import get_app_login_token
from login.templates.utils import getconf, httputils, dbutil
from login.templates.utils.confutils import getApiName, getAdminName, getcurrentPath
from login.templates.utils.utils import get_json_value_by_key, check_keyword_in_list


class case_Necessary_Search_Batch(unittest.TestCase):
    def setUp(self):
        # 忽略一些告警打印
        warnings.simplefilter("ignore", ResourceWarning)
    def test_search_batch_book(self):
        '''APP推荐页搜索框搜索书籍验证'''
        # 数据准备
        # 调用admin接口，获取在线的书籍
        data1 = {'pageNum': 3,
                 'sort': 'new_time',
                 'bstateKey': 0,
                 'contentLevel': 0,
                 'censorFlag': 0,
                 'pageSize': 20}
        r1 = httputils.getadmin(getAdminName('bookList'), data1, login_admin(), getcurrentPath('bookList'))
        # 遍历各个书籍的名称
        book_names = []
        for book_object in json.loads(r1.text)['list']:
            book_names.append(book_object.get('bookName'))
        print('书籍names', book_names)
        # 选择一本在线书籍
        if book_names:
            search_word = choice(book_names)
        print('搜索关键字：', search_word)
        # 接口入参
        data = {'keyWord':search_word,
                'pageNum':0,
                'pageSize':3,
                'searchOption':'1,2,3,4,5',
                'type':0,
                'token':get_app_login_token(),
                'mode':0}
        r = httputils.get_app(getApiName('searchBatch'), data)
        # 状态校验
        self.assertEqual(r.status_code, 200, '请求失败')
        self.assertEqual(json.loads(r.text)['status'], 0, '请求失败')
        # 返回值校验
        rs1 = json.loads(r.text)
        print(rs1)
        rs2 = rs1['data']['bookResult']
        res = get_json_value_by_key(rs2, 'name')  # 获取name列表
        print("name值：", res)
        self.assertTrue(check_keyword_in_list(search_word, res), '搜索结果为空！')#判断搜索name是否在name列表中

    def test_search_batch_album(self):
        '''APP推荐页搜索框搜索节目验证'''
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
        #接口入参
        data = {'keyWord':search_word,
                'pageNum':0,
                'pageSize':3,
                'searchOption':'1,2,3,4,5',
                'type':0,
                'token':get_app_login_token(),
                'mode':0}
        r = httputils.get_app(getApiName('searchBatch'), data)
        # 状态校验
        self.assertEqual(r.status_code, 200, '请求失败')
        self.assertEqual(json.loads(r.text)['status'], 0, '请求失败')
        # 返回值校验
        rs1 = json.loads(r.text)
        print(rs1)
        rs2 = rs1['data']['albumResult']
        res = get_json_value_by_key(rs2, 'name')  # 获取name列表
        print("name值：", res)
        self.assertTrue(check_keyword_in_list(search_word, res), '搜索结果为空！')#判断搜索name是否在name列表中
    def test_search_batch_readbook(self):
        '''APP推荐页搜索框搜索阅读书籍验证'''
        # 调用admin接口，获取在线的阅读书籍
        data1 = {
            'freeType': -1,
            'stateType': 1,
            'orderType': 1,
            'pageSize': 20,
            'fatherType': 0,
            'secondType': 0,
            'bodyType': 0,
            'contentType': 0,
            'pageNum': 3
        }
        r1 = httputils.getadmin(getAdminName('readBookList'), data1, login_admin(), getcurrentPath('ReadBookList'))
        # 遍历各个阅读书籍的name
        readbooks = []
        for readbook_object in json.loads(r1.text).get('list'):
            readbooks.append(readbook_object.get('bookName'))
        print('阅读书籍names:', readbooks)
        if readbooks:
            search_word = choice(readbooks)
        print('搜索关键字：', search_word)
        #app接口入参
        data = {'keyWord':search_word,
                'pageNum':0,
                'pageSize':3,
                'searchOption':'1,2,3,4,5',
                'type':0,
                'token':get_app_login_token(),
                'mode':0}
        r = httputils.get_app(getApiName('searchBatch'), data)
        # 状态校验
        self.assertEqual(r.status_code, 200, '请求失败')
        self.assertEqual(json.loads(r.text)['status'], 0, '请求失败')
        # 返回值校验
        rs1 = json.loads(r.text)
        print(rs1)
        rs2 = rs1['data']['readResult']
        res = get_json_value_by_key(rs2, 'name')  # 获取name列表
        print("name值：", res)
        self.assertTrue(check_keyword_in_list(search_word, res), '搜索结果为空！')#判断搜索name是否在name列表中
    def test_search_batch_anchor(self):
        '''APP推荐页搜索框搜索主播验证'''
        # 数据准备
        anchor_names = ['郭德纲','单田芳','周建龙','易中天','大灰狼','播音米小圈']
        search_word = choice(anchor_names) #
        # 获取一本在线书籍
        data = {'keyWord':search_word,
                'pageNum':0,
                'pageSize':3,
                'searchOption':'1,2,3,4,5',
                'type':0,
                'token':get_app_login_token(),
                'mode':0}
        r = httputils.get_app(getApiName('searchBatch'), data)
        # 状态校验
        self.assertEqual(r.status_code, 200, '请求失败')
        self.assertEqual(json.loads(r.text)['status'], 0, '请求失败')
        # 返回值校验
        rs1 = json.loads(r.text)
        print(rs1)
        rs2 = rs1['data']['announcerResult']
        res = get_json_value_by_key(rs2, 'nickName')  # 获取name列表
        print("name值：", res)
        self.assertTrue(check_keyword_in_list(search_word, res), '搜索结果为空！')#判断搜索name是否在name列表中


if __name__ == '__main__':
    unittest.main()
