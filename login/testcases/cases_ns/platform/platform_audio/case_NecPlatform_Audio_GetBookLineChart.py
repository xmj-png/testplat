#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import unittest
import warnings
from login.templates.platform.common.Login_Platform import login_platform
from login.templates.utils import getconf, httputils, dbutil
from login.templates.utils.confutils import  getPlatformName


class case_NecPlatform_Audio_Get_Book_Line_Chart(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning) #忽略ResourceWarning提示

    def test_necplatform_audio_get_book_line_chart_jiaoyin(self):
        """获取听书号-数据中心-数据总览交音统计"""
        # 登录并获取token
        platform_token = login_platform()
        # 获取platform接口url
        getBookLineChart=getPlatformName('getBookLineChart')
        #入参
        params={
             'countType': 1,
             'type': 1
        }
        #调用接口
        res=httputils.get_platforms(getBookLineChart,params,platform_token)
        #将json格式的字符串转换成字典
        r=json.loads(res.text)
        print(r)
        #校验接口
        self.assertTrue(r['status']==0 and len(r['data'].get('list'))>0,msg='测试失败！！！')
    def test_necplatform_audio_get_book_line_chart_shenting(self):
        """获取听书号-数据中心-数据总览审听统计"""
        # 登录并获取token
        platform_token = login_platform()
        # 获取platform接口url
        getBookLineChart=getPlatformName('getBookLineChart')
        #入参
        params={
             'countType': 2,
             'type': 3
        }
        #调用接口
        res=httputils.get_platforms(getBookLineChart,params,platform_token)
        #将json格式的字符串转换成字典
        r=json.loads(res.text)
        print(r)
        #校验接口
        self.assertTrue(r['status']==0 and len(r['data'].get('list'))>0,msg='测试失败！！！')
    def test_necplatform_audio_get_book_line_chart_houqi(self):
        """获取听书号-数据中心-数据总览后期统计"""
        # 登录并获取token
        platform_token = login_platform()
        # 获取platform接口url
        getBookLineChart=getPlatformName('getBookLineChart')
        #入参
        params={
             'countType': 3,
             'type': 3
        }
        #调用接口
        res=httputils.get_platforms(getBookLineChart,params,platform_token)
        #将json格式的字符串转换成字典
        r=json.loads(res.text)
        print(r)
        #校验接口
        self.assertTrue(r['status']==0 and len(r['data'].get('list'))>0,msg='测试失败！！！')

if __name__ == '__main__':
    unittest.main()
