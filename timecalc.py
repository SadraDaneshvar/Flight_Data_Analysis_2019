import datetime as dt


#change gharbi to Irani
def sharghigharbi(data):
    def gLeapYear(y):
        if (y%4==0) and ((y%100!=0) or (y%400==0)):
            return True
        else: 
            return False
    
    def sLeapYear(y):
        ary = [1, 5, 9, 13, 17, 22, 26, 30]
        result = False
        b = y%33
        if b in ary: 
            result = True
        return result
    
    def shamsiDate(gyear, gmonth, gday):
        _gl = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
        _g  = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
        
        deydiffjan = 10
        if gLeapYear(gyear-1):  
            deydiffjan = 11
        if gLeapYear(gyear):  
            gd = _gl[gmonth-1]+gday
        else: 
            gd = _g[gmonth-1]+gday
        
        if gd>79:
            sy = gyear - 621
            gd = gd - 79
            if gd<=186:
                gmod = gd%31
                if gmod==0:
                    sd = 31
                    sm = int(gd/31)
                else:
                    sd = gmod
                    sm = int(gd/31) + 1
            else:
                gd = gd - 186
                gmod = gd%30
                if gmod==0:
                    sd = 30
                    sm = int(gd/30) + 6
                else:
                    sd = gmod
                    sm = int(gd/30) + 7
        else:
            sy = gyear - 622
            gd = gd+deydiffjan
            gmod = gd%30
            if gmod==0:
                sd = 30
                sm = int(gd/30) + 9 
            else:
                sd = gmod; 
                sm = int(gd/30) + 10 
    
        result = [sy, sm, sd]
        return result
    global datelist
    datelist=[]
    for i in data['request_date_id']:
        sreq=str(i)
        if sreq!='0':
            x=int(sreq[0:4])
            y=int(sreq[4:6])
            z=int(sreq[6:8])
        else:
            x,y,z=0,0,0
        datelist.append((x,y,z))
    for i in range(len(datelist)):
        datelist[i]=shamsiDate(datelist[i][0],datelist[i][1],datelist[i][2])
    
#اضافه کردن ستون روز شمسی به داده
def rooz(data):    
    dayp=[]    
    for i in data['request_date_id']:
            sreq=str(i)
            if sreq!='0':
                x=int(sreq[0:4])
                y=int(sreq[4:6])
                z=int(sreq[6:8])
                dayofweek=dt.date(x,y,z).strftime('%A')    
                if dayofweek=='Sunday':
                    dayp.append('1shanbe')
                if dayofweek=='Monday':
                    dayp.append('2shanbe')
                if dayofweek=='Tuesday':
                    dayp.append('3shanbe')
                if dayofweek=='Wednesday':
                    dayp.append('4shanbe')
                if dayofweek=='Thursday':
                    dayp.append('5shanbe')
                if dayofweek=='Friday':
                    dayp.append('jomE')
                if dayofweek=='Saturday':
                    dayp.append('shanbe')
    
    data['rooz']=dayp
    return data

#اضافه کردن ستون ماه شمسی به داده
def mah(data):    
    monthp=[]
    persian=['','farvardin','ordibehesht','khordad','tir','mordad','shahrivar','mehr','aban','azar','dey','bahman','esfand']
    for i in datelist:
        monthp.append(persian[i[1]])
    data['mah']=monthp    
    return data

#اضافه کردن ستون سال شمسی به داده
def sal(data):
    yearp=[]
    for i in datelist:
        yearp.append(i[0])
    data['sal']=yearp    
    return data

#اضافه کردن ستون روز میلادی به داده
def dayofweek(data):
    dow=[]    
    for i in data['request_date_id']:
        sreq=str(i)
        if sreq!='0':
            x=int(sreq[0:4])
            y=int(sreq[4:6])
            z=int(sreq[6:8])
            dayofweek=dt.date(x,y,z).strftime('%A')    
            dow.append(dayofweek)
        else:
            dow.append('0')
    data['day_of_the_week']=dow
    return data

#اضافه کردن ستون ماه میلادی به داده
def month(data):
    
    month=[]
    for i in data['request_date_id']:
        sreq=str(i)
        if sreq!='0':
            
            x=int(sreq[0:4])
            y=int(sreq[4:6])
            z=int(sreq[6:8])        
            m=dt.date(x,y,z).strftime('%B')
            month.append(m)
        else:
            month.append('0')
    data['month']=month
    return data

#اضافه کردن ستون سال میلادی به داده
def year(data):           
    year=[]
    for i in data['request_date_id']:
        sreq=str(i)
        if sreq!='0':
            x=int(sreq[0:4])
            y=int(sreq[4:6])
            z=int(sreq[6:8])
            y=dt.date(x,y,z).year    
            year.append(y)
        else:
            year.append('0')            
    data['year']=year
    return data         
    

#اضافه کردن ساعت خرید بلیت
#برای تعیین ساعت های خرید ، بازه های نیم ساعته در نظر گرفته شده اند
def time(data):
    timejustinhour=[]
    for i in data['request_time']:
        if i.minute>30:
            h=i.hour+1
        if i.minute<30:
            h=i.hour
        if h==0:
            h=24
        timejustinhour.append(h)
    data['time_intervals']=timejustinhour
    return data    

#اضافه کردن ستون فاصله زمان خرید بلیت و زمان پرواز
def timedelta(data):
    timedel=[]    
    for i in range(len(data)):
        sreq=str(data.loc[i,'request_date_id'])
        sdep=str(data.loc[i,'departure_date_id'])
        if sreq!='0':
            x=int(sreq[0:4])
            y=int(sreq[4:6])
            z=int(sreq[6:8])
        else:
            x,y,z=1,1,1    
        if sdep!='0':
            x2=int(sdep[0:4])
            y2=int(sdep[4:6])
            z2=int(sdep[6:8])
        else:
            x2,y2,z2=1,1,1
        reqdate=dt.date(x,y,z)
        depdate=dt.date(x2,y2,z2)
        if (x!=1) and (x2!=1):
            
            timedel.append((depdate-reqdate).days)
        else:
            
            timedel.append(None)
            
    data['timedelta']=timedel
    return data



    












