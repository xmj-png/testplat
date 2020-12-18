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


class case_NecPlatform_Audio_Production_Book_List(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning) #忽略ResourceWarning提示

    def test_necplatform_audio_production_book_list(self):
        """书籍管理-生产查看列表"""
        # 登录并获取token
        admin_token = login_admin()
        # 获取admin接口url
        productionBookList = getAdminName('productionBookList')
        # 获取前端页面的url
        productionView = getcurrentPath('productionView')
        # 入参
        params = {'recordingStatus':-1,'audioExamineType':-1,'postProductionType':-1,
                  'postExamineType':-1,'productionClose':-1,'copyrightId':0,
                  'searchType':0,'searchKey':'','pageSize':20,'pageNum':1}
        # 调用接口
        res = httputils.getadmin(productionBookList, params, admin_token, productionView)
        sleep(1)
        # 将json格式的字符串转换成字典
        r = json.loads(res.text)
        print(r)
        # 校验接口请求是否成功
        self.assertTrue(r['status'] == 0 and len(r['data']['bookList']) > 0, msg='测试失败！！！')



if __name__ == '__main__':
    unittest.main()
