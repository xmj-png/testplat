'''
阅读书籍相关操作
'''
import json
from random import choice

from login.templates.admin.account.adminlogin import login_admin
from login.templates.utils import httputils
from login.templates.utils.confutils import getAdminName, getcurrentPath
from login.templates.utils.dbutil import select
from login.templates.utils.utils import dec_To_Bin



class readbook_operation():
    '''阅读书籍操作类'''
    @staticmethod
    def get_readbook_info(readbook_id):
        '''获取阅读书籍信息
        :param readbook_id 阅读书籍id
        :return dict
        '''
        res  = httputils.getadmin(getAdminName('readBookInfo'),
                                  {'id':readbook_id},
                                  login_admin(),
                                  getcurrentPath('ReadBookEdit'))
        json_res = json.loads(res.text)
        print(json_res)
        #初始化一个字典
        readbookinfo = {}
        if json_res['status']==0:
            readbookinfo['bookId']=readbook_id
            readbookinfo['readOutBookId']=json_res['data']['readOutBookId']
            readbookinfo['bookName']=json_res['data'].get('bookName')
            readbookinfo['desc']=json_res['data'].get('desc')
            if json_res['data']['typeList']:
                readbookinfo['typeId']=json_res['data']['typeList'][0].get('typeId')
            else:
                readbookinfo['typeId'] =''
            if json_res['data']['authorList']:
                authorList_size=len(json_res['data']['authorList'])
                readbookinfo['userId']=json_res['data']['authorList'][authorList_size-1].get('userId')
            else:
                readbookinfo['userId'] = ''
            # readbookinfo['typeName'] = json_res['data']['typeList'][0].get('typeName')
            # if json_res['data'].get('author') is None:
            #     readbookinfo['author']=''
            # else:
            #     readbookinfo['author']=json_res['data'].get('author')
            readbookinfo['orgId']=json_res['data'].get('orgId')
            readbookinfo['contentState']=json_res['data'].get('contentState')#1连载 2完结 3停止更新
            # readbookinfo['sections']=json_res['data'].get('sections')#章节数
            if json_res['data'].get('recReason'):
                readbookinfo['recReason']=json_res['data'].get('recReason')#长的推荐理由
            else:
                readbookinfo['recReason'] = ''
            readbookinfo['shortRecReason']=json_res['data'].get('shortRecReason')#短的推荐理由
            readbookinfo['state']=json_res['data'].get('state') #0下线 1上线
            readbookinfo['timeLimitedFree']=json_res['data'].get('timeLimitedFree')
            readbookinfo['freeSections']=json_res['data'].get('freeSections')
            readbookinfo['priceType']=json_res['data']['priceInfo'].get('intPriceType')
            readbookinfo['price']=json_res['data'].get('wordsPriceY')
            readbookinfo_marketingList=json_res['data'].get('marketingList')
            # marketing_names = ''
            marketing_ids = ''
            for i in range(len(readbookinfo_marketingList)):
                # marketing_names+=readbookinfo_marketingList[i].get('name')+','
                marketing_ids+=str(readbookinfo_marketingList[i].get('id'))+','
            # readbookinfo['marketingList_name']=marketing_names.rstrip(',')
            readbookinfo['marketingList']=marketing_ids.rstrip(',')
            censor_flag = json_res['data'].get('censorFlag')
            bin_code = dec_To_Bin(censor_flag)
            print(bin_code)
            if bin_code[0] == '0':
                readbookinfo['canNotSearch'] = 'true'
            if bin_code[1] == '0':
                readbookinfo['canNotFuzzySearch'] = 'true'
            if bin_code[2] == '0':
                readbookinfo['canNotRecommendByMen'] = 'true'
            if bin_code[5] == '0':
                readbookinfo['canNotFreeSection'] = 'true'
            if bin_code[6] == '0':
                readbookinfo['canNotBuySection'] = 'true'
            if bin_code[7] == '0':
                readbookinfo['canNotUnBuySection'] = 'true'
            readbookinfo['vipDiscount']=json_res['data'].get('vipDiscount')
            readbookinfo['ticketLimit']=json_res['data'].get('ticketLimit')
            readbookinfo['isDown']=json_res['data'].get('isDown')
            readbookinfo['showReaders']=json_res['data'].get('showReaders')
            readbookinfo['contentLevel']=json_res['data'].get('contentLevel')
            readbookinfo['cover']=json_res['data'].get('cover')
            readbookinfo['coverFormat']='read_book_cover'
            typeIds=''
            if json_res['data']['typeList']:
                for i in range(len(json_res['data']['typeList'])):
                    typeIds+=str(json_res['data']['typeList'][i].get('typeId'))+','
                typeIds=typeIds.rstrip(',')
                readbookinfo['typeIds']=typeIds
            else:
                readbookinfo['typeIds'] = ''
            userIds=''
            if json_res['data']['authorList']:
                for i in range(len(json_res['data']['authorList'])):
                    userIds+=str(json_res['data']['authorList'][i].get('userId'))
                userIds=userIds.rstrip(',')
                readbookinfo['userIds']=userIds
            else:
                readbookinfo['userIds'] = ''
            print(readbookinfo)
            return readbookinfo
    @staticmethod
    def edit_readbook_info(readbook_id,book_kv_dict):
        '''修改阅读书籍信息
        :param readbook_id 阅读书籍id
        :param book_kv_dict 需要修改的字段，类型为dict，例如：{'bookName':'夜色惝恍001'}
        :return 修改成功或失败信息
        '''
        readbook_info = readbook_operation.get_readbook_info(readbook_id)
        if readbook_info['typeId']=='':
            typeIds = select('SELECT type_id FROM audiobook.t_type  where type_id >=5050 and visible_state=0 limit 0,100;','db_audiobook')
            readbook_info['typeId'] = choice(typeIds).get('type_id')
            readbook_info['typeIds'] = choice(typeIds).get('type_id')
        if readbook_info['userId']=='':
            userIds = select("SELECT user_id FROM  audiobook.t_book_user where 'type'=0 limit 100,100;",'db_audiobook')
            readbook_info['userId'] = choice(userIds).get('user_id')
            readbook_info['userIds'] = choice(userIds).get('user_id')
        for k,v in book_kv_dict.items():
            readbook_info[k] = v
        res = httputils.postadmin(getAdminName('readBookEdit'),readbook_info,login_admin(),getcurrentPath('ReadBookEdit'))
        r = json.loads(res.text)
        success_message = "修改阅读书籍:%s的信息%s成功！！"%(readbook_id,book_kv_dict)
        if r.get('status')==0:
            print(success_message)
            return success_message
        else:
            print(r.get('msg'))
            return r.get('msg')



if __name__=='__main__':
    # readbook_operation.get_readbook_info(190868)
    readbook_operation.edit_readbook_info(159510,{'bookName':'你的恰好我的温暖001'})