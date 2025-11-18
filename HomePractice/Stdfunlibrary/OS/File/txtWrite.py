'''
模式字串   當開啟檔案已存在        當開啟檔案不存在

r         開啟唯讀的檔案            產生錯誤
w         清除檔案內容後寫入         建立寫入檔案
a         開啟檔案從檔尾後寫入       建立寫入檔案
r+        開啟讀寫的檔案            產生錯誤
w+        清除檔案內容後讀寫內容     建立讀寫檔案
a+        開啟檔案從檔尾後開始讀寫   建立讀寫檔案
'''
from datetime import datetime
import time

#注意: 目前目錄為: D:\Github\python_crawl，若省略指定路徑，則檔案會在此目前目錄下開啟
f=open('log.txt','w')
for i in range(10):
    print(datetime.now().strftime('%Y%m%d_%H:%M:%S - '),i)
    f.write(datetime.now().strftime('%Y%m%d_%H:%M:%S - '))
    time.sleep(1)
    f.write(str(i))
    f.write('\n')
f.close()