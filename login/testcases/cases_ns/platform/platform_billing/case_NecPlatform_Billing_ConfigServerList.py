#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import random
import unittest
from time import sleep
from login.templates.admin.account.adminlogin import login_admin
from login.templates.utils import getconf, httputils, dbutil
from login.templates.utils.confutils import getcurrentPath, getAdminName


class case_NecPlatform_Billing_ConfigServerList(unittest.TestCase):

    def test_necplatform_billing_config_server_list(self):
        """会员分成参数列表页"""
        # 登录并获取token
        admin_token = login_admin()
        # 获取admin接口url
        configServerList=getAdminName('configServerList')
        #获取前端页面的url
        memberSplitParams=getcurrentPath('memberSplitParams')
        #入参
        data={'type':'VIP_BILLING'}
        #调用接口
        res=httputils.getadmin(configServerList,data,admin_token,memberSplitParams)
        sleep(1)
        #将json格式的字符串转换成字典
        r=json.loads(res.text)
        print(r)
        #校验接口请求是否成功
        self.assertTrue(r['status']==0 and len(r['list'])>0,msg='测试失败！！！')



if __name__ == '__main__':
    unittest.main()
