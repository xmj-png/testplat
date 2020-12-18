#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import unittest
import warnings
from time import sleep

from login.templates.admin.account.adminlogin import login_admin
from login.templates.platform.common.Login_Platform import login_platform
from login.templates.utils import getconf, httputils, dbutil
from login.templates.utils.confutils import getPlatformName, getAdminName, getcurrentPath


class case_NecPlatform_Audio_Pending_Admin_Approve_BookList(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning) #忽略ResourceWarning提示

    def test_necplatform_audio_pending_admin_approve_book_list(self):
        """待懒人复审书籍（内容）列表"""
        # 登录并获取token
        admin_token = login_admin()
        # 获取admin接口url
        pendingAdminApproveBookList = getAdminName('pendingAdminApproveBookList')
        # 获取前端页面的url
        waitVerify_bookList = getcurrentPath('waitVerify_bookList')
        # 入参
        params = {'approveType': 1,
                'queryType': 0,
                'keyWords': '',
                'pageSize':20,
                'pageNum':1}
        # 调用接口
        res = httputils.getadmin(pendingAdminApproveBookList, params, admin_token, waitVerify_bookList)
        sleep(1)
        # 将json格式的字符串转换成字典
        r = json.loads(res.text)
        print(r)
        # 校验接口请求是否成功
        self.assertTrue(r['status'] == 0 and len(r['data']['list']) > 0, msg='测试失败！！！')
    def test_necplatform_audio_pending_admin_approve_finished_book_list(self):
        """待审核成品书籍列表"""
        # 登录并获取token
        admin_token = login_admin()
        # 获取admin接口url
        pendingAdminApproveBookList = getAdminName('pendingAdminApproveBookList')
        # 获取前端页面的url
        waitVerify_bookList = getcurrentPath('waitVerify_bookList')
        # 入参
        params = {'onlineInfoStatus': -1,
                'approveType': 3,
                'queryType': 0,
                'keyWords': '',
                'pageSize':20,
                'pageNum':1}
        # 调用接口
        res = httputils.getadmin(pendingAdminApproveBookList, params, admin_token, waitVerify_bookList)
        sleep(1)
        # 将json格式的字符串转换成字典
        r = json.loads(res.text)
        print(r)
        # 校验接口请求是否成功
        self.assertTrue(r['status'] == 0 and len(r['data']['list']) > 0, msg='测试失败！！！')


if __name__ == '__main__':
    unittest.main()
