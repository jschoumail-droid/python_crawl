#使用 datetime 必須先 import datetime 模組，或使用 from 的方式，單獨 import 特定的類型
'''
import datetime
from datetime import date
'''
#ex1
print("=====ex1=====")
'''
datetime.date 可以處理日期相關的操作,本身包含三個屬性:year、month 和 day,分別用逗號區隔
'''
import datetime
d = datetime.date(2020,1,1)   # 2020-01-01
print(d)

#ex2
print("=====ex2=====")
'''
執行了 today() 的方法，印出今天的日期 (使用 ISO 格式的日期字串),
回傳目前的西元年、月、日
'''
import datetime
today = datetime.date.today()
print(today)     # 2025-11-17

#ex3
print("=====ex3=====")
'''
取得日期後，可以使用下面幾種常用的方法，進一步取出日期的資訊進行操作
year	取得西元年
month	取得月份
day 	取得日期
replace()	取代日期，產生新的物件
weekday()	回傳一星期中的第幾天，星期一為 0
isoweekday()	回傳一星期中的第幾天，星期一為 1
isocalendar()	回傳一個 tuple,內容分別是 ( 年、第幾週、isoweekday )
isoformat()	回傳 ISO 格式的日期字串
ctime() 	回傳日期和時間的字串
strftime()	回傳特定格式字串所表示的時間(詳細可參考 strftime() 和 strptime())
'''
import datetime
today = datetime.date.today()
print(today)                 # 2021-10-19
print(today.year)            # 2021
print(today.month)           # 10
print(today.day)             # 19
print(today.weekday())       # 1    ( 因為是星期二，所以是 1 )
print(today.isoweekday())    # 2    ( 因為是星期二，所以是 2 )
print(today.isocalendar())   # (2021, 42, 2)  ( 第三個數字是星期二，所以是 2 )
print(tuple(today.isocalendar()))
print(today.isoformat())     # 2021-10-19
print(today.ctime())         # Tue Oct 19 00:00:00 2021
print(today.strftime('%Y.%m.%d'))    # 2021.10.19

newDay = today.replace(year=2020)
print(newDay)                # 2020-10-19

#ex4
print("=====ex4=====")
'''
利用「.days」的屬性,計算出兩個日期差了幾天
'''
import datetime
d1 = datetime.date(2020, 6, 24)
d2 = datetime.date(2021, 11, 24)
print(abs(d1-d2).days)       # 518

#ex5
print("=====ex5=====")
'''
datetime.time 可以處理時間相關的操作,本身包含下列幾個屬性:
hour、minute、second、microsecond 和 tzinfo,分別用逗號區隔
'''
import datetime
thisTime = datetime.time(12,0,0,1)
print(thisTime)   # 12:00:00.000001

#ex6
print("=====ex6=====")
'''
tzinfo 是時區的選項，預設 None 採用 UTC 時區，如果要轉換成台灣 UTC+8 的時區可採用下方的寫法
'''
import datetime
thisTime = datetime.time(14,0,0,1,tzinfo=datetime.timezone(datetime.timedelta(hours=8)))
print(thisTime)    # 14:00:00.000001+08:00

#ex7
print("=====ex7=====")
'''
使用 datetime.time 將字串轉換為時間物件後，就能透過下面幾種常用的方法，取出時間的資訊
hour	取得小時
minute	取得分鐘
second	取得秒數
microsecond	取得微秒數 (1/1000000 秒)
replace()	取代時間，產生新的物件
isoformat()	回傳 ISO 格式的時間字串
tzname()	回傳目前時區資訊
strftime()	回傳特定格式字串所表示的時間 ( 詳細可參考 strftime() 和 strptime() )
'''
import datetime
thisTime = datetime.time(14,0,0,1,tzinfo=datetime.timezone(datetime.timedelta(hours=8)))
print(thisTime)               # 14:00:00.000001+08:00
print(thisTime.isoformat())   # 14:00:00.000001+08:00
print(thisTime.tzname())      # UTC+08:00
print(thisTime.strftime('%H:%M:%S'))   # 14:00:00

#newTime = datetime.date.today().replace(hour=20) #error
'''
print(datetime.datetime.today()) #correct
newTime = datetime.datetime.today().replace(hour=20)
'''
newTime = thisTime.replace(hour=20)
print(newTime)                # 20:00:00.000001+08:00

#ex8
print("=====ex8=====")
'''
datetime.datetime 可以處理日期與時間相關的操作,本身包含下列幾個屬性:
year、month、dayhour、minute、second、microsecond 和 tzinfo,分別用逗號區隔
'''
import datetime
thisTime = datetime.datetime(2020,1,1,20,20,20,20)
print(thisTime)    # 2020-01-01 20:20:20.000020

#ex9
print("=====ex9=====")
'''
datetime.datetime 有下面幾個主要的方法
today()	回傳目前的日期與時間
now()	回傳目前的日期與時間，可加入 tz 參數設定時區
utcnow()	回傳目前的日期與時間
'''
import datetime
print(datetime.datetime.today())    # 2025-11-17 17:08:59.895027
print(datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))))
# 2025-11-17 17:08:59.895026+08:00
print(datetime.datetime.utcnow())   # 2025-11-17 09:08:59.895026

#ex10
print("=====ex10=====")
'''
使用 datetime.datetime 將字串轉換為日期時間物件後，就能透過下面幾種常用的方法，取出的日期時間資訊
year	取得西元年
month	取得月份
day	取得日期
hour	取得小時
minute	取得分鐘
second	取得秒數
microsecond	取得微秒數 (1/1000000 秒)
weekday()	回傳一星期中的第幾天，星期一為 0
isoweekday()	回傳一星期中的第幾天，星期一為 1
isocalendar()	回傳一個 tuple,內容分別是 ( 年、第幾週、isoweekday )
isoformat()	回傳 ISO 格式的日期字串
ctime()	回傳日期和時間的字串
timetuple()	回傳日期與時間所組成的 time.struct_time 物件
strftime()	回傳特定格式字串所表示的時間 ( 詳細可參考 strftime() 和 strptime() )
'''
import datetime
now = datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8)))
print(now)                # 2025-11-17 17:14:01.581065+08:00
print(now.date())         # 2025-11-17
print(now.time())         # 17:14:01.581065
print(now.tzname())       # UTC+08:00
print(now.weekday())      # 0
print(now.isoweekday())   # 1
print(now.isocalendar())  # datetime.IsoCalendarDate(year=2025, week=47, weekday=1)
print(tuple(now.isocalendar()))
print(now.isoformat())    # 2025-11-17T17:16:20.815025+08:00
print(now.ctime())        # Mon Nov 17 17:16:20 2025
print(now.strftime('%Y/%m/%d %H:%M:%S'))  # 2025/11/17 17:16:20
print(now.timetuple())
# time.struct_time(tm_year=2025, tm_mon=11, tm_mday=17, tm_hour=17,
#                  tm_min=16, tm_sec=20, tm_wday=0, tm_yday=321, tm_isdst=-1)

#ex11
print("=====ex11=====")
'''
要進行日期或時間的計算，可以透過 datetime.timedelta 增加或減少日期或時間，
本身包含 days、seconds、microseconds、milliseconds、minutes、hours、weeks 的屬性，
屬性的預設值都是 0
使用 datetime.timedelta 只需要將其放在日期或時間物件後方，就回傳計算後的時間
'''
import datetime
today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)
nextweek = today + datetime.timedelta(weeks=1)
print(today)       # 2025-11-17 17:22:07.658018
print(yesterday)   # 2025-11-16 17:22:07.658018
print(tomorrow)    # 2025-11-18 17:22:07.658018
print(nextweek)    # 2025-11-24 17:22:07.658018

#ex11
print("=====ex11=====")
'''
datetime.timezone 負責時區的轉換，主要和 datetime.datetime、datetime.time 互相搭配使用
datetime.timedelta 裡 hours 的數值，可以參考：時區列表，台灣處在 GMT+8 的時區，
所以 hours 等於 8,如果是日本，因為是 GTM+9,hours 就要設定為 9。
'''
import datetime
tzone = datetime.timezone(datetime.timedelta(hours=8))
now = datetime.datetime.now(tz=tzone)
print(now)    # 2025-11-17 17:25:47.987843+08:00