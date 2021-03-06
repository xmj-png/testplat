import random
from time import sleep

from login.templates.admin.account.adminlogin import login_admin
from login.templates.utils import httputils, confutils
from login.templates.utils.confutils import getAdminName
import json

from login.templates.utils.dbutil import select


def charge_for_coin(coin_type: str, amount: str, user_id: str, payType: str,channel: str):
    """
    懒人币充值申请
    :param coin_type:0-安卓,1-ios
    :param amount:
    :param user_id:
    :return:
    """
    # 发起申请
    order_id = random.randint(10000000000,99999999999)
    data = {
        'srcUserIds': user_id,
        'coinType': coin_type,
        'addCoin': amount,
        'reasonSelect':'用户充值丢失补偿',
        'reason': 'auto_test',
        'outOrderNo':order_id,
        'channel': channel,
        'payType': str(payType)
    }
    r = httputils.postadmin(getAdminName('operationRecordBathEdit'),
                            data,
                            login_admin(),
                            confutils.getcurrentPath('OperationRecordBatchEdit'))
    print(r.text)
    res_json = json.loads(r.text)
    if res_json['status'] == 0:
        return user_id
    else:
        return False


def get_audit_list(user_id):
    """
    获取充值list
    :return:
    """
    super_admin_token = login_admin('admin', 'www.lrts.me')
    data = {
        'recordStatus': '0',
        'searchKey': user_id,
        'searchField': '0'
    }
    r = httputils.postadmin(getAdminName('operationRecordList'),
                            data,
                            super_admin_token,
                            confutils.getcurrentPath('OperationRecordList'))
    print(r.text)
    res_json = json.loads(r.text)
    count = len(res_json['list'])
    last_id = res_json['list'][int(count) - 1]['id']
    print('最后添加的申请ID', last_id)
    return {'last_id': str(last_id), 'super_admin_token': super_admin_token}


def approve_coin_charge(recordId, super_admin_token):
    """
    审核充值
    :param super_admin_token:
    :param recordId:
    :return:
    """
    data = {
        'recordId': recordId,
        'remark': 'auto',
        'isAccept': 'true'
    }
    r = httputils.postadmin(getAdminName('operationRecordAuditEdit'),
                            data,
                            super_admin_token,
                            confutils.getcurrentPath('OperationRecordList'))
    print(r.text)
    res_json = json.loads(r.text)
    if res_json['status'] == 0:
        return True
    else:
        return False


def charge_coin_to_user(coin_type: str, amount: str, user_id: str,payType: str,channel: str):
    """
       懒人币充值
       :param coin_type:0-安卓,1-ios
       :param amount:
       :param user_id:
       :return:
       """
    # 发起申请
    apply = charge_for_coin(coin_type, amount, user_id, payType, channel)
    if apply:
        audits = get_audit_list(user_id)
        print('超级管理员', audits)
        flag = approve_coin_charge(audits.get('last_id'), audits.get('super_admin_token'))
        if flag:
            user_id_xx = apply[-2:]
            order_id = select('SELECT id FROM audiobook.w_order_%s wo where user_id =%s and order_type =1 and status =1 order by create_time DESC limit 1 ;'%(user_id_xx,apply),'db_audiobook')
            if order_id:
                print('充值成功！！')
                return order_id[0].get('id')
            else:
                return 1
        else:
            return '审核失败'
    else:
        return '申请失败'
