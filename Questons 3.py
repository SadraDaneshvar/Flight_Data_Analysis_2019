#موارد مربوط به خواسته 3


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


#نمودار تعداد بلیت خریداری شده و مجموع میزان فروش در هرماه
a = timeanalysis.MONTHpersianbypricesum(d).reset_index()
maah = ['Farvardin','Ordibehesht','Khordad','Tir','Mordad','Shahrivar','Mehr','Aban','Azar','Dey','Bahman','Esfand']
#بدست اوردن مجموع فروس بر حسب ماه
price = []
for i in maah:
    for j in range(len(a['mah'])):
        
        if a['mah'][j] == i.lower():
            price.append(a['price'][j]/1000000)
#بدست آوردن تعداد بلیت در هر ماه
a=timeanalysis.MONTTHpersianbyusercount(d).reset_index()
count = []
for i in maah:
    for j in range(len(a['mah'])):
        
        if a['mah'][j] == i.lower():
            count.append(a['id'][j])
#کشیدن نمودار
maah = ['Farvardin','Ordibehesht','Khordad','Tir','Mordad','Shahrivar','Mehr','Aban','Azar','Dey','Bahman','Esfand']
fig, ax1=plt.subplots()
color='tab:red'
plt.title('Total Sale & Total Tickets Count by month')
ax1.set_xlabel('Persian Month')
ax1.set_ylabel('Total Sale (Bilion Toman)',color=color,size=12)
ax1.plot(maah,price,color=color,marker='.')
plt.xticks(maah, rotation = 45 , size=10)
ax1.tick_params(axis='y',labelcolor=color)
ax2=ax1.twinx()
color='tab:blue'
ax2.set_ylabel('Total Count', color=color, size=12) 
ax2.plot(maah, count, color=color,marker='.')
plt.xticks(maah, rotation = 45 , size=10)
ax2.tick_params(axis='y', labelcolor=color)
fig.tight_layout() 
#ذخیره و نمایش نمودار 
plt.savefig('Total Sale & Total Tickets Count by month.png', dpi = 2000 , bbox_inches='tight',quality=95) 
plt.show()


#نمودار تعداد بلیت خریداری شده و میانگین میزان فروش در هرماه
a=timeanalysis.MONTHpersianbypriceaverage(d).reset_index()
#بدست اوردن میانگین فروس بر حسب ماه

maah = ['Farvardin','Ordibehesht','Khordad','Tir','Mordad','Shahrivar','Mehr','Aban','Azar','Dey','Bahman','Esfand']
price = []
for i in maah:
    for j in range(len(a['mah'])):
        
        if a['mah'][j] == i.lower():
            price.append(a['price'][j])
#بدست آوردن تعداد بلیت در هر ماه
#بدست اوردن مجموع فروس بر حسب ماه
a=timeanalysis.MONTHpersianbyusercount(d).reset_index()
count = []
for i in maah:
    for j in range(len(a['mah'])):
        
        if a['mah'][j] == i.lower():
            count.append(a['id'][j])
maah = ['Farvardin','Ordibehesht','Khordad','Tir','Mordad','Shahrivar','Mehr','Aban','Azar','Dey','Bahman','Esfand']
#کشیدن نمودار
fig, ax1=plt.subplots()
color='tab:red'
plt.title('Average Sale & Total Tickets Count by month')
ax1.set_xlabel('Persian Month')
ax1.set_ylabel('Average Sale (Thousand Toman)',color=color,size=12)
ax1.plot(maah,price,color=color,marker='.')
plt.xticks(maah, rotation = 45 , size=10)
ax1.tick_params(axis='y',labelcolor=color)
ax2=ax1.twinx()
color='tab:blue'
ax2.set_ylabel('Total Count', color=color, size=12) 
ax2.plot(maah, count, color=color,marker='.')
plt.xticks(maah, rotation = 45 , size=10)
ax2.tick_params(axis='y', labelcolor=color)
fig.tight_layout() 
#ذخیره نمودار 
plt.savefig('savepath' , dpi = 2000 , bbox_inches='tight',quality=95) 
plt.show()


#نمودار تعداد بلیت خریداری شده و مجموع میزان فروش در روزهای هفته

#بدست اوردن مجموع فروس بر حسب روز هفته
a=timeanalysis.DAYOFWEEKpersianbypricesum(d).reset_index()
rooz = ['shanbe','1shanbe','2shanbe','3shanbe','4shanbe','5shanbe','jomE']
price = []
for i in rooz:
    for j in range(len(a['rooz'])):
        
        if a['rooz'][j] == i:
            price.append(a['price'][j]/1000000)
#بدست آوردن تعداد بلیت در هر روز هفته
a=timeanalysis.DAYOFWEEKpersianbyusercount(d).reset_index()

rooz = ['shanbe','1shanbe','2shanbe','3shanbe','4shanbe','5shanbe','jomE']
count = []
for i in rooz:
    for j in range(len(a['rooz'])):
        
        if a['rooz'][j] == i:
            count.append(a['id'][j])
#کشیدن نمودار
fig, ax1=plt.subplots()
color='tab:red'
plt.title('Total Sale & Total Tickets Count by Day of Week ')
ax1.set_xlabel('Day of Week')
ax1.set_ylabel('Total Sale (Bilion Toman)',color=color,size=12)
ax1.plot(rooz,price,color=color,marker='.')
plt.xticks(rooz, rotation = 45 , size=10)
ax1.tick_params(axis='y',labelcolor=color)
ax2=ax1.twinx()
color='tab:blue'
ax2.set_ylabel('Total Count', color=color, size=12) 
ax2.plot(rooz, count, color=color,marker='.')
plt.xticks(rooz, rotation = 45 , size=10)
ax2.tick_params(axis='y', labelcolor=color)
fig.tight_layout() 
#ذخیره و نمایش نمودار 
plt.savefig('Total Sale & Total Tickets Count by Day of Week .png' , dpi = 2000 , bbox_inches='tight',quality=95) 
plt.show()  

#نمودار تعداد بلیت خریداری شده و میانگین میزان فروش در روزهای هفته

#بدست اوردن میانگین فروس بر حسب روز هفته
a=timeanalysis.DAYOFWEEKpersianbypriceaverage(d).reset_index()
rooz = ['shanbe','1shanbe','2shanbe','3shanbe','4shanbe','5shanbe','jomE']
price = []
for i in rooz:
    for j in range(len(a['rooz'])):
        
        if a['rooz'][j] == i:
            price.append(a['price'][j])
#بدست آوردن تعداد بلیت در هر روز هفته
a=timeanalysis.DAYOFWEEKpersianbyusercount(d).reset_index()

rooz = ['shanbe','1shanbe','2shanbe','3shanbe','4shanbe','5shanbe','jomE']
count = []
for i in rooz:
    for j in range(len(a['rooz'])):
        
        if a['rooz'][j] == i:
            count.append(a['id'][j])
#کشیدن نمودار

fig, ax1=plt.subplots()
color='tab:red'
plt.title('Average Sale & Total Tickets Count by Day of Week ')
ax1.set_xlabel('Day of Week')
ax1.set_ylabel('Average Sale (Thousand Toman)',color=color,size=12)
ax1.plot(rooz,price,color=color,marker='.')
plt.xticks(rooz, rotation = 45 , size=10)
ax1.tick_params(axis='y',labelcolor=color)
ax2=ax1.twinx()
color='tab:blue'
ax2.set_ylabel('Total Count', color=color, size=12) 
ax2.plot(rooz, count, color=color,marker='.')
plt.xticks(rooz, rotation = 45 , size=10)
ax2.tick_params(axis='y', labelcolor=color)
fig.tight_layout()  
#ذخیره و نمایش نمودار 
plt.savefig('savepath/Average Sale & Total Tickets Count by Day of Week' , dpi = 2000 , bbox_inches='tight',quality=95) 
plt.show()


#نمودار تعداد بلیت خریداری شده و میانگین میزان فروش در روزهای هفته
#بدست اوردن مجموع فروس بر حسب ساعت
a=timeanalysis.TIMEbypricesum(d).reset_index()
saat = list(range(1,25))
price = []
for i in saat:
    for j in range(len(a['time_intervals'])):
        
        if a['time_intervals'][j] == i:
            price.append(a['price'][j]/1000000)
        
#بدست آوردن تعداد بلیت در هر ساعت
a=timeanalysis.TIMEbyusercount(d).reset_index()

saat = list(range(1,25))
count = []
for i in saat:
    for j in range(len(a['time_intervals'])):
        
        if a['time_intervals'][j] == i:
            count.append(a['id'][j])
#کشیدن نمودار
fig, ax1=plt.subplots()
color='tab:red'
plt.title('Total Sale & Total Tickets Count by Time')
ax1.set_xlabel('Time')
ax1.set_ylabel('Total Sale (Bilion Toman)',color=color,size=12)
ax1.plot(saat,price,color=color,marker='.')
plt.xticks(saat, rotation = 45 , size=10)
ax1.tick_params(axis='y',labelcolor=color)
ax2=ax1.twinx()
color='tab:blue'
ax2.set_ylabel('Total Count', color=color, size=12) 
ax2.plot(saat, count, color=color,marker='.')
plt.xticks(saat, rotation = 45 , size=10)
ax2.tick_params(axis='y', labelcolor=color)
fig.tight_layout()  
#ذخیره نمودار
plt.savefig('savepath/Total Sale & Total Tickets Count by Time' , dpi = 2000 , bbox_inches='tight',quality=95) 
plt.show()   
#نمودار تعداد بلیت خریداری شده و میانگین میزان فروش درساعتها
#بدست اوردن میانگین فروس بر حسب ساعت
a=timeanalysis.TIMEbypriceaverage(d).reset_index()

saat = list(range(1,25))
price = []
for i in saat:
    for j in range(len(a['time_intervals'])):
        
        if a['time_intervals'][j] == i:
            price.append(a['price'][j])
        
#بدست آوردن تعداد بلیت در هر ساعت
a=timeanalysis.TIMEbyusercount(d).reset_index()

saat = list(range(1,25))
count = []
for i in saat:
    for j in range(len(a['time_intervals'])):
        
        if a['time_intervals'][j] == i:
            count.append(a['id'][j])

fig, ax1=plt.subplots()
color='tab:red'
plt.title('Average Sale & Total Tickets Count by Time')
ax1.set_xlabel('Time')
ax1.set_ylabel('Average Sale (Thousand Toman)',color=color,size=12)
ax1.plot(saat,price,color=color,marker='.')
plt.xticks(saat, rotation = 45 , size=10)
ax1.tick_params(axis='y',labelcolor=color)
ax2=ax1.twinx()
color='tab:blue'
ax2.set_ylabel('Total Count', color=color, size=12) 
ax2.plot(saat, count, color=color,marker='.')
plt.xticks(saat, rotation = 45 , size=10)
ax2.tick_params(axis='y', labelcolor=color)
fig.tight_layout()  
#ذخیره نمودار
plt.savefig('savepath/Average Sale & Total Tickets Count by Time' , dpi = 2000 , bbox_inches='tight',quality=95) 
plt.show()   














