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
from random import choice

from login.templates.app.account.Get_Logon_Token import get_app_login_token
from login.templates.utils import getconf, httputils, dbutil
from login.templates.utils.getconf import get_global_conf


class case_Necessary_Get_Conversation_List(unittest.TestCase):

    def test_get_conversation_list(self):
        """获取消息中心-消息列表"""
        # 登录并获取token
        token = get_app_login_token()
        # 入参
        data = {
            'opType':'H',
            'size':20,
            'token':token,
            'mode':0
        }
        # 请求消息中心消息列表
        r = httputils.get_app(get_global_conf('apinames', 'getConversationList'), data)
        print(r.text)
        res = json.loads(r.text)
        #断言
        self.assertTrue(res['status'] == 0 and len(res['data'].get('conversationList')) )

if __name__ == '__main__':
    unittest.main()
