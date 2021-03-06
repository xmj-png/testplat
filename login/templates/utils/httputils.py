import requests

from login.templates.utils import getconf
from login.templates.utils.utils import securitycode, geturl, joint_parameters


def post_app(apiname, parameters, headers=getconf.getdict('Headers', 'user-agent')):
    """
    新用例的app端post统一调用这个新的请求方法
    :param headers: 请求头，不传默认取配置；传则取对应值
    :param apiname:取自config_global.imi文件下的apinames
    :param parameters:默认传参imei，q，nwt已加，只需要添加剩下的参数
    :return:
    """
    parameters['imei'] = getconf.get_conf('params', 'imei')
    parameters['q'] = getconf.get_conf('params', 'q')
    parameters['nwt'] = getconf.get_conf('params', 'nwt')
    url = getconf.get_conf('HOST', 'apiDomain')
    if 'Android' in headers.get('user-agent'):
        parameters['sc'] = securitycode(apiname, parameters)
        return requests.post(url + apiname, data=parameters, headers=headers)
    elif 'iOS' in headers.get('user-agent'):
        parameters['sc'] = securitycode(apiname, parameters, 2)
        return requests.post(url + apiname, data=parameters, headers=headers)


def post_reg(apiname, parameters):
    """
    新自动注册专用
    :param apiname:
    :param parameters:
    :return:
    """
    url = getconf.get_conf('HOST', 'apiDomain')
    headers = getconf.getdict('Headers', 'user-agent')
    if 'Android' in headers.get('user-agent'):
        parameters['sc'] = securitycode(apiname, parameters)
        return requests.post(url + apiname, data=parameters, headers=headers)
    elif 'iOS' in headers.get('user-agent'):
        parameters['sc'] = securitycode(apiname, parameters, 2)
        return requests.post(url + apiname, data=parameters, headers=headers)


def get_app(apiname, parameters, headers=getconf.getdict('Headers', 'user-agent')):
    """
    新用例的app端get统一调用这个新的请求方法
    :param headers: 请求头，不传默认取配置；传则取对应值
    :param apiname:取自config_global.imi文件下的apinames
    :param parameters:默认传参imei，q，nwt已加，只需要添加剩下的参数
    :return:
    """
    parameters['imei'] = getconf.get_conf('params', 'imei')
    parameters['q'] = getconf.get_conf('params', 'q')
    parameters['nwt'] = getconf.get_conf('params', 'nwt')
    url = getconf.get_conf('HOST', 'apiDomain')
    if 'Android' in headers.get('user-agent'):
        parameters['sc'] = securitycode(apiname, parameters)
        # return requests.get(url + apiname + '?' + joint_parameters(parameters), headers=headers)
        return requests.get(url + apiname + '?',params=parameters, headers=headers)
    elif 'iOS' in headers.get('user-agent'):
        parameters['sc'] = securitycode(apiname, parameters, 2)
        # return requests.get(url + apiname + '?' + joint_parameters(parameters), headers=headers)
        return requests.get(url + apiname + '?', params=parameters, headers=headers)
def get_app_advert(apiname, parameters, headers=getconf.getdict('Headers', 'user-agent')):
    """
    新用例的app端广告获取统一调用这个新的get请求方法
    :param headers: 请求头，不传默认取配置；传则取对应值
    :param apiname:取自config_global.imi文件下的apinames
    :param parameters:默认传参imei，q，nwt已加，只需要添加剩下的参数
    :return:
    """
    parameters['imei'] = getconf.get_conf('params', 'imei')
    parameters['q'] = getconf.get_conf('params', 'q')
    parameters['nwt'] = getconf.get_conf('params', 'nwt')
    url = getconf.get_conf('HOST', 'apidomain_advert')
    if 'Android' in headers.get('user-agent'):
        parameters['sc'] = securitycode(apiname, parameters)
        return requests.get(url + apiname + '?' + geturl(parameters), headers=headers)
    elif 'iOS' in headers.get('user-agent'):
        parameters['sc'] = securitycode(apiname, parameters, 2)
        return requests.get(url + apiname + '?' + geturl(parameters), headers=headers)

# admin下Post方式提交请求-登录专用
def postadmin_old(url, apiname, parameters, headers):
    return requests.post(url + apiname, data=parameters, headers=headers)

#paltform下post方法提交请求-登录专用
def post_platform(url, apiname, data, headers):
    return requests.post(url + apiname, json=data, headers=headers)


# admin下Post方式提交请求-非登录
def postadmin(apiname, parameters, admintoken, adminapiname):
    """
    :param apiname:取自config_global.imi文件下的adminapis
    :param parameters:入参
    :param admintoken:
    :param adminapiname:
    :return:
    """
    headers = {'User-Agent': getconf.get_conf('webHD', 'user-agent'), 'Accept': getconf.get_conf('webHD', 'accept'),
               'Authorization': 'Bearer {"token":"' + admintoken + '","currentPath":"' + adminapiname + '"}'}
    if 'platformcopyright' in apiname:
        headers['Content-Type'] = 'application/json;charset=UTF-8'
        return requests.post(getconf.get_conf('HOST', 'adminDomain') + apiname, json=parameters, headers=headers)
    elif 'operationRecordAuditEdit' in apiname:
        return requests.post(getconf.get_conf('HOST', 'adminDomain') + apiname, data=parameters, headers=headers,
                             cookies={"psid": admintoken})
    else:
        return requests.post(getconf.get_conf('HOST', 'adminDomain') + apiname, data=parameters, headers=headers)


# admin下get方式提交请求-非登录
def getadmin(apiname, parameters, admintoken, adminapiname):
    """
    :param url:取自config_global.ini文件下的adminapis
    :param apiname:入参
    :param parameters:
    :param headers:
    :return:
    """
    headers = {'User-Agent': getconf.get_conf('webHD', 'User-Agent'), 'Accept': getconf.get_conf('webHD', 'Accept'),
               'Authorization': 'Bearer {"token":"' + admintoken + '","currentPath":"' + adminapiname + '"}'}
    return requests.get(getconf.get_conf('HOST', 'adminDomain') + apiname + '?' + joint_parameters(parameters),
                        headers=headers)
# paltform下get方式提交请求-非登录
def get_platforms(apiname, parameters,platform_token):
    """
    非登录
    :param url:取自config_global.ini文件下的adminapis
    :param apiname:入参
    :param parameters:
    :param headers:
    :return:
    """
    headers = {'User-Agent': getconf.get_conf('webHD', 'User-Agent'), 'Accept': getconf.get_conf('webHD', 'Accept'),
               'Content-Type': getconf.get_conf('webHD', 'content-type-json'),'cookie':'sid'+'='+platform_token}
    return requests.get(getconf.get_conf('HOST', 'platform_domain') + apiname + '?' + joint_parameters(parameters),
                        headers=headers)

#调用platform下getLoginToken接口时用
def get_paltforms_login(apiname, parameters):
    """
    登录专用
    :param url:取自config_global.ini文件下的adminapis
    :param apiname:入参
    :param parameters:
    :param headers:
    :return:
    """
    headers = {'User-Agent': getconf.get_conf('webHD', 'user-agent'), 'Accept': getconf.get_conf('webHD', 'Accept'),
               'Content-Type': getconf.get_conf('webHD', 'content-type-json')}
    return requests.get(getconf.get_conf('HOST', 'platform_domain') + apiname + '?' + joint_parameters(parameters),
                        headers=headers)
