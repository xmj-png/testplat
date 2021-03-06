import base64
import hashlib
from pyDes import des, PAD_PKCS5, CBC
import binascii

# from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
# from Crypto.PublicKey import RSA
# from login.templates.utils.confutils import get_public_key, get_private_key


def encode_md(encodestr):
    # MD5加密(返回bytes，作为二进制数据字符串值)
    md = hashlib.md5(encodestr.encode("utf-8")).digest()
    return md


def encrypt_md5(s):
    #MD5加密(返回str，作为十六进制数据字符串值)
    new_md5 = hashlib.md5()
    # 这里必须用encode()函数对字符串进行编码，不然会报 TypeError: Unicode-objects must be encoded before hashing
    new_md5.update(s.encode(encoding='utf-8'))
    # 加密
    return new_md5.hexdigest()

def encrypt_des(get_token,pwd='123456'):
    token=get_token.encode('utf-8') #秘钥
    tokens=token[0:8] #取秘钥的前8位
    iv='lrts8621'.encode('utf-8') #偏转向量
    pwds=encrypt_md5(pwd)
    #des加密,其中tokens，iv必须是8位
    des_obj = des(tokens, CBC, IV=iv,padmode=PAD_PKCS5)  # 初始化一个des对象，参数是秘钥，加密方式，偏移，填充方式
    secret_bytes = des_obj.encrypt(pwds,padmode=PAD_PKCS5)  # 用对象的encrypt方法加密
    # 转base64编码返回
    print('加密后的密码:',base64.standard_b64encode(secret_bytes).decode())
    return base64.standard_b64encode(secret_bytes).decode()


def encode_base64(encodestr):
    # base64加密
    return base64.b64encode(encodestr)  # 返回byte类型


def decode_base64(decodestr):
    # base64解密
    return base64.b64decode(decodestr)  # 返回byte类型


def app_account_encode(inputstr):
    """
    账户密码加密
    :param inputstr: 类型为str
    :return:
    """
    return str(encode_base64(encode_md(inputstr)), "utf-8")

#
# def rsa_encrypt(msg):
#     """
#     RSA加密
#     :param pub_key_str:公钥
#     :param msg:待加密信息
#     :return:
#     """
#     msg = msg.encode('utf-8')
#     length = len(msg)
#     default_length = 117
#     # 公钥加密
#     public_keystr = '-----BEGIN RSA PUBLIC KEY-----\n' + get_public_key() + '\n-----END RSA PUBLIC KEY-----'
#     pubobj = Cipher_pkcs1_v1_5.new(RSA.importKey(public_keystr))
#     # 长度不用分段
#     if length < default_length:
#         return base64.b64encode(pubobj.encrypt(msg))
#     # 需要分段
#     offset = 0
#     res = []
#     while length - offset > 0:
#         if length - offset > default_length:
#             res.append(pubobj.encrypt(msg[offset:offset + default_length]))
#         else:
#             res.append(pubobj.encrypt(msg[offset:]))
#         offset += default_length
#     byte_data = b''.join(res)
#     return base64.b64encode(byte_data)
#
#
# def rsa_decrypt(msg):
#     """
#     RSA解密
#     :param msg:待解密信息
#     :return:
#     """
#
#     msg = base64.b64decode(msg)
#     length = len(msg)
#     default_length = 128
#     # 私钥解密
#     private_keystr = '-----BEGIN RSA PRIVATE KEY-----\n' + get_private_key() + '\n-----END RSA PRIVATE KEY-----'
#     priobj = Cipher_pkcs1_v1_5.new(RSA.importKey(private_keystr))
#     # 长度不用分段
#     if length < default_length:
#         return b''.join(priobj.decrypt(msg, b'xyz'))
#     # 需要分段
#     offset = 0
#     res = []
#     while length - offset > 0:
#         if length - offset > default_length:
#             res.append(priobj.decrypt(msg[offset:offset + default_length], b'xyz'))
#         else:
#             res.append(priobj.decrypt(msg[offset:], b'xyz'))
#         offset += default_length
#     return b''.join(res)
if __name__=='__main__':
    encrypt_des('d5f1c4e5')