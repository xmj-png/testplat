#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import random

from login.templates.app.account.Get_Logon_Token import get_app_login_token
from login.templates.utils import getconf, httputils, dbutil
from login.templates.utils.dbutil import select
from login.templates.utils.utils import ranstr, random_chinese


def test_listeningList_add_books(username,password):
    """创建听单，并加入100本书籍"""
    token = get_app_login_token(str(username),str(password)) #登录获取token
    # 数据准备
    folder_name = random_chinese(4)+ranstr(2)
    data1={
        'id':'0',
        'name':folder_name,
        'token': token,
        'mode': '0'
    }
    #调用接口添加听单
    r1=httputils.get_app(getconf.get_global_conf('apinames', 'addFolder.action'), data1)
    res1=json.loads(r1.text)
    if res1['status']==0:
        folderId=res1['data'].get('folderId')
        print(type(folderId))
        print('听单Id:',folderId)
        '''往听单里加书籍'''
        #查询数据库在线的500本书籍
        books=select("SELECT book_id FROM t_book  WHERE bState=0 LIMIT 1000","db_audiobook")
        #从1000本书籍中选择100本书籍
        ran_list=random.sample(books,100)
        print(ran_list)
        #往听单里加书籍
        for book_id_dict in ran_list:
            data2={
                'list':str({"list":[{"srcType":'3',"srcEntityId":str(book_id_dict['book_id']),"opType":'0',"folderId":str(folderId),"createTime":"2020-09-01 19:15:48"}]}),
                'token':token,
                'mode':"0"
            }
            #调用接口往听单新增书籍
            r2=httputils.get_app(getconf.get_global_conf('apinames', 'ClientAddConllection'), data2)
            res2=json.loads(r2.text)
            print(res2)
        print("听单:" + folder_name + " 成功加入100本书籍！！！")
        return {'folder_name':folder_name}
    else:
        print('听单创建失败！！！')

if __name__ == '__main__':
    test_listeningList_add_books(15879790216,123456)