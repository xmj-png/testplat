from django import forms

class Folder_Add_Books_form(forms.Form):
    '''听单新增书籍'''
    host_name = (
        ('moon', '月亮'),
        ('mars', '火星'),
        ('earth', '地球'),
    )
    host = forms.ChoiceField(label="测试环境", choices=host_name)
    username = forms.CharField(label='用户名', max_length=64,
                                      widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "输入用户名"}))
    password = forms.CharField(label='密码', max_length=64,
                                        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "输入密码"}))
class Unbundle_phone_form(forms.Form):
    '''听单新增书籍'''
    host_name = (
        ('moon', '月亮'),
        ('mars', '火星'),
        ('earth', '地球'),
        ('build', '预发布'),
    )
    host = forms.ChoiceField(label="测试环境", choices=host_name)
    user_id = forms.CharField(label='用户id', max_length=64,
                                      widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "输入用户id"}))
    phone_num = forms.CharField(label='手机号', max_length=64,
                              widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "输入手机号"}))