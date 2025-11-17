#ex1
print('=====ex1=====')
#建立一個包含時區的datetime
import datetime
from dateutil import tz

d=datetime.datetime(1989,4,24,10,11,tzinfo=tz.gettz("Europe/Madrid"))
print(d)

#ex2
print('=====ex2=====')
'''
跨時區的時間比較
'''
import datetime
from dateutil import tz

d1=datetime.datetime(1989,4,24,hour=11,tzinfo=tz.gettz("Europe/Madrid"))
d2=datetime.datetime(1989,4,24,hour=8,tzinfo=tz.gettz("America/Los_Angeles"))
print(d1.hour>d2.hour) #True
print(d1>d2) #False

#ex3
print('=====ex3=====')
'''
轉換時區
'''
import datetime
from dateutil import tz

d2=datetime.datetime(1989,4,24,hour=8,tzinfo=tz.gettz("America/Los_Angeles"))
d2_madrid=d2.astimezone(tz.gettz("Europe/Madrid"))
print("America/Los_Angeles",d2)
print("Europe/Madrid",d2_madrid)
#print(d2_madrid.hour)

#ex4
print('=====ex4=====')
'''
計算兩個datetime物件的時間差
'''
import datetime as dt

d1=dt.datetime(2019,2,25,10,50,tzinfo=dt.timezone.utc)
d2=dt.datetime(2019,2,26,11,20,tzinfo=dt.timezone.utc)
td=d2-d1
print(td.total_seconds())

#ex5
print('=====ex5=====')
'''
轉成ISO 8601標準的字串
'''
d1=dt.datetime.now(dt.timezone.utc)
print(d1)
print(d1.isoformat())

#ex6
print('=====ex6=====')
'''
計算Unix/POXIS紀元時間
使用datetime和time取得兩種當前時間
比較時 datetime, 要使用UTC時區,因為time.time回傳Unix紀元時間是使用UTC時區時間
'''
import datetime as dt
import time

time_now=time.time()
datetime_now=dt.datetime.now(dt.timezone.utc)
print(time_now)
print(datetime_now)

epoch=datetime_now-dt.timedelta(seconds=time_now)
print(epoch)
