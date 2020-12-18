#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import random
import unittest
from time import sleep
from login.templates.admin.account.adminlogin import login_admin
from login.templates.utils import getconf, httputils, dbutil
from login.templates.utils.confutils import getcurrentPath, getAdminName


class case_NecPlatform_Billing_Billing_Info_Approval_List(unittest.TestCase):

    def test_necplatform_billing_billing_info_approval_list(self):
        """结算信息审核列表页"""
        # 登录并获取token
        admin_token = login_admin()
        # 获取admin接口url
        billingInfoApprovalList=getAdminName('billingInfoApprovalList')
        #获取前端页面的url
        billingAudit_list=getcurrentPath('billingAudit_list')
        #入参
        data={'pageSize': 20,
            'pageNum': 1,
            'cooperatorType': -1,
            'status': 2}
        #调用接口
        res=httputils.getadmin(billingInfoApprovalList,data,admin_token,billingAudit_list)
        sleep(1)
        #将json格式的字符串转换成字典
        r=json.loads(res.text)
        print(r)
        #校验接口请求是否成功
        self.assertTrue(r['status']==0,msg='测试失败！！！')

    def test_platform_billing_billing_info_approval_copyright_list(self):
        """结算信息审核版权列表页"""
        # 登录并获取token
        admin_token = login_admin()
        # 获取admin接口url
        billingInfoApprovalList=getAdminName('billingInfoApprovalList')
        #获取前端页面的url
        billingAudit_list=getcurrentPath('billingAudit_list')
        #入参
        data={'pageSize': 20,
            'pageNum': 1,
            'cooperatorType': 2,
            'status': 2}
        #调用接口
        res=httputils.getadmin(billingInfoApprovalList,data,admin_token,billingAudit_list)
        sleep(1)
        #将json格式的字符串转换成字典
        r=json.loads(res.text)
        print(r)
        #校验接口请求是否成功
        self.assertTrue(r['status']==0,msg='测试失败！！！')
    def test_platform_billing_billing_info_approval_Anchor_list(self):
        """结算信息审核主播列表页"""
        # 登录并获取token
        admin_token = login_admin()
        # 获取admin接口url
        billingInfoApprovalList=getAdminName('billingInfoApprovalList')
        #获取前端页面的url
        billingAudit_list=getcurrentPath('billingAudit_list')
        #入参
        data = {'pageSize': 20,
                'pageNum': 1,
                'cooperatorType': 3,
                'status': 2}
        #调用接口
        res=httputils.getadmin(billingInfoApprovalList,data,admin_token,billingAudit_list)
        sleep(1)
        #将json格式的字符串转换成字典
        r=json.loads(res.text)
        print(r)
        #校验接口请求是否成功
        self.assertTrue(r['status']==0,msg='测试失败！！！')
    def test_platform_billing_billing_info_approval_channel_list(self):
        """结算信息审核渠道列表页"""
        # 登录并获取token
        admin_token = login_admin()
        # 获取admin接口url
        billingInfoApprovalList=getAdminName('billingInfoApprovalList')
        #获取前端页面的url
        billingAudit_list=getcurrentPath('billingAudit_list')
        #入参
        data = {'pageSize': 20,
                'pageNum': 1,
                'cooperatorType': 1,
                'status': 2}
        #调用接口
        res=httputils.getadmin(billingInfoApprovalList,data,admin_token,billingAudit_list)
        sleep(1)
        #将json格式的字符串转换成字典
        r=json.loads(res.text)
        print(r)
        #校验接口请求是否成功
        self.assertTrue(r['status']==0,msg='测试失败！！！')




if __name__ == '__main__':
    unittest.main()
