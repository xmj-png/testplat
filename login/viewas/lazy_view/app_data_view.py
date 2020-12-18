from login.forms_group import app_forms
from login.templates.app.common.Test_Listening_List_Add_Books import test_listeningList_add_books
from login.templates.utils.confutils import login_control, init_configs
from django.shortcuts import redirect, render

def folder_add_books(request):
    '''听单添加书籍'''
    #登录控制
    if request.session.is_empty() and login_control():
        return redirect('/login/')
    #判断请求是否为空
    if request.method:
        # 表单数据获取，返回一个 querydict (该对象包含了所有的HTTP POST参数，通过表单上传的所有字符都会保存在该属性中)
        folder_form = app_forms.Folder_Add_Books_form(request.POST)
        print('folder_form>>>>>>>>>>>>>>>>>>>>>',folder_form)
        #校验表单数据是否合法
        if folder_form.is_valid():
            #获取环境信息并切换环境
            app_env = folder_form.cleaned_data.get('host')
            init_configs(app_env)
            #获取用户名和密码
            username = folder_form.cleaned_data.get('username')
            password = folder_form.cleaned_data.get('password')
            #调用方法往听单里加书
            Folder_Name = test_listeningList_add_books(username,password)
            message = "听单：%s 添加了100本书籍！\n" % (Folder_Name.get('folder_name'))
            return render(request, 'login/app/folder_add_books.html', locals())
        return render(request, 'login/app/folder_add_books.html', locals())










