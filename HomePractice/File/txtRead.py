#f=open('D:\Github\python_crawl\HomePractice\File\pg37431.txt')

#注意目前目錄為: D:\Github\python_crawl，所以檔案要放在此目錄下，
#   方可使用下列statement執行，即省略指定路徑
f=open('pg37431.txt')

text=f.read()
print(text)
f.close()