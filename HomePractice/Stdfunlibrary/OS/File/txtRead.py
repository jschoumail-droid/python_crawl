'''
模式字串   當開啟檔案已存在        當開啟檔案不存在

r         開啟唯讀的檔案            產生錯誤
w         清除檔案內容後寫入         建立寫入檔案
a         開啟檔案從檔尾後寫入       建立寫入檔案
r+        開啟讀寫的檔案            產生錯誤
w+        清除檔案內容後讀寫內容     建立讀寫檔案
a+        開啟檔案從檔尾後開始讀寫   建立讀寫檔案
'''

#f=open('D:\Github\python_crawl\HomePractice\File\pg37431.txt')

#注意目前目錄為: D:\Github\python_crawl，所以檔案要放在此目錄下，
#   方可使用下列statement執行，即省略指定路徑
'''f=open('pg37431.txt')
text=f.read()
print(text)
f.close()'''

with open('pg37431.txt') as f:
    print(f.read(5))
    print(f.readline())#從目前檔案指標讀至此列結束(含\n)