# coding=gbk
from login.templates.platform.common.operate_mysql import select_platform, select_platform


def announcerName():
    '''���ɲ�������'''
    cp_record = select_platform("select * from platform.t_copyright_announcer order by id desc limit 1;")
    cp_id = cp_record[0]['id']
    cp_id = str(cp_id)
    cp_id_lenth = len(cp_id)
    if cp_id_lenth < 4:
        AnnouncerName_Number = str(int(cp_id) + 1).zfill(4)
    elif cp_id_lenth == 4 and cp_id != '9999':
        AnnouncerName_Number = str(int(cp_id) + 1)
    elif cp_id_lenth > 4 and cp_id[-4:] != '9999':
        AnnouncerName_Number = str(int(cp_id[-4:]) + 1).zfill(4)
    else:
        AnnouncerName_Number = '0001'
    AnnouncerName = '����' + AnnouncerName_Number
    print('����������Ϊ��'+AnnouncerName)
    return AnnouncerName

if __name__=='__main__':
    announcerName()
