# opening files and modules ---------------------------------------------------------------------------------------------- 

import pandas as pd

#پرطرفدارترین کمپانی ها بر حسب تعداد مسافر
def mostPopularcompanybyusercount(data):
    popular = data.groupby(['company']).count().sort_values(['user_id'],ascending=False)['user_id']
    return popular


#پردرآمدترین کمپانی ها
def Richestcompanybyprice(data):
    rich = data.groupby(['company']).sum().sort_values(['price'],ascending=False)['price']
    return rich
        

# problem 2 (most popular and richest airlines per month) -----------------------------------------------------------------

#پرطرفدارترین کمپانی ها بر حسب تعداد مسافر در ماه میلادی
def mostpopularcompanypermonth(data):
    m = data.groupby('month')
    M=[]
    for month , month_df in m:
        M.append(month)
    
    pcm = data.groupby(['month','company']).count()['user_id'].reset_index() # pcm = Popular Company per Month
    rcm = data.groupby(['month','company']).sum()['price'].reset_index() # rcm = Rich Company per Month
    rcm = pd.DataFrame(rcm)
    rcm = pd.DataFrame(pcm)
    pc=[] # Popular Company
    rc=[] # Rich Company
    for i in M:
        pc.append(pd.DataFrame(pcm.loc[pcm['month'] == i].sort_values(['user_id'],ascending=False)['company']).iloc[0,0])    
        rc.append(pd.DataFrame(rcm.loc[rcm['month'] == i].sort_values(['price'],ascending=False)['company']).iloc[0,0])
    ans=pd.DataFrame() # ans1: msot popular company per month
    ans['month'] = M            
    ans['company'] = pc 
    return ans

#پرطرفدارترین کمپانی ها بر حسب تعداد مسافر در ماه های شمسی
def mostpopularcompanypermonthpersian(data):
    m = data.groupby('mah')
    M=[]
    for mah , mah_df in m:
        M.append(mah)
    
    pcm = data.groupby(['mah','company']).count()['user_id'].reset_index() # pcm = Popular Company per mah
    rcm = data.groupby(['mah','company']).sum()['price'].reset_index() # rcm = Rich Company per mah
    rcm = pd.DataFrame(rcm)
    rcm = pd.DataFrame(pcm)
    pc=[] # Popular Company
    rc=[] # Rich Company
    for i in M:
        pc.append(pd.DataFrame(pcm.loc[pcm['mah'] == i].sort_values(['user_id'],ascending=False)['company']).iloc[0,0])    
        rc.append(pd.DataFrame(rcm.loc[rcm['mah'] == i].sort_values(['price'],ascending=False)['company']).iloc[0,0])
    ans=pd.DataFrame() # ans1: msot popular company per mah
    ans['mah'] = M            
    ans['company'] = pc 
    return ans
    
#پردرآمدترین کمپانی ها بر حسب ماه میلادی
def richestcompanypermonth(data):
    m = data.groupby('month')
    M=[]
    for month , month_df in m:
        M.append(month)
    
    pcm = data.groupby(['month','company']).count()['user_id'].reset_index() # pcm = Popular Company per Month
    rcm = data.groupby(['month','company']).sum()['price'].reset_index() # rcm = Rich Company per Month
    rcm = pd.DataFrame(rcm)
    rcm = pd.DataFrame(pcm)
    pc=[] # Popular Company
    rc=[] # Rich Company
    for i in M:
        pc.append(pd.DataFrame(pcm.loc[pcm['month'] == i].sort_values(['user_id'],ascending=False)['company']).iloc[0,0])    
        rc.append(pd.DataFrame(rcm.loc[rcm['month'] == i].sort_values(['price'],ascending=False)['company']).iloc[0,0])
    
    ans=pd.DataFrame() 
    ans['month'] = M
    ans['company'] = rc
    return ans

#پردرآمدترین کمپانی ها بر حسب ماه شمسی
def richestcompanypermonth_persian(data):
    m = data.groupby('mah')
    M=[]
    for mah , mah_df in m:
        M.append(mah)
    
    pcm = data.groupby(['mah','company']).count()['user_id'].reset_index() # pcm = Popular Company per mah
    rcm = data.groupby(['mah','company']).sum()['price'].reset_index() # rcm = Rich Company per mah
    rcm = pd.DataFrame(rcm)
    rcm = pd.DataFrame(pcm)
    pc=[] # Popular Company
    rc=[] # Rich Company
    for i in M:
        pc.append(pd.DataFrame(pcm.loc[pcm['mah'] == i].sort_values(['user_id'],ascending=False)['company']).iloc[0,0])    
        rc.append(pd.DataFrame(rcm.loc[rcm['mah'] == i].sort_values(['price'],ascending=False)['company']).iloc[0,0])
    
    ans=pd.DataFrame()
    ans['mah'] = M
    ans['company'] = rc
    return ans




# problem 3 (most popular and richest airlines from each source )


#پرطرفدارترین کمپانی ها بر حسب مبدا ها
def mostpopularcompanybysource(data):
    s = data.groupby('source')
    S=[]
    for source , source_df in s:
        S.append(source)
    
    pcs = data.groupby(['source','company']).count()['user_id'].reset_index() # pcs = Popular Company per Source
    pcs = pd.DataFrame(pcs)
    rcs = data.groupby(['source','company']).sum()['price'].reset_index() # rcs = Richest Company per Source
    rcs = pd.DataFrame(rcs)
    k1=[]
    k2=[]
    for i in S:
        k1.append(pd.DataFrame(pcs.loc[pcs['source'] == i].sort_values(['user_id'],ascending=False)['company']).iloc[0,0])
        k2.append(pd.DataFrame(rcs.loc[rcs['source'] == i].sort_values(['price'],ascending=False)['company']).iloc[0,0])
    
    ans=pd.DataFrame() 
    ans['source'] = S
    ans['company'] = k1
    return ans
    
#پردرآمدترین کمپانی ها بر حسب مبدا ها
def richestcompanybysource(data):
    s = data.groupby('source')
    S=[]
    for source , source_df in s:
        S.append(source)
    
    pcs = data.groupby(['source','company']).count()['user_id'].reset_index() # pcs = Popular Company per Source
    pcs = pd.DataFrame(pcs)
    rcs = data.groupby(['source','company']).sum()['price'].reset_index() # rcs = Richest Company per Source
    rcs = pd.DataFrame(rcs)
    k1=[]
    k2=[]
    for i in S:
        k1.append(pd.DataFrame(pcs.loc[pcs['source'] == i].sort_values(['user_id'],ascending=False)['company']).iloc[0,0])
        k2.append(pd.DataFrame(rcs.loc[rcs['source'] == i].sort_values(['price'],ascending=False)['company']).iloc[0,0])
    
    
    ans=pd.DataFrame() 
    ans['source'] = S
    ans['company'] = k2
    return ans



# problem 4 (most popular and richest companies per destination) -----------------------------------------------------------

#پرطرفدارترین کمپانی ها بر حسب مقصدها
def mostpopularcompanybydestination(data):
    s = data.groupby('destination')
    S=[]
    for destination , destination_df in s:
        S.append(destination)
    
    pcd = data.groupby(['destination','company']).count()['user_id'].reset_index() # pcd = Popular Company per Destination
    pcd = pd.DataFrame(pcd)
    rcd = data.groupby(['destination','company']).sum()['price'].reset_index() # rcd = Rich Company per Destination
    rcd = pd.DataFrame(rcd)
    k3=[]
    k4=[]
    for i in S:
        k3.append(pd.DataFrame(pcd.loc[pcd['destination'] == i].sort_values(['user_id'],ascending=False)['company']).iloc[0,0])
        k4.append(pd.DataFrame(rcd.loc[rcd['destination'] == i].sort_values(['price'],ascending=False)['company']).iloc[0,0])
    
    ans5=pd.DataFrame() # ans5: msot popular company per destination
    ans5['destination'] = S
    ans5['company'] = k3
    return ans5
    ans6=pd.DataFrame() # ans6: msot rich company per destination
    ans6['destination'] = S
    ans6['company'] = k4
    
#پردرآمدترین کمپانی ها بر حسب مقصدها
def richestcompanybydestination(data):
    s = data.groupby('destination')
    S=[]
    for destination , destination_df in s:
        S.append(destination)
    
    pcd = data.groupby(['destination','company']).count()['user_id'].reset_index() # pcd = Popular Company per Destination
    pcd = pd.DataFrame(pcd)
    rcd = data.groupby(['destination','company']).sum()['price'].reset_index() # rcd = Rich Company per Destination
    rcd = pd.DataFrame(rcd)
    k3=[]
    k4=[]
    for i in S:
        k3.append(pd.DataFrame(pcd.loc[pcd['destination'] == i].sort_values(['user_id'],ascending=False)['company']).iloc[0,0])
        k4.append(pd.DataFrame(rcd.loc[rcd['destination'] == i].sort_values(['price'],ascending=False)['company']).iloc[0,0])
    
    
    ans=pd.DataFrame() # ans6: msot rich company per destination
    ans['destination'] = S
    ans['company'] = k4
    return ans
