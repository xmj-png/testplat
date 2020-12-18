#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import unittest
import warnings
from time import sleep
from login.templates.platform.common.Login_Platform import login_platform
from login.templates.utils import getconf, httputils, dbutil
from login.templates.utils.confutils import  getPlatformName


class case_NecPlatform_Audio_GetUnReadCount(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning) #忽略ResourceWarning提示

    def test_necplatform_audio_get_un_read_count(self):
        """获取听书号-账号统计信息？"""
        # 登录并获取token
        platform_token = login_platform()
        # 获取platform接口url
        getUnreadCount=getPlatformName('getUnreadCount')
        #入参
        params={}
        #调用接口
        res=httputils.get_platforms(getUnreadCount,params,platform_token)
        #将json格式的字符串转换成字典
        r=json.loads(res.text)
        print(r)
        #校验接口
        self.assertTrue(r['status']==0 and len(r['data'])>0,msg='测试失败！！！')

if __name__ == '__main__':
    unittest.main()
