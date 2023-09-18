#موارد مربوط به خواسته 6


#خواندن کتابخانه
import pandas as pd
import matplotlib.pyplot as plt
import timecalc
import commute
#خواندن داده ها
d = pd.read_excel(r'C:\Users\Mahan\Desktop\New folder\FlightSales.xlsx')
#اضافه کردن ستون های مربوط به امور زمانی
timecalc.sharghigharbi(d)
d=timecalc.rooz(d)
d=timecalc.mah(d)
d=timecalc.year(d)
d=timecalc.dayofweek(d)
d=timecalc.month(d)
d=timecalc.year(d)
d=timecalc.time(d)


#نمودار ستونی فروش و تعداد مسافر شرکتهای مختلف
#بدست آوردن مجموع فروش شرکتها
import companies
a= companies.Richestcompanybyprice(d).reset_index()
b=sorted(list(a['company']))
b=list(map(str,b))
price = []
#v=sum(price)/len(price)
for i in b:
    for j in range(len(a['company'])):
        
        if a['company'][j] == int(i):
            price.append(a['price'][j]/1000000)            
#بدست آوردن تعداد مسافر شرکتها
a = companies.mostPopularcompanybyusercount(d).reset_index()
b=sorted(list(a['company']))
b=list(map(str,b))
count = []
for i in b:
    for j in range(len(a['company'])):        
        if a['company'][j] == int(i):
            count.append(a['user_id'][j]/1000)

#به دست آوردن شرکتهای برتر از نظر فروش و تعداد مسافر

averagep=int(round(sum(price)/len(price)))
averagec=int(round(sum(count)/len(count)))
topcomp=[]
for i in range(len(b)):
    if (price[i]>averagep) and (count[i]>averagec):
        topcomp.append(b[i])
#کشیدن نمودار
import numpy as np
ind = np.arange(len(b))
width=0.44
fig, ax=plt.subplots()
rect1=ax.bar(ind+width/2,price,width=width,color='xkcd:sky blue')
rect2=ax.bar(ind-width/2,count,width=width,color='xkcd:jade green')
plt.xticks(ind,b)
plt.xlabel('Company Code')
plt.text(-2.22,90,'Bilion Toman',color='xkcd:sky blue')
plt.text(-3.05 , 84.5 , 'Thousand Passengers',color='xkcd:jade green')
plt.hlines(averagep,-0.6,len(b),linestyles='--',colors='xkcd:ocher',label='Average')
plt.text(11.5,averagep,'Average Sale='+str(int(averagep)) ,color='xkcd:ocher')
plt.hlines(averagec,-0.6,len(b),linestyles='--',colors='xkcd:milk chocolate',label='Average')
plt.text(5.5,averagec,'Average Passengers='+str(int(averagec)) ,color='xkcd:milk chocolate')
plt.title('Companies Sale & Popularity')
#ذخیره نمودار 
plt.savefig('savepath/Companies Sale & Popularity' , dpi = 2000 , bbox_inches='tight',quality=95) 
plt.show()

#نمودار میزان فروش شرکتهای مختلف در ماه های مختلف
q = d.groupby(['company','mah']).sum()['price'].reset_index()
q = pd.DataFrame(q)
q = q[q['company'].isin(topcomp)].reset_index()
m = q.groupby('company')
C=[]
for company , company_df in m:
    C.append(company)
maah = ['Farvardin','Ordibehesht','Khordad','Tir','Mordad','Shahrivar','Mehr','Aban','Azar','Dey','Bahman','Esfand']
for p in C:
    m=[]
    c=[]
    a = q.loc[q['company'] == p].reset_index()
    for i in maah:
        for j in range(len(a['mah'])):
            if a['mah'][j] == i:
                c.append(a['price'][j]/1000000)
                m.append(i)
    plt.plot(m,c,label=str(p))
plt.title('Three Richest Companies Sale Distribution')
plt.xlabel('Month')
plt.xticks(rotation=45)
plt.ylabel('Total sale (Billion Toman)')
plt.legend()    
plt.savefig('savepath/Three Richest Companies Sale Distribution' , dpi = 2000 , bbox_inches='tight',quality=95) 
plt.show()


#بدست آوردن مقصد های پرطرفدار
a=commute.popularDestination(d).reset_index()
x=(list(a['destination']))
x=list(map(str,x))
y=list(a['id'])
v=sum(y)/len(y)
topdest=[]
for i in range(len(x)):
    if y[i]>v:
        topdest.append(x[i])


#بدست آوردن مبدا های پرطرفدار
a=commute.popularSource(d).reset_index()
x=(list(a['source']))
x=list(map(str,x))
y=list(a['id'])
v=sum(y)/len(y)
topsource=[]
for i in range(len(x)):
    if y[i]>v:
        topsource.append(x[i])





#نمودار توزیع مقصدهای مختلف در پرواز های شرکتهای با فروش و مسافر بیشتر
a=d[d['company'].isin(topcomp)]
a=a[a['destination'].isin(topdest)]
a=a.groupby(['company','destination']).count().reset_index()[['company','destination','id']]
dest=list(a['destination'].unique())
comp=list(a['company'].unique())
s=[]
for i in range(len(dest)):
    ss=[]    
    for j in comp:
        t=0
        for k in list(a[a['company']==j]['id']):
            if list(a[(a['company']==j) & (a['id']==k)]['destination'])==dest[i]:
                ss.append(k)
                t=1
        if t==0:
            ss.append(0)                                  
        
    s.append(ss)
s=s[-len(dest):]
ind=np.arange(len(comp))
summ=np.array(s[0])
plt.bar(ind,s[0],width=0.35,label=topdest[0])
for i in range(1,len(dest)):
    plt.bar(ind,s[i],width=0.35,bottom=summ,label=topdest[i])
    summ=summ+np.array(s[i])
plt.xticks(ind,topcomp)
plt.legend(title='Destination Code')
plt.xlabel('Company Code')
plt.ylabel('Passengers Count')
plt.title('Destination Distribution for Top Companies')
plt.savefig('savepath/Destination Distribution for Top Companies' , dpi = 2000 , bbox_inches='tight',quality=95) 




#نمودار توزیع مبدا مختلف در پرواز های شرکتهای با فروش و مسافر بیشتر
a=d[d['company'].isin(topcomp)]
a=a[a['source'].isin(topdest)]
a=a.groupby(['company','source']).count().reset_index()[['company','source','id']]
dest=list(a['source'].unique())
comp=list(a['company'].unique())
s=[]
for i in range(len(dest)):
    ss=[]    
    for j in comp:
        t=0
        for k in list(a[a['company']==j]['id']):
            if list(a[(a['company']==j) & (a['id']==k)]['source'])==dest[i]:
                ss.append(k)
                t=1
        if t==0:
            ss.append(0)                                  
        
    s.append(ss)
s=s[-len(dest):]
import numpy as np
ind=np.arange(len(comp))
summ=np.array(s[0])
plt.bar(ind,s[0],width=0.35,label=topdest[0])
for i in range(1,len(dest)):
    plt.bar(ind,s[i],width=0.35,bottom=summ,label=topdest[i])
    summ=summ+np.array(s[i])
plt.xticks(ind,topcomp)
plt.legend(title='source Code')
plt.xlabel('Company Code')
plt.ylabel('Passengers Count')
plt.title('source Distribution for Top Companies')
plt.savefig('source Distribution for Top Companies.png' , dpi = 2000 , bbox_inches='tight',quality=95) 







