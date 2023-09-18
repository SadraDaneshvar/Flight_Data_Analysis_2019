def pointset(a=0,b=1,c=2,d=3):
        #ساختار امتیاز بندی
    global point
    point=[]
    
    point.insert(0, int(a))
    point.insert(1, int(b))
    point.insert(2, int(c))
    point.insert(3, int(d))
    return point


def pointkolli(data):
    #میانگین، کمینه، بیشینه خرید کلی از هر کمپانی
    average_prices=int(data['price'].mean())
    min_prices=int(data['price'].min())
    max_prices=int(data['price'].max())
    #به دست آوردن مرزهای بازه ها
    charak_1=(min_prices+average_prices)/2
    charak_3=(max_prices+average_prices)/2
    charak_2=average_prices
    pointkolli=[]
    s=data.groupby(['user_id'])['price'].mean().reset_index()
    for i in s['price']:
        if (int(i)<=charak_1):
            pointkolli.append(point[0])
        if (int(i)>charak_1) and (int(i)<=charak_2):
            pointkolli.append(point[1])
        if (int(i)>charak_2) and (int(i)<=charak_3):
            pointkolli.append(point[2])
        if (int(i)>charak_3):
            pointkolli.append(point[3])
    s['pointkolli']=pointkolli
    return s            
 
        
def pointwithcompanydevide(d):
    company_list=sorted(list(d.company.unique()))    
    c=d.groupby('company')
    company_dataframes=[]
    #جدا کردن کمپانی ها
    for company , company_df in c:
        company_dataframes.append(company_df)
    
    #تعداد خرید کلی از هر کمپانی بدون در نظر گرفتن خرید توسط مشتری تکراری
    buys_count=[]
    for i in range (len(company_list)):
        buys_count.append(len(company_dataframes[i]))
    
    #تعداد مشتری هایی که از هر کمپانی خرید کرده اند
    company_users=[]
    for i in range (len(company_list)):
        cdf=company_dataframes[i].groupby(['user_id'])
        company_users.append(len(cdf)) 
#تعیین چارک
    avg=list(d.groupby(['company'])['price'].mean())
    mins=list(d.groupby(['company'])['price'].min())
    maxs=list(d.groupby(['company'])['price'].max())
    charak_1=[(mins[i]+avg[i])/2 for i in range(len(company_list))]
    charak_3=[(maxs[i]+avg[i])/2 for i in range(len(company_list))]
    #امتیازدهی بر اساس گروه های داخل چارکها
    dataframes_with_points=[]
    for i in range (len(company_list)):
        a1=company_dataframes[i].groupby(['user_id'])['price'].mean()
        a2=a1.reset_index()
        a2['points']=0
        for j in range (int(company_users[i])):
            if float(mins[i])<=float(a2['price'][j])<=float(charak_1[i]):
                a2['points'][j]+=point[0]
            elif float(charak_1[i])<=float(a2['price'][j])<=float(avg[i]):
                a2['points'][j]+=point[1]
            elif float(avg[i])<=float(a2['price'][j])<=float(charak_3[i]):
                a2['points'][j]+=point[2]
            elif float(charak_3[i])<=float(a2['price'][j])<=float(maxs[i]):
                a2['points'][j]+=point[3]
        dataframes_with_points.append(a2[['user_id','points']])
    return dataframes_with_points
#تعیین ماکسیمم درصد تخفیف
def percentset(a):
    global maxpercent
    maxpercent=a


# این تابع یک ستون ایجاد میکند که حاصل از جمع تخفیف ناشی از میانگین خرید کاربر و فاصله او با زمان پرواز است
def pointdeltagheimat(d):
    p=maxpercent/2
    
    f=d.groupby(['user_id','company']).mean().reset_index()
    f=f.fillna(0)
    takhfif=[]
    a=[]    
    for i in list(f['timedelta']):
        if i>0:
            a.append(i)
        
    takhfif1=[]
    takhfif2=[]
    averagedelta=sum(a)/len(a)
    for i in a:
        if i/averagedelta>=3:
            takhfif.append([p,1])
            takhfif1.append(i)
        else:
            takhfif.append([i,0])
    
    for i in takhfif:
        if i[1]==0:
            takhfif2.append(i[0])
    takhfifasli=[]
    for i in f['timedelta']:
        if i<=0:
            takhfifasli.append(-1)
        if i>0:
            if i in takhfif1:
                takhfifasli.append(p)
            if i in takhfif2:
                takh=(i/(max(takhfif2)-min(takhfif2)))*p
                takhfifasli.append(takh)
    f= d.groupby(['user_id','company']).mean().reset_index()[['user_id','company','price']]       
    a=[]
    for i in list(f['price']):
        if i>0:
            a.append(i)
        
    takhfif1=[]
    takhfif2=[]
    takhfif=[]
    averageprice=sum(a)/len(a)
    for i in a:
        if i/averageprice>=3:
            takhfif.append([10,1])
            takhfif1.append(i)
        else:
            takhfif.append([i,0])
    
    for i in takhfif:
        if i[1]==0:
            takhfif2.append(i[0])
    takhfifasli2=[]
    for i in f['price']:
        if i<=0:
            takhfifasli.append(-1)
        if i>0:
            if i in takhfif1:
                takhfifasli2.append(p)
            if i in takhfif2:
                takh=(i/(max(takhfif2)-min(takhfif2)))*p
                takhfifasli2.append(takh)
    import numpy as np
    t=np.array(takhfifasli)
    t2=np.array(takhfifasli2)
    a=d.groupby(['user_id','company']).mean().reset_index()
    a['takhfif']=list(t+t2)
    return a
#این تابع یک لیست خروچی شامل ستون تخفیف با تقسیم دیتا به بخش هایی که هر کدام مربوط به یک شرکت خاص هستند خروجی میدهد
def percentdevided(d):
    company_dataframes=[]
    company_list=sorted(list(d.company.unique()))
    for i in company_list:
        company_dataframes.append(d[d['company']==i])
    takhfifdevided=[]
    for i in company_dataframes:
        a=pointdeltagheimat(i)
        takhfifdevided.append(a)
    return takhfifdevided
            
            
