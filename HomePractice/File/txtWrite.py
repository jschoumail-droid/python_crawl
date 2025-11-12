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