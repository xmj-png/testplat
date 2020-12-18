import json
import unittest
from random import choice

from login.templates.admin.account.adminlogin import login_admin
from login.templates.app.account.Get_Logon_Token import get_app_login_token
from login.templates.utils import httputils
from login.templates.utils.confutils import getApiName, getAdminName, getcurrentPath


class case_Necessary_Album_Classification_Page_Check(unittest.TestCase):

    def test_Album_Classification_Page_Check(self):
        """节目分类页，数据正常返回"""
        #1、获取admin节目分类
        admin_token = login_admin()
        #调用typeList接口获取节目分类
        r1 = httputils.getadmin(getAdminName('album_typeList'), {'typeCode':2}, admin_token,
                                            getcurrentPath('TypeSnsList'))
        res1 = json.loads(r1.text)
        typeIds = []
        for i in res1['list']:
            typeIds.append(i.get('typeId'))
        select_typeIds = choice(typeIds)
        # 登录并获取app token
        token = get_app_login_token()
        # 第一次请求获取资源筛选数据
        data = {
            'dsize': '20',
            'entityId': select_typeIds,#节目分类：情感
            'token': token,
            'entityType': '1',
            'pageNum': '1',
            'showFilters': '0',
            'mode': '0'
        }
        # 首次请求资源筛选页数据
        r = httputils.get_app(getApiName('filterResources'), data)
        print(r.text)
        self.assertTrue(json.loads(r.text)['albumCount'] > 0 and len(json.loads(r.text)['albums']) > 0 and len(json.loads(r.text)['albumIds']) > 0)

    if __name__ == '__main__':
        unittest.main()
