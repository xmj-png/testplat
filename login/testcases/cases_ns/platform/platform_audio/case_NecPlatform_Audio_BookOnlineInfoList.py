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


class case_NecPlatform_Audio_Book_Online_Info_List(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning) #忽略ResourceWarning提示

    def test_necplatform_audio_complete_book_online_info_list(self):
        """完善上架信息审核列表"""
        # 登录并获取token
        admin_token = login_admin()
        # 获取admin接口url
        bookOnlineInfoList = getAdminName('bookOnlineInfoList')
        # 获取前端页面的url
        completeInfo = getcurrentPath('completeInfo')
        # 入参
        params = {'approvalType': 1,
                    'copyrightId': 0,
                    'contentType': -1,
                    'searchType': 0,
                    'keyword':'',
                    'pageNum': 1,
                    'pageSize': 20}
        # 调用接口
        res = httputils.getadmin(bookOnlineInfoList, params, admin_token, completeInfo)
        sleep(1)
        # 将json格式的字符串转换成字典
        r = json.loads(res.text)
        print(r)
        # 校验接口请求是否成功
        self.assertTrue(r['status'] == 0 and len(r['data']['onlineInfoList']) > 0, msg='测试失败！！！')
    def test_necplatform_audio_modification_book_online_info_list(self):
        """修改上架信息审核列表"""
        # 登录并获取token
        admin_token = login_admin()
        # 获取admin接口url
        bookOnlineInfoList = getAdminName('bookOnlineInfoList')
        # 获取前端页面的url
        completeInfo = getcurrentPath('completeInfo')
        # 入参
        params = {'approvalType': 2,
                    'copyrightId': 0,
                    'contentType': -1,
                    'searchType': 0,
                    'keyword':'',
                    'pageNum': 1,
                    'pageSize': 20}
        # 调用接口
        res = httputils.getadmin(bookOnlineInfoList, params, admin_token, completeInfo)
        sleep(1)
        # 将json格式的字符串转换成字典
        r = json.loads(res.text)
        print(r)
        # 校验接口请求是否成功
        self.assertTrue(r['status'] == 0 and len(r['data']['onlineInfoList']) > 0, msg='测试失败！！！')

if __name__ == '__main__':
    unittest.main()
