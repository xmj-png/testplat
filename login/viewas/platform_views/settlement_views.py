from django.views.decorators.csrf import csrf_exempt

from login import models
from login.forms_group import platform_forms
from login.templates.platform.settlement.Settlement import Settlement
from login.templates.utils.confutils import login_control, init_configs
from django.shortcuts import redirect, render

from login.templates.utils.utils import get_local_time_second


def settlement_not_vip(request):
    """
    结算非VIP业务
    :param request:
    :return:
    """
    if request.session.is_empty() and login_control():
        return redirect('/login/')
    # print('request信息',request.method,request.session.is_empty())
    print('request.method++++++++++++++>',request.method)
    if request.method: #获取请求的方法，如get,post ...
        settlement_form = platform_forms.settlement_not_vip_form(request.POST) #表单数据获取，返回一个 querydict ，该对象包含了所有的HTTP POST参数，通过表单上传的所有 字符 都会保存在该属性中
        print('**************',settlement_form)
        if settlement_form.is_valid(): #校验表单有没错误
            # 切换环境
            Settlement_env = settlement_form.cleaned_data.get('host')
            init_configs(Settlement_env)
            #获取结算数据
            Settlement_Date = settlement_form.cleaned_data.get('settlement_date') #根据键获取值同 cleaned_data['settlement_date']，其中cleaned_data就是读取表单返回的值
            Settlement_Res_ID = settlement_form.cleaned_data.get('settlement_res_id')
            PlatformType = int(settlement_form.cleaned_data.get('platformType'))
            Settlement_Partner_ID = settlement_form.cleaned_data.get('settlement_partner_id')
            Settlement_Cooperation_Business = settlement_form.cleaned_data.get('settlement_cooperation_business')
            print('数据类型',type(Settlement_Date))
            if PlatformType==1:
                settlement_record = Settlement(Settlement_Date, Settlement_Res_ID, Settlement_Partner_ID,int(Settlement_Cooperation_Business)).settlement_lr_yaya(1)
            else:
                settlement_record = Settlement(Settlement_Date, Settlement_Res_ID, Settlement_Partner_ID,int(Settlement_Cooperation_Business)).settlement_lr_yaya(2)
            print('数据值：',settlement_record)
            print('数据类型：',type(settlement_record))
            #存表
            results = models.settlement_not_vip_models()
            results.settlement_month=settlement_record.get('settlement_month')
            results.partner_id=settlement_record.get('partner_id')
            results.entity_id=settlement_record.get('entity_id')
            results.business=settlement_record.get('business')
            results.sum_cash_flow = settlement_record.get('lr_sum_cash_flow')
            results.sum_cash_flow_billing=settlement_record.get('lr_sum_cash_flow_billing')
            results.channel_partner_amount=settlement_record.get('lr_channel_partner_amount')
            results.sum_commission_in=settlement_record.get('lr_sum_commission_in')
            results.base_billing_amount=settlement_record.get('lr_base_billing_amount')
            results.partner_amount=settlement_record.get('lr_partner_amount')
            results.tech_amount=settlement_record.get('lr_tech_amount')
            results.baseBillingAounmt_subtract_techAmount=settlement_record.get('baseBillingAounmt_subtract_techAmount')
            results.create_time=get_local_time_second()
            results.update_time=get_local_time_second()
            results.save() #存表操作
            message = "本月实际流水：%s \n" % (settlement_record.get('lr_sum_cash_flow')) +\
                      "本月可分成流水：%s \n" % str(settlement_record.get('lr_sum_cash_flow_billing'))+ \
                      "渠道分成金额：%s \n" % str(settlement_record.get('lr_channel_partner_amount')) + \
                      "支付手续费：%s \n" % str(settlement_record.get('lr_sum_commission_in')) + \
                      "分成基数：%s \n" % str(settlement_record.get('lr_base_billing_amount')) + \
                      "当月税前：%s \n" % str(settlement_record.get('lr_partner_amount')) + \
                      "懒人技术服务费：%s \n" % str(settlement_record.get('lr_tech_amount')) + \
                      "分成基数 - 懒人技术服务费：%s \n" % str(settlement_record.get('baseBillingAounmt_subtract_techAmount'))
            return render(request, 'login/platform/settlement_not_vip.html', locals())
    return render(request, 'login/platform/settlement_not_vip.html', locals())

def settlement_not_vip_result(request):
    '''
    结算结果展示
    :param request:
    :return:
    '''
    settlement_data = models.settlement_not_vip_models.objects.filter().order_by('-create_time').values()[0:10]
    print('结算结果：', settlement_data)
    return render(request, 'login/platform/settlement_not_vip_result.html', {'settlement_data': settlement_data})