#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import unittest
import warnings
from login.templates.platform.common.Login_Platform import login_platform
from login.templates.utils import getconf, httputils, dbutil
from login.templates.utils.confutils import  getPlatformName


class case_NecPlatform_Audio_GetAlbumInfoList(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning) #忽略ResourceWarning提示

    def test_necplatform_audio_get_album_info_list(self):
        """获取听书号的我的节目模块的节目信息"""
        # 登录并获取token
        platform_token = login_platform()
        # 获取platform接口url
        getAlbumInfoList=getPlatformName('getAlbumInfoList')
        #入参
        params={'state':-1,'pageNum':1,'pageSize':20}
        #调用接口
        res=httputils.get_platforms(getAlbumInfoList,params,platform_token)
        #将json格式的字符串转换成字典
        r=json.loads(res.text)
        print(r)
        #校验接口
        self.assertTrue(r['status']==0 and len(r['data'])>0,msg='测试失败！！！')

if __name__ == '__main__':
    unittest.main()
