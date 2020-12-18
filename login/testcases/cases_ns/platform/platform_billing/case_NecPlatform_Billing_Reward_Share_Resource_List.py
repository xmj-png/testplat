#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import random
import unittest
from time import sleep
from login.templates.admin.account.adminlogin import login_admin
from login.templates.utils import getconf, httputils, dbutil
from login.templates.utils.confutils import getcurrentPath, getAdminName


class case_Platform_Billing_Reward_Share_Resource_List(unittest.TestCase):

    def test_platform_billing_reward_share_resource_list(self):
        """打赏分成资源管理列表页"""
        # 登录并获取token
        admin_token = login_admin()
        # 获取admin接口url
        shareFeeResourceList=getAdminName('shareFeeResourceList')
        #获取前端页面的url
        shareFeeResourceList_page=getcurrentPath('ShareFeeResourceList')
        #入参
        data={}
        #调用接口
        res=httputils.getadmin(shareFeeResourceList,data,admin_token,shareFeeResourceList_page)
        sleep(1)
        #将json格式的字符串转换成字典
        r=json.loads(res.text)
        print(r)
        #校验接口请求是否成功
        self.assertTrue(r['status']==0 and len(r['list'])>0,msg='测试失败！！！')



if __name__ == '__main__':
    unittest.main()
