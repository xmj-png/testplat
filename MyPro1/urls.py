"""MyPro1 URL Configuration

The `urlpatterns` list routes URLs to viewas. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function viewas
    1. Add an import:  from my_app import viewas
    2. Add a URL to urlpatterns:  path('', viewas.home, name='home')
Class-based viewas
    1. Add an import:  from other_app.viewas import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import TemplateView
from django.views.static import serve
from login.views import echarts_data, change_hosts, data_ajax, test_data, pass_rate_stats
from login import views, static
from login.viewas.lazy_view import activitys_view, app_data_view
from login.viewas.lazy_view import user_view
from login.viewas.test_view import autotest_view
from login.viewas.test_view import cases_views
from django.urls import include
from django.conf.urls import url
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('platform/', include('login.urls')),
    # path('app/', include('login.urls')),
    path('app/folder_add_books',app_data_view.folder_add_books),
    path('app/unbundle_phone_num',user_view.unbundle_phone_view),
    path('', views.index),
    path('pages/', views.pages),
    path('pages/', views.error),
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', views.logout),
    path('add_cases/', cases_views.add_cases),
    path('cases_detail/', cases_views.cases_detail, name="cases_detail"),
    path('search_case/', cases_views.search_case),
    path('delete_case/', cases_views.delete_case),
    path('upload_cases/', cases_views.upload_cases),
    path('cases_pages/<pindex>', cases_views.cases_pages, name="cases_pages"),
    path('case_edit/', cases_views.case_edit),
    path('api_test/', autotest_view.api_test),
    path('run_test/', autotest_view.run_test),
    path('test_report/<report_name>', autotest_view.test_report),
    path('test_report_single/', autotest_view.test_report_single),
    path('test_report_list10/', autotest_view.test_report_list10),
    path('send_email/', autotest_view.send_email),
    path('mail_config_manual/', autotest_view.mail_config_manual),
    path('run_case/', autotest_view.run_case),
    path('send_vip/', user_view.send_vip),
    path('vip_expire/', user_view.vip_expire),
    path('send_code/', user_view.send_code),
    path('charge_account/', user_view.charge_account),
    path('add_buy_share/', activitys_view.add_buy_share),
    path('add_ShareListen_free/', activitys_view.add_ShareListen_free),
    path('add_Subtracts_activity/', activitys_view.add_Subtracts_activity),
    path('items_list/<x_type>', activitys_view.items_list),
    path('app/lazy_reg', views.lazy_reg),
    path('get_config/', views.get_config),
    # path('crypt_utils/',viewas.crypt_utils),
    path('error/', views.error),
    path('get_ips/', views.get_ips),
    path('echarts/', TemplateView.as_view(template_name='login/echarts.html'), name='echarts-url'),
    path('api/echarts/', echarts_data, name='api-echarts'),
    path('api/pass_stats/', pass_rate_stats, name='api-passStats'),
    path('api/modify_config/', change_hosts, name='modify_config'),
    path('api/test_ajax/', data_ajax, name='test_ajax'),
    path('test_data/', test_data),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}, name='static'),
    url(r'^favicon\.ico$', RedirectView.as_view(url=r'static/favicon.ico')),
    # path('test001/',views.test001),
    path('app/test002',views.test002)
]
