'''
Python 的標準函式「os」提供了操作系統中檔案的方法,可以針對檔案進行重新命名、編輯、刪除等相關操作
os 模組常用的方法
https://docs.python.org/zh-tw/3/library/os.html
方法	 參數	  說明
getcwd()		     取得目前程式的工作資料夾路徑
chdir()   path	     改變程式的工作資料夾路徑
mkdir()   folder	 建立資料夾
rmdir()	  folder	 刪除空資料夾
listdir() folder	 列出資料夾裡的內容
open()	  file, mode 開啟檔案
write()	  string	 寫入內容到檔案
rename()  old, new 	 重新命名檔案
remove()  file	     刪除檔案
stat()	  file	     取得檔案的屬性
close()   file	     關閉檔案
path		         取得檔案的各種屬性
system		         執行系統命令 ( 等同使用 cmd 或終端機輸入指令 )
'''

#ex1
print('=====ex1=====')
'''
os.getcwd() 可以取得 .py 程式運作的工作資料夾路徑
'''
import os
print(os.getcwd())   # D:\Github\python_crawl

#ex2
print('=====ex2=====')
'''
os.chdir(path) 可以修改 .py 程式運作的工作資料夾為指定的路徑 path
'''
import os
os.chdir('Homepractice/Stdfunlibrary/OS/File')
print('change directory to',os.getcwd())
# 原本在 D:\Github\python_crawl，改到 D:\Github\python_crawl\
#           Homepractice/Stdfunlibrary\OS\File
#f = open('pg37431.txt','r')
f = open('txtFile.txt','r')
print(f.read())    # hello world
f.close()

#ex2
print('=====ex2=====')
'''
os.mkdir(folder) 可以在指定的目錄下，建立一個新的資料夾
'''
import os
os.chdir('D:\work')
print('change directory to',os.getcwd())
os.mkdir('demo')         # 建立一個名為 demo 的資料夾
print('make dir: demo')
#os.mkdir('demo/hello')

#ex3
print('=====ex3=====')
'''
os.rmdir(folder) 會刪除一個「空」的資料夾 ( 裡面不能有其他檔案或資料夾 )
'''
import os
os.chdir('D:\work')
os.rmdir('demo')
print('remove dir: demo')

#ex4
print('=====ex4=====')
'''
os.listdir(folder) 會以串列的形式，列出資料夾中所有的內容
'''
import os
os.chdir('D:\Github\python_crawl\Homepractice/Stdfunlibrary\OS')
print('change directory to',os.getcwd())
print("List all content in .\File dir :\n",os.listdir('File'))

#ex5
print('=====ex5=====')
'''
os.open(file, mode) 可以開啟指定的檔案，開啟檔案時需要設定模式 mode,
如果需要多種模式可使用「|」區隔
模式	    說明
os.O_RDONLY	以只讀的方式打開
os.O_WRONLY	以只寫的方式打開
os.O_RDWR	以讀寫的方式打開
os.O_APPEND	以追加的方式打開
os.O_CREAT	建立並打開一個新檔案

os.close(file) 可以將開啟的檔案關閉，釋放記憶體
'''

import os
os.chdir('D:\work')
print('change directory to',os.getcwd())
f = os.open('demo.txt', os.O_RDWR|os.O_CREAT)   # 建立一個可讀寫的 demo.txt
print('open demo.txt')
os.close(f)

#ex6
print('=====ex6=====')
'''
os.write(file, str) 可以將指定的文字寫入檔案裡，如果執行過程中出現「TypeError: a bytes-like object is required, not 'str'」的問題，表示寫入的編碼需要轉換
只需要在後方加入「.encode」就能順利完成
'''
import os
os.chdir('D:\work')
print('change directory to',os.getcwd())
f = os.open('demo.txt', os.O_RDWR)     # 開啟 demo.txt 檔案
str = 'good morning!!!'                # 設定寫入的文字
#os.write(f, str)
os.write(f, str.encode())              # 將文字寫入檔案
print('write good morning! in demo.txt')
os.close(f)

#ex7
print('=====ex7=====')
'''
os.remove(file) 可以刪除指定的檔案
'''
import os
os.chdir('D:\work')
print('change directory to',os.getcwd())
os.remove('demo.txt')     # 刪除 test.txt

#ex8
print('=====ex8=====')
'''
os.rename(old, new) 可以將指定的檔案更換名稱，如果有副檔名表示檔案，如果沒有副檔名表示資料夾
'''
import os
os.chdir('D:\work')
print('change directory to',os.getcwd())
os.rename('demo1.txt','test1.txt')    # 將 demo.txt 更名為 test.txt
print('rename demo1.txt to test1.txt')
#os.rename('demo', 'demo2')           # 將 demo 資料夾更名為 demo2

#ex9
print('=====ex9=====')
'''
os.stat(file) 可以取得指定檔案的屬性
'''
import os
os.chdir('D:\work\Test')
print('change directory to',os.getcwd())
print('status of file area.py')
print(os.stat('area.py'))