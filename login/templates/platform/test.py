from login.templates.utils.dbutil import select
from login.templates.utils.getconf import get_conf

# print('11111111111111111111111')
# get_conf('webHD', 'Accept')
# print('2222222222222222222222222')
# cp_record = select("select * from yyting_partdb.c_comic_copyright  order by id desc limit 1;","db_yyting_partdb")

cp_record = select("select * from yyting_partdb.c_comic_copyright  order by id desc limit 1;","db_yyting_partdb")












