#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import unittest
import warnings
from login.templates.platform.common.Login_Platform import login_platform
from login.templates.platform.settlement.get_CurrentTime import before_today
from login.templates.utils import getconf, httputils, dbutil
from login.templates.utils.confutils import  getPlatformName


class case_NecPlatform_Billing_GetIncomeOverviewStat(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning) #忽略ResourceWarning提示

    def test_necplatform_Billing_get_income_overview_stat(self):
        """获取听书号-收益中心-总体概况页流水数据"""
        # 登录并获取token
        platform_token = login_platform()
        # 获取platform接口url
        getIncomeOverviewStat=getPlatformName('getIncomeOverviewStat')
        #入参
        params={}
        #调用接口
        res=httputils.get_platforms(getIncomeOverviewStat,params,platform_token)
        #将json格式的字符串转换成字典
        r=json.loads(res.text)
        print(r)
        #校验接口
        self.assertTrue(r['status']==0 and len(r['data'])>0,msg='测试失败！！！')

if __name__ == '__main__':
    unittest.main()
