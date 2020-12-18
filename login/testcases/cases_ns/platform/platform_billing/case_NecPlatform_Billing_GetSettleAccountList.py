#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import unittest
import warnings
from time import sleep
from login.templates.platform.common.Login_Platform import login_platform
from login.templates.platform.settlement.get_CurrentTime import before_today, getCurrentTime, before_month
from login.templates.utils import getconf, httputils, dbutil
from login.templates.utils.confutils import  getPlatformName


class case_NecPlatform_Audio_GetSettleAccountList(unittest.TestCase):
    def setUp(self):
        # 忽略ResourceWarning提示
        warnings.simplefilter('ignore', ResourceWarning)

    def test_necplatform_audio_get_settle_account_list(self):
        """获取听书号-收益中心-对账结算页数据"""
        # 登录并获取token
        platform_token = login_platform()
        # 获取platform接口url
        getSettleAccountList=getPlatformName('getSettleAccountList')
        #入参
        settlement_time = before_month()
        year = settlement_time[0]
        month = settlement_time[1]
        print(year,month)
        params={
                'partnerId': -1,
                'serviceType': 2,
                'year': year,
                'month': month
                }
        #调用接口
        res=httputils.get_platforms(getSettleAccountList,params,platform_token)
        #将json格式的字符串转换成字典
        r=json.loads(res.text)
        print(r)
        #校验接口
        self.assertTrue(r['status']==0 and len(r['data'])>0 ,msg='测试失败！！！')

if __name__ == '__main__':
    unittest.main()
