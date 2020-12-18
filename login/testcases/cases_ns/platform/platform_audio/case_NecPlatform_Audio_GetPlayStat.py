#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import unittest
import warnings
from login.templates.platform.common.Login_Platform import login_platform
from login.templates.platform.settlement.get_CurrentTime import before_today
from login.templates.utils import getconf, httputils, dbutil
from login.templates.utils.confutils import  getPlatformName


class case_NecPlatform_Audio_Get_Play_Stat(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning) #忽略ResourceWarning提示

    def test_necplatform_audio_get_play_stat_book(self):
        """获取听书号-数据中心-书籍分析"""
        # 登录并获取token
        platform_token = login_platform()
        # 获取platform接口url
        getPlayStat=getPlatformName('getPlayStat')
        #入参
        params={'type': 1,
                'startTime': before_today(-1),
                'endTime': before_today(-1),
                'orderBy': 2,
                'pageNum': 1,
                'pageSize': 20
                }
        #调用接口
        res=httputils.get_platforms(getPlayStat,params,platform_token)
        #将json格式的字符串转换成字典
        r=json.loads(res.text)
        print(r)
        #校验接口
        self.assertTrue(r['status']==0 and len(r['data'].get('list'))>0,msg='测试失败！！！')
    def test_necplatform_audio_get_play_stat_album(self):
        """获取听书号-数据中心-节目分析"""
        # 登录并获取token
        platform_token = login_platform()
        # 获取platform接口url
        getPlayStat=getPlatformName('getPlayStat')
        #入参
        params={'type': 2,
                'startTime': before_today(-1),
                'endTime': before_today(-1),
                'orderBy': 2,
                'pageNum': 1,
                'pageSize': 20
                }
        #调用接口
        res=httputils.get_platforms(getPlayStat,params,platform_token)
        #将json格式的字符串转换成字典
        r=json.loads(res.text)
        print(r)
        #校验接口
        self.assertTrue(r['status']==0 and len(r['data'].get('list'))>0,msg='测试失败！！！')

if __name__ == '__main__':
    unittest.main()
