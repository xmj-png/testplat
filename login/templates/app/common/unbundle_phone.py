import json

import requests

from login.templates.admin.account.adminlogin import login_admin
from login.templates.utils import httputils
from login.templates.utils.confutils import getAdminName, getcurrentPath
from login.templates.utils.dbutil import select


def unbundle_phone(userId,phone):
    '''解绑手机号'''
    admin_token = login_admin()
    # 入参
    userid=str(userId)
    phone=str(phone)
    #获取user_id最后一位数
    id = userid[-1:]
    result = select('SELECT * FROM audiobook.t_user_ext_%s where user_id =%s and phone_num=%s;'%(id,userid,phone),'db_audiobook')
    print('result:',result)
    if result:
        param = {
                'checkCode':'admin98712',
                'phoneNum':phone,
                'userId':userid
        }
        r= httputils.getadmin(getAdminName('unbindPhoneNumTools'),
                               param,
                               admin_token,
                               getcurrentPath('main'))
        res = json.loads(r.text)

        if res['status']==0:
            print(res['msg'])
            return 1
        else:
            print(res['msg'])
            return 0
    else:
        print('手机号和用户id不匹配！！')
        return -1

if __name__=='__main__':
    unbundle_phone(676658025,14757694922)
