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


class case_NecPlatform_Audio_Package_Book_List(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning) #忽略ResourceWarning提示

    def test_necplatform_audio_package_book_list(self):
        """书籍管理-合集书籍列表"""
        # 登录并获取token
        admin_token = login_admin()
        # 获取admin接口url
        packageBookList = getAdminName('packageBookList')
        # 获取前端页面的url
        packageBook = getcurrentPath('packageBook')
        # 入参
        params = {'copyrightId':-1,'purchaseType':-1,'pageSize':20,'pageNum':1}
        # 调用接口
        res = httputils.getadmin(packageBookList, params, admin_token, packageBook)
        sleep(1)
        # 将json格式的字符串转换成字典
        r = json.loads(res.text)
        print(r)
        # 校验接口请求是否成功
        self.assertTrue(r['status'] == 0 and len(r['data']) > 0, msg='测试失败！！！')



if __name__ == '__main__':
    unittest.main()
