import pandas as pd
d = pd.read_excel(r'C:\Users\SMT\Desktop\Documents\Book1.xlsx') 
d.isna().sum() # تعدادداده هایی که عدد نیستند در هر ستون
d = d.dropna() # حذف سطر هایی که داده های غیر عدد دارند
d.duplicated() # خطوطی که شبیه آن ها در داده وجود دارد را نشان می دهد
d.isin([0]).sum() # تعداد داده هایی که 0 هستند را نشان می دهد
# کد زیر تعداد افرادی را که همزمان بلیت خریداری کرده اند را نشان می دهد
l = list(d.columns)[1:]
a=d.groupby(l).count()
len(a)
# کد زیر سطری که دارای قیمیت ناهنجار " 0.03 " است را حذف می کند
d = d[d['price'] > 1]

d.to_excel('path.xlsx')

