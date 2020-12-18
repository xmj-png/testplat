#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import random
import unittest
from time import sleep
from login.templates.admin.account.adminlogin import login_admin
from login.templates.utils import getconf, httputils, dbutil
from login.templates.utils.confutils import getcurrentPath, getAdminName


class case_Platform_Billing_Member_Share_Resource_List(unittest.TestCase):

    def test_platform_billing_member_share_resource_list(self):
        """会员分成资源管理列表页"""
        # 登录并获取token
        admin_token = login_admin()
        # 获取admin接口url
        memberShareList=getAdminName('memberShareList')
        #获取前端页面的url
        memberShareList_page=getcurrentPath('memberSplitResourceList')
        #入参
        data={'pageSize':'20',
            'pageNum':'1',
            'resourceType':'-1',
            'expireStatus':'-1'}
        #调用接口
        res=httputils.getadmin(memberShareList,data,admin_token,memberShareList_page)
        sleep(1)
        #将json格式的字符串转换成字典
        r=json.loads(res.text)
        print(r)
        #校验接口请求是否成功
        self.assertTrue(r['status']==0 and len(r['list'])>0,msg='测试失败！！！')



if __name__ == '__main__':
    unittest.main()
