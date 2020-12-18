#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import random
import unittest
from time import sleep
from login.templates.admin.account.adminlogin import login_admin
from login.templates.utils import getconf, httputils, dbutil
from login.templates.utils.confutils import getcurrentPath, getAdminName


class case_Platform_Billing_Member_Grade_List(unittest.TestCase):

    def test_platform_billing_member_grade_list(self):
        """公司补贴级别系数列表页"""
        # 登录并获取token
        admin_token = login_admin()
        # 获取admin接口url
        billing_memberGradeList=getAdminName('billing_memberGradeList')
        #获取前端页面的url
        rewardFactor_list=getcurrentPath('rewardFactor_list')
        #入参
        data={'pageSize':20,'pageNum':1}
        #调用接口
        res=httputils.getadmin(billing_memberGradeList,data,admin_token,rewardFactor_list)
        sleep(1)
        #将json格式的字符串转换成字典
        r=json.loads(res.text)
        print(r)
        #校验接口请求是否成功
        self.assertTrue(r['status']==0 and len(r['list'])>0,msg='测试失败！！！')



if __name__ == '__main__':
    unittest.main()
