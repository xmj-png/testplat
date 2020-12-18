import time
from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta

def getCurrentTime():
    '''获取当前的时间的年月日'''
    currentDate_time = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
    currentDate=time.strftime("%Y-%m-%d", time.localtime())
    currentMonth_style1=time.strftime("%Y-%m", time.localtime())
    currentMonth_style2=time.strftime("%Y%m", time.localtime())
    print(currentDate_time)
    return [currentDate,currentMonth_style1,currentMonth_style2,currentDate_time]
def month_days(date1='202006'):
    '''获取当前月份的天数'''
    date1=str(date1)
    years=int(date1[0:4])
    month=date1[4:6]
    if (years % 4 == 0 and years % 100 != 0) or (years % 400 == 0):
        if month in ['01','03','05','07','08','10','12']:
            month_days=31
        elif month in ['04','06','09','11']:
            month_days=30
        else:
            month_days=29
    else:
        if month in ['01','03','05','07','08','10','12']:
            month_days = 31
        elif month in ['04','06','09','11']:
            month_days = 30
        else:
            month_days = 28
    return month_days
def before_today(days=-1):
    '''获取当前时间前N天的日期'''
    before_todays = (date.today() + timedelta(days=days)).strftime("%Y-%m-%d")
    print(before_todays)
    return before_todays
def before_month(month=1):
    '''获取当前月份的前N个月'''
    current_date = str(date.today())
    current_month = current_date[5:7]
    before_days = str(date.today()-relativedelta(months=+month))
    before_months = before_days[5:7]
    before_years = before_days[0:4]
    print(before_years,before_months)
    return [before_years,before_months,current_month]




if __name__=='__main__':
    getCurrentTime()