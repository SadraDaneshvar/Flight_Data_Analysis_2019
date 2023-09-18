#موارد مربوط به خواسته1,2


#خواندن کتابخانه
import pandas as pd
import timecalc
import costumers
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

#تعیین امتیاز برای فضای باشگاه مشتری
#دادن چهار امتیاز برای چهار گروه هر شرکت
costumers.pointset()
#ذخیره فایل سی اس وی امتیازدهی هر کاربر در شرکتهای مختلف
a = costumers.pointwithcompanydevide(d)
company_list=sorted(list(d.company.unique())) 
for i in range(len(company_list)):
    a[i].to_csv(str(company_list[i])+'.csv',index=False) 

 

#تعیین بیشینه درصد تخفیف
a=costumers.percentdevided(d)
company_list=sorted(list(d.company.unique())) 
for i in range(len(company_list)):
    a[i].to_csv(str(company_list[i])+'.csv',index=False) 










    
#ذخیره فایل سی اس وی تخفیف ها برای شرکتهای مختلف
    
    




















