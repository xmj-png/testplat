import os
import yaml
from login.templates.utils import getconf
from login.templates.utils.getconf import write_config_ini


def getApiName(apiname):
    """
    获取apiname
    :param apiname:
    :return:api路径
    """
    return getconf.get_global_conf('apinames', apiname)


def getAdminName(adminapiname):
    """
    获取adminapiname
    :param apiname:
    :return:adminapi路径
    """
    return getconf.get_global_conf('adminapis', adminapiname)

def getPlatformName(platform_api_name):
    """
    获取adminapiname
    :param apiname:
    :return:adminapi路径
    """
    return getconf.get_global_conf('platform_apis', platform_api_name)


def getcurrentPath(current_apiname):
    """
    获取currentPath
    :param apiname:
    :return:currentPath路径
    """
    return getconf.get_global_conf('currentPath', current_apiname)


def get_private_key():
    """
    获取私钥
    :return:
    """
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with open(path + '\\config\\private_key.pem') as pk:
        key_data = pk.read()
        return key_data


def get_public_key():
    """
    获取公钥钥
    :return:
    """
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with open(path + '\\config\\public_key.pem') as pk:
        key_data = pk.read()
        return key_data


def init_configs(host_name):
    """
    环境配置初始化
    :param host_name:
    :return:
    """
    if host_name in ['mars','earth','moon']:
        host_api = 'http://'+host_name+'-api.mting.info'
        host_admin = 'http://'+host_name+'-admin.lrts.me'
        host_advert = 'http://'+host_name+'-advert.mting.info'
        host_paltform = 'http://'+host_name+'-a.lrts.me'
        # host_names = host_name.split(',')
        write_config_ini('HOST', 'apidomain', host_api)
        write_config_ini('HOST', 'admindomain', host_admin)
        write_config_ini('HOST', 'apidomain_advert', host_advert)
        write_config_ini('HOST', 'platform_domain', host_paltform)
    else:
        host_api = 'http://ps.mting.info'
        host_admin = 'https://padmin.lrts.me'
        host_advert = 'http://p-advert-api.mting.info'
        host_paltform = 'https://p-a.lrts.me'
        # host_names = host_name.split(',')
        write_config_ini('HOST', 'apidomain', host_api)
        write_config_ini('HOST', 'admindomain', host_admin)
        write_config_ini('HOST', 'apidomain_advert', host_advert)
        write_config_ini('HOST', 'platform_domain', host_paltform)

    if 'earth' in host_name:
        #audiobook数据库
        write_config_ini('mysql', 'host', '172.16.6.2')
        #platform数据库
        write_config_ini('mysql_platform', 'host', '172.16.6.3')
        # billing数据库
        write_config_ini('mysql_billing', 'host', '172.16.6.3')
        # readbook数据库
        write_config_ini('mysql_readbook', 'host', '172.16.6.3')
        # yystory数据库
        write_config_ini('mysql_yystory', 'host', '172.16.6.3')
        # 修改数据库除ip地址之外的配置
        change_mysql_connect_info()
    elif 'moon' in host_name:
        # audiobook数据库
        write_config_ini('mysql', 'host', '172.16.7.2')
        # platform数据库
        write_config_ini('mysql_platform', 'host', '172.16.7.3')
        # billing数据库
        write_config_ini('mysql_billing', 'host', '172.16.7.3')
        # readbook数据库
        write_config_ini('mysql_readbook', 'host', '172.16.7.3')
        # yystory数据库
        write_config_ini('mysql_yystory', 'host', '172.16.7.3')
        #修改数据库除ip地址之外的配置
        change_mysql_connect_info()
    elif 'mars' in host_name:
        # audiobook数据库
        write_config_ini('mysql', 'host', '172.16.9.2')
        # platform数据库
        write_config_ini('mysql_platform', 'host', '172.16.9.3')
        # billing数据库
        write_config_ini('mysql_billing', 'host', '172.16.9.3')
        # readbook数据库
        write_config_ini('mysql_readbook', 'host', '172.16.9.3')
        # yystory数据库
        write_config_ini('mysql_yystory', 'host', '172.16.9.3')
        # 修改数据库除ip地址之外的配置
        change_mysql_connect_info()
    elif 'build' in host_name:
        # audiobook数据库
        write_config_ini('mysql', 'host', '192.168.1.51')
        write_config_ini('mysql', 'port', '3306')
        write_config_ini('mysql', 'username', 'readonly')
        write_config_ini('mysql', 'password', 'aoiwhII&j@iwg##wiMbquwu!wiPwuBMq')
        # platform数据库
        write_config_ini('mysql_platform', 'host', 'plus-r.mysql.lrts.me')
        write_config_ini('mysql_platform', 'port', '3306')
        write_config_ini('mysql_platform', 'username', 'platform_read')
        write_config_ini('mysql_platform', 'password', 'Ycnsr,,R02.zsr:#C4]Rin:sri8')
        # billing数据库
        write_config_ini('mysql_billing', 'host', 'plus-r.mysql.lrts.me')
        write_config_ini('mysql_billing', 'port', '3306')
        write_config_ini('mysql_billing', 'username', 'billing_r')
        write_config_ini('mysql_billing', 'password', 'NKwiwcnwi#Cnmwi!]Rinwui==Unciwg9248gwbw82u')
        # readbook数据库
        write_config_ini('mysql_readbook', 'host', 'plus-r.mysql.lrts.me')
        write_config_ini('mysql_readbook', 'port', '3306')
        write_config_ini('mysql_readbook', 'username', 'readbook_r')
        write_config_ini('mysql_readbook', 'password', 'hnzrjgg@#9248zrwliGUnz9024..RIbT')
        # yystory数据库
        write_config_ini('mysql_yystory', 'host', 'plus-r.mysql.lrts.me')
        write_config_ini('mysql_yystory', 'port', '3306')
        write_config_ini('mysql_yystory', 'username', 'yystory_read')
        write_config_ini('mysql_yystory', 'password', 'Ynzrmki#@Cni,.Ro:sribh82478Gbwuj')
    else:
        pass

def change_mysql_connect_info():
    '''修改测试环境数据库连接信息'''
    # audiobook数据库
    write_config_ini('mysql', 'port', '3306')
    write_config_ini('mysql', 'username', 'lazyaudio')
    write_config_ini('mysql', 'password', 'q(nQ5_0xeYNriZaUSBvgP)@E')
    # platform数据库
    write_config_ini('mysql_platform', 'port', '3306')
    write_config_ini('mysql_platform', 'username', 'readonly')
    write_config_ini('mysql_platform', 'password', 'CnRhsirghsorig##!!Ri72174Glw')
    # billing数据库
    write_config_ini('mysql_billing', 'port', '3306')
    write_config_ini('mysql_billing', 'username', 'readonly')
    write_config_ini('mysql_billing', 'password', 'CnRhsirghsorig##!!Ri72174Glw')
    # readbook数据库
    write_config_ini('mysql_readbook', 'port', '3306')
    write_config_ini('mysql_readbook', 'username', 'readonly')
    write_config_ini('mysql_readbook', 'password', 'CnRhsirghsorig##!!Ri72174Glw')
    # yystory数据库
    write_config_ini('mysql_yystory', 'port', '3306')
    write_config_ini('mysql_yystory', 'username', 'readonly')
    write_config_ini('mysql_yystory', 'password', 'CnRhsirghsorig##!!Ri72174Glw')

def get_services_conf(key1, key2):
    """
    读取yaml文件获取配置，二级key
    :param key1:第一层级的key值
    :param key2:第二层级的key值
    :return:
    """
    config_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/config/service_config.yaml'
    f = open(config_path, 'r', encoding='utf-8')
    cfg = f.read()
    data = yaml.load(cfg)
    value = data[key1][key2]
    return value


def login_control():
    """
    获取登录开关配置
    :return:
    """
    return get_services_conf('keys', 'loginKey')
