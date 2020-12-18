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


class case_NecPlatform_Audio_Banner_List(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning) #忽略ResourceWarning提示

    def test_necplatform_audio_banner_list(self):
        """听书号配置-投放banner列表"""
        # 登录并获取token
        admin_token = login_admin()
        # 获取admin接口url
        bannerList = getAdminName('bannerList')
        # 获取前端页面的url
        banner_list = getcurrentPath('banner_list')
        # 入参
        params = {'status': 1,
                    'pageSize': 20,
                    'pageNumber': 1,
                    }
        # 调用接口
        res = httputils.getadmin(bannerList, params, admin_token, banner_list)
        sleep(1)
        # 将json格式的字符串转换成字典
        r = json.loads(res.text)
        print(r)
        # 校验接口请求是否成功
        self.assertTrue(r['status'] == 0, msg='测试失败！！！')

if __name__ == '__main__':
    unittest.main()
