#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/10 14:38
# @Author  : caozhuo
# @FileName: case_Necessary_Search_Album.py
# @Software: PyCharm

import json
import unittest
from random import choice
from time import sleep

from login.templates.admin.albumn.Albumn_Operation import get_album_info_dict, edit_album_info_by_dict
from login.templates.app.account.Get_Logon_Token import get_app_login_token
from login.templates.utils import httputils, dbutil
from login.templates.utils.confutils import getApiName


class case_Necessary_Change_Album_Descripiton(unittest.TestCase):

    def test_change_album_description(self):
        '''修改节目的描述'''
        # 查询数据库获取节目id
        # albums_ids = dbutil.select('SELECT * FROM audiobook.t_sns_ablumn where status=0 and wait_offline =0 limit 100,100;', 'db_audiobook')
        albums_ids =['59702','80026','8727','20526']
        print('albums_id',albums_ids)
        if albums_ids:
            album_id = choice(albums_ids)
            print(type(album_id))
        #调用admin接口获取节目信息
        album_info = get_album_info_dict(album_id)
        sleep(0.5)
        description = album_info.get('description')
        if description is None:
            description = ''
        #调用admin接口修改节目信息
        changed_album_description = description+'AutoTest01'
        r=edit_album_info_by_dict(album_id,{'description':changed_album_description})
        print(r)
        sleep(1)
        #调用api接口查看节目的描述是否修改
        data = {
                'ablumnId':album_id,
                'token':get_app_login_token(),
                'mode':0
                }
        r = httputils.get_app(getApiName('ablumnDetailPage'), data)
        sleep(2)
        # 状态校验
        self.assertEqual(r.status_code, 200, '请求失败')
        self.assertEqual(json.loads(r.text)['status'], 0, '请求失败')
        # 返回值校验
        res = json.loads(r.text)['data']['ablumnDetail']['ablumn']['description']
        print(res)
        print(changed_album_description)
        self.assertEqual(res,changed_album_description, '节目描述修改未生效！！！')
        #数据还原
        origin_description = description
        edit_album_info_by_dict(album_id, {'description': origin_description})


if __name__ == '__main__':
    unittest.main()
