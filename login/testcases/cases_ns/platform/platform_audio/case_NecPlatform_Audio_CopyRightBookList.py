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


class case_NecPlatform_Audio_Copyright_Book_List(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning) #忽略ResourceWarning提示

    def test_necplatform_audio_copyright_book_copyright_view_list(self):
        """生成制作-版权书库-版权查看列表"""
        # 登录并获取token
        admin_token = login_admin()
        # 获取admin接口url
        copyrightBookList = getAdminName('copyrightBookList')
        # 获取前端页面的url
        copyrightBookList_page = getcurrentPath('copyrightView')
        # 入参
        params = {'pageNum':1,'contentType':-1,'purchaseType':-1,
                    'saleShareType':0,'productionStatus':-1,'lrtsLimitPay':-1,
                    'yayaLimitPay':-1,'pageSize':20}
        # 调用接口
        res = httputils.getadmin(copyrightBookList, params, admin_token, copyrightBookList_page)
        sleep(1)
        # 将json格式的字符串转换成字典
        r = json.loads(res.text)
        print(r)
        # 校验接口请求是否成功
        self.assertTrue(r['status'] == 0 and len(r['data']['list']) > 0, msg='测试失败！！！')

    def test_necplatform_audio_copyright_book_product_view_list(self):
        """生成制作-版权书库-生产查看列表"""
        # 登录并获取token
        admin_token = login_admin()
        # 获取admin接口url
        copyrightBookList = getAdminName('copyrightBookList')
        # 获取前端页面的url
        copyrightBookList_page = getcurrentPath('copyrightView')
        # 入参
        params = {'pageNum': 1, 'purchaseType': 1,
                  'rewardedType': -1, 'productionStatus': 0, 'pageSize': 20}
        # 调用接口
        res = httputils.getadmin(copyrightBookList, params, admin_token, copyrightBookList_page)
        sleep(1)
        # 将json格式的字符串转换成字典
        r = json.loads(res.text)
        print(r)
        # 校验接口请求是否成功
        self.assertTrue(r['status'] == 0 and len(r['data']['list']) > 0, msg='测试失败！！！')

if __name__ == '__main__':
    unittest.main()
