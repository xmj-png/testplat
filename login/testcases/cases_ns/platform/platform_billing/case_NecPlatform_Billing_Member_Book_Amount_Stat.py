#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import unittest
from time import sleep
from login.templates.admin.account.adminlogin import login_admin
from login.templates.utils import getconf, httputils, dbutil
from login.templates.utils.confutils import getcurrentPath, getAdminName


class case_Platform_Billing_Member_Book_Amount_Stat(unittest.TestCase):

    def test_platform_billing_member_book_amount_stat(self):
        """会员资源收入统计列表"""
        # 登录并获取token
        admin_token = login_admin()
        # 获取admin接口url
        memberBookAmountStat=getAdminName('memberBookAmountStat')
        #获取前端页面的url
        memberBookAmountStat_page=getcurrentPath('memberIncomeStat')
        #入参
        params={'pageSize':'20','pageNum':'1','productType':'1',
                'entityType':'1','copyrightId':'0','year':'0','month':'0',
                'searchType':'0','orderBy':'1','fatherTypeId':'-1','sonTypeId':'-1'}
        #调用接口
        res=httputils.getadmin(memberBookAmountStat,params,admin_token,memberBookAmountStat_page)
        sleep(1)
        #将json格式的字符串转换成字典
        r=json.loads(res.text)
        print(r)
        #校验接口请求是否成功
        self.assertTrue(r['status']==0,msg='测试失败！！！')



if __name__ == '__main__':
    unittest.main()
