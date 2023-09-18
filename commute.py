

import pandas as pd

#پیداکردن مسیرهای پرواز
def routes(data):
    #data['route']=str(data['source'])+'to'+str(data['destination'])
    a=[]
    for i in range(len(data)):
        s=str(data.loc[i,'source']) + ' to ' + str(data.loc[i,'destination'])
        a.append(s)
    data['route']=a        
    return data

#پرطرفدارترین مقصدها
def popularDestination(data):
    g1 = data.groupby(['destination']).count().sort_values(['id'],ascending=False)['id']
    return g1

#پرطرفدارترین مقصدها بر حسب ماه میلادی
def mostpopulardestinationbymonth(data):
    pdm = data.groupby(['month','destination']).count()['user_id'].reset_index()
    pdm = pd.DataFrame(pdm)    
    U=[]
    m = data.groupby('month')
    M=[]
    for month , month_df in m:
        M.append(month)
        
    for i in M:
        U.append(pd.DataFrame(pdm.loc[pdm['month'] == i].sort_values(['user_id'],ascending=False)['destination']).iloc[0,0])
        
    ans=pd.DataFrame() # ans7: most popular destinations per month
    ans['month'] = M
    ans['destination'] = U
    return ans

#پرطرفدارترین مقصدها بر حسب ماه شمسی
def mostpopulardestinationbymahpersian(data):
    pdm = data.groupby(['mah','destination']).count()['user_id'].reset_index()
    pdm = pd.DataFrame(pdm)    
    U=[]
    m = data.groupby('mah')
    M=[]
    for mah , mah_df in m:
        M.append(mah)
        
    for i in M:
        U.append(pd.DataFrame(pdm.loc[pdm['mah'] == i].sort_values(['user_id'],ascending=False)['destination']).iloc[0,0])
        
    ans=pd.DataFrame() # ans7: most popular destinations per mah
    ans['mah'] = M
    ans['destination'] = U
    return ans

#پرطرفدارترین مبداها
def popularSource(data):
    g2 = data.groupby(['source']).count().sort_values(['id'],ascending=False)['id']
    return g2

#پیدا کردن شهر هایی که تعداد پروازهای خروجی از آن ها از تعداد پروازهای وارد شده به آن ها بیشتر بوده است (یا به عبارتی بیشتر مبدا پرواز بوده اند)
def ImmigrationSource(data):
    g1 = data.groupby(['destination']).count().sort_values(['id'],ascending=False)['id'].reset_index()
    g2 = data.groupby(['source']).count().sort_values(['id'],ascending=False)['id'].reset_index()
    city = list(g2['source'])
    dif=[]  
    for i in g2['source']:
        for j in g1['destination']:
            if i == j:
                dif.append(((g2.loc[g2['source']==i]).iloc[0,1]) - ((g1.loc[g1['destination']==j]).iloc[0,1]))   
    
    e = pd.DataFrame()
    e['city'] = city
    e['dif'] = dif
    mf = e.sort_values(['dif'],ascending=False).loc[e['dif']>0] # migrated from
    return mf   

#پیدا کردن شهر هایی که تعداد پروازهای خروجی از آن ها از تعداد پروازهای وارد شده به آن ها کمتر بوده است (یا به عبارتی بیشتر مقصد پرواز بوده اند)
def ImmigrationDestination(data):
    g1 = data.groupby(['destination']).count().sort_values(['id'],ascending=False)['id'].reset_index()
    g2 = data.groupby(['source']).count().sort_values(['id'],ascending=False)['id'].reset_index()
    city = list(g2['source'])
    dif=[]  
    for i in g2['source']:
        for j in g1['destination']:
            if i == j:
                dif.append(((g2.loc[g2['source']==i]).iloc[0,1]) - ((g1.loc[g1['destination']==j]).iloc[0,1]))   
    
    e = pd.DataFrame()
    e['city'] = city
    e['dif'] = dif
    mt = e.sort_values(['dif']).loc[e['dif']<0] # migrated to
    return mt    

        
    

     