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

from login.templates.admin.readbook.Readbook_Operation import readbook_operation
from login.templates.app.account.Get_Logon_Token import get_app_login_token
from login.templates.utils import httputils, dbutil
from login.templates.utils.confutils import getApiName
from login.templates.utils.utils import get_json_value_by_key, check_keyword_in_list


class case_Necessary_Change_Readbook_Recommand_Reason(unittest.TestCase):

    def test_change_readbook_recommand_reason(self):
        '''修改阅读书籍推荐理由'''
        # 调用api接口获取阅读书籍推荐列表
        data1 = {
        'p':1,
        'size':15,
        'types':'[15, 16, 17, 18, 19]',
        'token':get_app_login_token(),
        'mode':0
        }
        r1 = httputils.get_app(getApiName('bookRecommendList'),data1)
        res1 = json.loads(r1.text)
        readbook_ids = get_json_value_by_key(res1,'id')
        part_readbook_ids =readbook_ids[0:20]
        print('readbook_ids:',part_readbook_ids)
        if part_readbook_ids:
            readbook_id = choice(part_readbook_ids)
            print(readbook_id)
            print(type(readbook_id))
        #调用admin接口获取阅读书籍的推荐理由
        readbook_info = readbook_operation.get_readbook_info(readbook_id)
        sleep(0.5)
        print('阅读书籍信息:',readbook_info)
        recReason = readbook_info.get('recReason')
        #调用admin接口修改阅读书籍的推荐理由
        change_readbook_recommand_reason = recReason+'Test01'
        readbook_operation.edit_readbook_info(readbook_id,{'recReason':change_readbook_recommand_reason})
        sleep(1)
        #调用api接口查看阅读书籍的推荐理由（长)是否修改
        data2 = {
            'p': 1,
            'size': 15,
            'types': '[15, 16, 17, 18, 19]',
            'token': get_app_login_token(),
            'mode': 0
        }
        r2 = httputils.get_app(getApiName('bookRecommendList'), data2)
        sleep(2)
        res2 = json.loads(r2.text)
        # 状态校验
        self.assertEqual(r2.status_code, 200, '请求失败')
        self.assertEqual(res2['status'], 0, '请求失败')
        # 返回值校验
        recReasons = get_json_value_by_key(res2,'recReason')
        self.assertTrue(check_keyword_in_list(change_readbook_recommand_reason,recReasons),'阅读书籍推荐理由修改失败！！！')
        #数据还原
        origin_readbook_recommand_reason = recReason
        readbook_operation.edit_readbook_info(readbook_id,{'recReason':origin_readbook_recommand_reason})


if __name__ == '__main__':
    unittest.main()

