#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import unittest
import warnings
from login.templates.platform.common.Login_Platform import login_platform
from login.templates.platform.settlement.get_CurrentTime import before_today
from login.templates.utils import getconf, httputils, dbutil
from login.templates.utils.confutils import  getPlatformName


class case_NecPlatform_Audio_Get_Play_Statistic(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning) #忽略ResourceWarning提示

    def test_necplatform_audio_get_play_statistic(self):
        """获取听书号-数量中心-数据总览播放统计信息"""
        # 登录并获取token
        platform_token = login_platform()
        # 获取platform接口url
        getPlayStatistic=getPlatformName('getPlayStatistic')
        #入参
        params={'type': 1,
                'countType': 1,
                'startTime': before_today(-7),
                'endTime': before_today(-1)}
        #调用接口
        res=httputils.get_platforms(getPlayStatistic,params,platform_token)
        #将json格式的字符串转换成字典
        r=json.loads(res.text)
        print(r)
        #校验接口
        self.assertTrue(r['status']==0 and len(r['data'].get('list'))>0,msg='测试失败！！！')

if __name__ == '__main__':
    unittest.main()
