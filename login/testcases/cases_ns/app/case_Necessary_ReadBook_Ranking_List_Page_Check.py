#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/10 14:38
# @Author  : caozhuo
# @FileName: case_Necessary_Search_Album.py
# @Software: PyCharm

import json
import unittest

from login.templates.admin.book.Book_Operation import get_albumn_by_pay_type
from login.templates.app.account.Get_Logon_Token import get_app_login_token
from login.templates.utils import getconf, httputils, dbutil
from login.templates.utils.utils import get_json_value_by_key, check_keyword_in_list, ranstr


class case_Necessary_ReadBook_Ranking_List_Page_Check(unittest.TestCase):

    def test_ReadBook_Ranking_List_Page_Check(self):
        """排行榜-看书榜，数据正常返回"""
        # 登录并获取token
        token = get_app_login_token()
        # 获取一个在线榜单
        rankid = dbutil.select('select id from t_rankings where state=0 and rank_type=2 limit 2', 'db_audiobook')
        print(type(rankid))
        print(rankid)
        if rankid:
            Id = rankid[0]["id"]
        data = {
            'token': token,
            'size': '20',
            'pageNum': '1',
            'rangeType': '0',
            'rankId': str(Id),
            'referId':'0',
            'mode': '0'
        }
        # 请求阅读榜单的资源数据
        r = httputils.get_app(getconf.get_global_conf('apinames', 'rankingsItemList'), data)
        print(r.text)
        list2 = json.loads(r.text)['list']
        if len(list2) == 0 and json.loads(r.text)['status'] == 0:
            #取另一个在线id，再次调用接口
            data = {
                'token': token,
                'size': '20',
                'pageNum': '1',
                'rangeType': '0',
                'rankId': str(rankid[1]["id"]),
                'referId': '0',
                'mode': '0'
            }
            # 请求阅读榜单的资源数据
            r = httputils.get_app(getconf.get_global_conf('apinames', 'rankingsItemList'), data)
            print(r.text)
            list3 = json.loads(r.text)['list']
            self.assertTrue(len(list3) > 0 and json.loads(r.text)['status'] == 0)
        else:
            self.assertTrue(len(list2) > 0 and json.loads(r.text)['status'] == 0)

    if __name__ == '__main__':
        unittest.main()
