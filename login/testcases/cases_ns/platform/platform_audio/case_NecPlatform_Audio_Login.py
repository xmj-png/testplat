#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import unittest
import warnings
from login.templates.platform.common.Login_Platform import login_platform, platform_get_login_token
from login.templates.utils import getconf, httputils, dbutil
from login.templates.utils.encodeutils import encrypt_des
from login.templates.utils.getconf import get_conf


class case_NecPlatform_Audio_Login(unittest.TestCase):
    env = get_conf('HOST', 'platform_domain')
    print('测试环境:',env)
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning) #忽略ResourceWarning提示



    def test_necplatform_audio_Account_password_login(self):
        """通过账号密码登录听书号"""
        username = get_conf('users', 'platform_phone')
        #登录获取公钥
        splatform = platform_get_login_token(username)
        pwd = get_conf('users', 'platform_pwd')
        # 前端密码加密
        encrypt_pwd = encrypt_des(splatform, pwd)
        paltform_domain = get_conf('HOST', 'platform_domain')
        r = httputils.post_platform(paltform_domain, '/ajax/login',
                                    {'accountName': username, 'pwd': encrypt_pwd},
                                    {
                                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
                                        'Content-Type': 'application/json;charset=UTF-8',
                                    })
        res= json.loads(r.text)
        self.assertTrue(res['status']==0,msg='账号密码登录听书号失败！！！')
    @unittest.skipIf(env=='https://p-a.lrts.me', '条件为True ，用例2跳过')
    def test_necplatform_audio_phone_verification_code_login(self):
        '''通过手机验证码登录听书号'''
        phone = get_conf('users', 'platform_phone')
        paltform_domain = get_conf('HOST', 'platform_domain')
        r1 = httputils.post_platform(paltform_domain, '/ajax/loginForSms',
                                     {'phone': phone, 'smsKey': '0000'
                                      },
                                     {
                                         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
                                         'Content-Type': 'application/json;charset=UTF-8',
                                         'Accept': 'application/json, text/plain, */*'})
        res = json.loads(r1.text)
        self.assertTrue(res['status']==0,msg='手机验证码登录听书号失败！！！')


if __name__ == '__main__':
    unittest.main()
