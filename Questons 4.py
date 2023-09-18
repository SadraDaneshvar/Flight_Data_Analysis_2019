#موارد مربوط به خواسته 4


#خواندن کتابخانه
import pandas as pd
import matplotlib.pyplot as plt
import timecalc
import timeanalysis 
#خواندن داده ها
d = pd.read_excel(r'path.xlsx')
#اضافه کردن ستون های مربوط به امور زمانی
timecalc.sharghigharbi(d)
d=timecalc.rooz(d)
d=timecalc.mah(d)
d=timecalc.year(d)
d=timecalc.dayofweek(d)
d=timecalc.month(d)
d=timecalc.year(d)
d=timecalc.time(d)

#نمودار بررسی وابستگی اختلاف زمان خرید بلیت و زمان پرواز
a = timeanalysis.timedeltawithmonthpersian(d).reset_index()

maah = ['farvardin','ordibehesht','khordad','tir','mordad','shahrivar','mehr','aban','azar','dey','bahman','esfand']
mean = []
for i in maah:
    for j in range(len(a['mah'])):
        
        if a['mah'][j] == i:
            mean.append(a['mean'][j])
            
plt.plot(maah,mean,marker='.') 
plt.xticks(maah , rotation = 'vertical')
plt.xlabel('Month')
plt.ylabel('TimeDelta Average')
plt.title('Departure time and Request time Difference')
plt.savefig('C:/Users/SMT/Desktop/Project/Modujles/timedeltawithmonthpersian.png' , dpi = 1200 , bbox_inches='tight')
plt.close()

#نمودار ستونی میانگین اختلاف زمان خرید بلیط و زمان پرواز برای شرکتهای مختلف
a = d.groupby(['company']).mean()['timedelta'].reset_index()
company = list(a['company'])
timedelta = list(a['timedelta'])
plt.bar(company , timedelta)
plt.xticks(company)
plt.xlabel('Company')
plt.ylabel('Departure and Request time differencial')
plt.title('Departure and Request time differencial per Company')
plt.savefig('C:/Users/SMT/Desktop/Project/Modujles/Departure and Request time differencial per Company.png',dpi=1200)
plt.close()
       





