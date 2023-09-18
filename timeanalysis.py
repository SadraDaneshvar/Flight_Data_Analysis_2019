import timecalc as z

#تعداد خرید بلیت بر حسب روز میلادی
def DAYOFWEEKbyusercount(data):
    data=z.dayofweek(data)
    G1 = data.groupby(['day_of_the_week']).count().sort_values(['id'],ascending=False)['id']
    return G1

#تعداد خرید بلیت بر حسب روز شمسی
def DAYOFWEEKpersianbyusercount(data):
    data=z.rooz(data)
    G1 = data.groupby(['rooz']).count().sort_values(['id'],ascending=False)['id']
    return G1

#تعداد خرید بلیت بر حسب ماه میلادی
def MONTHbyusercount(data):
    data=z.month(data)
    G1 = data.groupby(['month']).count().sort_values(['id'],ascending=False)['id']
    return G1

#تعداد خرید بلیت بر حسب ماه شمسی
def MONTHpersianbyusercount(data):
    data=z.mah(data)
    G1 = data.groupby(['mah']).count().sort_values(['id'],ascending=False)['id']
    return G1

#تعداد خرید بلیت بر حسب ساعت خرید
def TIMEbyusercount(data):
    data=z.time(data)
    G1 = data.groupby(['time_intervals']).count().sort_values(['id'],ascending=False)['id']
    return G1

#میانگین قیمت خرید بلیت بر حسب روز میلادی
def DAYOFWEEKbypriceaverage(data):
    data=z.dayofweek(data)
    G1 = data.groupby(['day_of_the_week']).mean().sort_values(['price'],ascending=False)['price']
    return G1

#میانگین قیمت خرید بلیت بر حسب روز شمسی
def DAYOFWEEKpersianbypriceaverage(data):
    data=z.rooz(data)
    G1 = data.groupby(['rooz']).mean().sort_values(['price'],ascending=False)['price']
    return G1

#مجموع قیمت خرید بلیت بر حسب روز شمسی
def DAYOFWEEKpersianbypricesum(data):
    data=z.rooz(data)
    G1 = data.groupby(['rooz']).sum().sort_values(['price'],ascending=False)['price']
    return G1

#میانگین قیمت خرید بلیت بر حسب ماه میلادی
def MONTHbypriceaverage(data):
    data=z.month(data)
    G1 = data.groupby(['month']).mean().sort_values(['price'],ascending=False)['price']
    return G1

#میانگین قیمت خرید بلیت بر حسب ماه شمسی
def MONTHpersianbypriceaverage(data):
    data=z.mah(data)
    G1 = data.groupby(['mah']).mean().sort_values(['price'],ascending=False)['price']
    return G1

#مجموع قیمت خرید بلیت بر حسب ماه شمسی
def MONTHpersianbypricesum(data):
    data=z.mah(data)
    G1 = data.groupby(['mah']).sum().sort_values(['price'],ascending=False)['price']
    return G1

#میانگین قیمت خرید بلیت بر حسب ساعت خرید
def TIMEbypriceaverage(data):
    data=z.time(data)
    G1 = data.groupby(['time_intervals']).mean().sort_values(['price'],ascending=False)['price']
    return G1

#مجموع قیمت خرید بلیت بر حسب ساعت خرید
def TIMEbypricesum(data):
    data=z.time(data)
    G1 = data.groupby(['time_intervals']).sum().sort_values(['price'],ascending=False)['price']
    return G1

#فاصله زمان خرید بلیت و زمان پرواز در ماه های میلادی
def timedeltawithmonth(data):
    data=z.timedelta(data)
    data=z.month(data)
    f = data.isnull().groupby(data['month']).sum()
    f1=list(f['timedelta'])
    f2=list(data.groupby(['month']).count()['timedelta'])
    f3=list(data.groupby(['month']).sum()['timedelta'])
    length = [i - j for i, j in zip(f2, f1)] 
    mean = [i / j for i, j in zip(f3, length)]
    f['mean'] = mean
    g = f.sort_values(['mean'],ascending=False)['mean']
    return g

#فاصله زمان خرید بلیت و زمان پرواز در ماه های شمسی
def timedeltawithmonthpersian(data):
    data=z.timedelta(data)
    data=z.mah(data)
    f = data.isnull().groupby(data['mah']).sum()
    f1=list(f['timedelta'])
    f2=list(data.groupby(['mah']).count()['timedelta'])
    f3=list(data.groupby(['mah']).sum()['timedelta'])
    length = [i - j for i, j in zip(f2, f1)] 
    mean = [i / j for i, j in zip(f3, length)]
    f['mean'] = mean
    g = f.sort_values(['mean'],ascending=False)['mean']
    return g




    











 