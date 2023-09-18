#موارد مربوط به خواسته 3


#خواندن کتابخانه
import pandas as pd
import matplotlib.pyplot as plt
import timecalc
import commute

#خواندن داده ها
d = pd.read_excel('path.xlsx')
#اضافه کردن ستون های مربوط به امور زمانی
timecalc.sharghigharbi(d)
d=timecalc.rooz(d)
d=timecalc.mah(d)
d=timecalc.year(d)
d=timecalc.dayofweek(d)
d=timecalc.month(d)
d=timecalc.year(d)
d=timecalc.time(d)



#نمودار ستونی تعداد مسافر ها برای مقصدهای مختلف
a=commute.popularDestination(d).reset_index()
x=(list(a['destination']))
x=list(map(str,x))
y=list(a['id'])
v=sum(y)/len(y)
plt.bar(x,y,align='center')
plt.xticks(x,rotation='vertical')
plt.hlines(v,-0.6,len(x),linestyles='--',colors='y',label='Average')
plt.text(len(x)/2,v,'Average Count='+str(int(v)) ,color='g')
plt.xlim(-0.6,len(x))
plt.title('Destinations Popularity bar')
plt.xlabel('Destination Code')
plt.ylabel('Count of Passengers')
plt.savefig('savepath/Destinations Popularity bar' , dpi = 2000 , bbox_inches='tight',quality=95) 
plt.show()



#نمودار ستونی تعداد مسافر ها برای مبداهای مختلف
import commute
a=commute.popularSource(d).reset_index()
x=(list(a['source']))
x=list(map(str,x))
y=list(a['id'])
v=sum(y)/len(y)
plt.bar(x,y,align='center',color='r')
plt.xticks(x,rotation='vertical')
plt.hlines(v,-0.6,len(x),linestyles='--',colors='y',label='Average')
plt.text(len(x)/2,v,'Average Count='+str(int(v)) ,color='g')
plt.xlim(-0.6,len(x))
plt.title('Source Popularity bar')
plt.xlabel('Source Code')
plt.ylabel('Count of Passengers')
plt.savefig('savepath\Source Popularity' , dpi = 2000 , bbox_inches='tight',quality=95) 
plt.show()

#در نظر گرفتن چند مبدا، مقصد و شرکت پرطرفدار برای بررسی توزیع ها
popularoutes=list(d.groupby('route').count().sort_values('user_id',ascending=False).reset_index()['route'].head(8))                                  
popularsource=list(d.groupby('source').count().sort_values('user_id',ascending=False).reset_index()['source'].head(8))                                  
populardestination=list(d.groupby('destination').count().sort_values('user_id',ascending=False).reset_index()['destination'].head(8))                                  


#بررسی توزیع تعداد مسافر مسیرهای با مسافر بیشتر در مبدا های پر مسافر
a=d.groupby(['source','route']).count().reset_index()
a=d[d['route'].isin(popularoutes) & d['source'].isin(popularsource)]
a=a.groupby(['source','route']).count().reset_index()
a=a[['source','route','id']]
route=list(a['route'].unique())
source=list(a['source'].unique())
s=[]
for i in range(len(route)):
    ss=[]    
    for j in source:
        t=0
        for k in list(a[a['source']==j]['id']):
            if list(a[(a['source']==j) & (a['id']==k)]['route'])[0]==route[i]:
                ss.append(k)
                t=1
        if t==0:
            ss.append(0)
    s.append(ss)
s=s[-len(route):]
import numpy as np
ind=np.arange(len(source))
summ=np.array(s[0])
plt.bar(ind,s[0],width=0.35,label=route[0])
for i in range(1,len(route)):
    plt.bar(ind,s[i],width=0.35,bottom=summ,label=route[i])
    summ=summ+np.array(s[i])
plt.xticks(ind,source)
plt.legend(title='Route')
plt.xlabel('Source Code')
plt.ylabel('Passengers Count')
plt.title('Route Distribution for Top Sources')
plt.savefig('save path/Destination Distribution for Top Companies' , dpi = 2000 , bbox_inches='tight',quality=95) 
plt.show()



#بررسی توزیع تعداد مسافر مسیرهای با مسافر بیشتر در مقصد های پر مسافر
a=d.groupby(['destination','route']).count().reset_index()
a=d[d['route'].isin(popularoutes) & d['destination'].isin(populardestination)]
a=a.groupby(['destination','route']).count().reset_index()
a=a[['destination','route','id']]
route=list(a['route'].unique())
destination=list(a['destination'].unique())
s=[]
for i in range(len(route)):
    ss=[]    
    for j in destination:
        t=0
        for k in list(a[a['destination']==j]['id']):
            if list(a[(a['destination']==j) & (a['id']==k)]['route'])[0]==route[i]:
                ss.append(k)
                t=1
        if t==0:
            ss.append(0)
    s.append(ss)
s=s[-len(route):]
#s=np.array(s).T
import numpy as np
ind=np.arange(len(destination))
summ=np.array(s[0])
plt.bar(ind,s[0],width=0.35,label=route[0])
for i in range(1,len(route)):
    plt.bar(ind,s[i],width=0.35,bottom=summ,label=route[i])
    summ=summ+np.array(s[i])
plt.xticks(ind,destination)
plt.legend(title='Route',prop={'size':6})
plt.xlabel('destination Code')
plt.ylabel('Passengers Count')
plt.title('Route Distribution for Top destinations')
plt.savefig('C:/Users/SMT/Desktop/Project/Modujles/Destination Distribution for Top Companies.png' , dpi = 2000 , bbox_inches='tight',quality=95) 
plt.close()












