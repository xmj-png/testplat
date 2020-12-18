#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import random
import unittest
from time import sleep
from login.templates.admin.account.adminlogin import login_admin
from login.templates.utils import getconf, httputils, dbutil
from login.templates.utils.confutils import getcurrentPath, getAdminName


class case_NecPlatform_Billing_Billing_Platform_List(unittest.TestCase):

    def test_necplatform_billing_billing_platform_list(self):
        """分成听书号列表页"""
        # 登录并获取token
        admin_token = login_admin()
        # 获取admin接口url
        billingPlatformList=getAdminName('billingPlatformList')
        #获取前端页面的url
        splitList=getcurrentPath('splitList')
        #入参
        params={'pageSize': 20,
                'pageNum': 1,
                'cooperatorType': -1,
                'status': -1,
                'userType': -1}
        #调用接口
        res=httputils.getadmin(billingPlatformList,params,admin_token,splitList)
        sleep(0.1)
        #将json格式的字符串转换成字典
        r=json.loads(res.text)
        print(r)
        #校验接口请求是否成功
        self.assertTrue(r['status']==0 and len(r['data']['list'])>0,msg='测试失败！！！')
    def test_platform_billing_billing_platform_copyrigiht_list(self):
        """分成听书号列表页(版权)"""
        # 登录并获取token
        admin_token = login_admin()
        # 获取admin接口url
        billingPlatformList=getAdminName('billingPlatformList')
        #获取前端页面的url
        splitList=getcurrentPath('splitList')
        #入参
        params={'pageSize': 20,
                'pageNum': 1,
                'cooperatorType': 2,
                'status': -1,
                'userType': -1}
        #调用接口
        res=httputils.getadmin(billingPlatformList,params,admin_token,splitList)
        sleep(0.1)
        #将json格式的字符串转换成字典
        r=json.loads(res.text)
        print(r)
        #校验接口请求是否成功
        self.assertTrue(r['status']==0 and len(r['data']['list'])>0,msg='测试失败！！！')
    def test_platform_billing_billing_platform_copyrigiht_anchor_list(self):
        """分成听书号列表页(主播)"""
        # 登录并获取token
        admin_token = login_admin()
        # 获取admin接口url
        billingPlatformList=getAdminName('billingPlatformList')
        #获取前端页面的url
        splitList=getcurrentPath('splitList')
        #入参
        params={'pageSize': 20,
                'pageNum': 1,
                'cooperatorType': 3,
                'status': -1,
                'userType': -1}
        #调用接口
        res=httputils.getadmin(billingPlatformList,params,admin_token,splitList)
        sleep(0.1)
        #将json格式的字符串转换成字典
        r=json.loads(res.text)
        print(r)
        #校验接口请求是否成功
        self.assertTrue(r['status']==0 and len(r['data']['list'])>0,msg='测试失败！！！')
    def test_platform_billing_billing_platform_copyrigiht_channel_list(self):
        """分成听书号列表页(渠道)"""
        # 登录并获取token
        admin_token = login_admin()
        # 获取admin接口url
        billingPlatformList=getAdminName('billingPlatformList')
        #获取前端页面的url
        splitList=getcurrentPath('splitList')
        #入参
        params={'pageSize': 20,
                'pageNum': 1,
                'cooperatorType': 1,
                'status': -1,
                'userType': -1}
        #调用接口
        res=httputils.getadmin(billingPlatformList,params,admin_token,splitList)
        sleep(0.1)
        #将json格式的字符串转换成字典
        r=json.loads(res.text)
        print(r)
        #校验接口请求是否成功
        self.assertTrue(r['status']==0 and len(r['data']['list'])>0,msg='测试失败！！！')

if __name__ == '__main__':
    unittest.main()
