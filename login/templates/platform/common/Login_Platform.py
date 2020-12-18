import json
from login.templates.utils import httputils, getconf
from login.templates.utils.confutils import getAdminName, getPlatformName
from login.templates.utils.encodeutils import encrypt_des
from login.templates.utils.getconf import get_conf, write_config_ini


def check_paltform_token_by_get_userinfo(platform_token):
    """
    检查token是否有效
    :param platform_token:
    :return:
    """
    r = httputils.get_platforms(getPlatformName('getUserBasicInfo'),
                                {},
                                platform_token,
                                )
    result = json.loads(r.text)
    if result['status'] == 0:
        return 0
    else:
        return 1


def platform_get_login_token(username=get_conf('users', 'platform_phone')):
    """
    听书号登录获取公钥(token)
    :return:
    """
    r = httputils.get_paltforms_login('/ajax/getLoginToken', {'accountName': username})
    token = json.loads(r.text)['data']['token']
    print('平台获取的token',token)
    return token


def login_platform(username=get_conf('users', 'platform_phone'), pwd=get_conf('users', 'platform_pwd')):
    """
    听书号登录获取token(私钥）
    :return:
    """
    platform_token = get_conf('admin', 'platform_token')
    check_code=check_paltform_token_by_get_userinfo(platform_token)
    print('CheckCode:调用接口获取为1，否则0:', check_code)
    if check_code == 1 or username != get_conf('users', 'platform_phone'):
        # 前端密码加密
        splatform = platform_get_login_token()
        encrypt_pwd = encrypt_des(splatform, pwd)
        paltform_domain = get_conf('HOST', 'platform_domain')
        print('username',username)
        r = httputils.post_platform(paltform_domain, '/ajax/login',
                                    {'accountName': username, 'pwd': encrypt_pwd},
                                    {
                                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
                                        'Content-Type': 'application/json;charset=UTF-8',
                                        })
        token_got = json.loads(r.text)['data']['token']
        print('获取的token', token_got)
        if token_got is not None:
            write_config_ini('admin', "platform_token", token_got)
            return token_got
        else:
            r1 = httputils.post_platform(paltform_domain, '/ajax/loginForSms',
                                         {'phone': getconf.get_conf('users', 'platform_phone'), 'smsKey': '0000'
                                          },
                                         {
                                             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
                                             'Content-Type': 'application/json;charset=UTF-8',
                                             'Accept': 'application/json, text/plain, */*'})
            token_got1 = json.loads(r1.text)['data']['token']
            print('获取的token', token_got)
            if token_got1:
                write_config_ini('admin', "platform_token", token_got1)
                return token_got1
    else:
        print('获取的token', platform_token)
        return platform_token

if __name__=='__main__':
    login_platform()
