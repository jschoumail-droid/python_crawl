'''
os.path 可以取得檔案的各種屬性,os.path 具有下列幾種常用的使用方法
方法	說明
abspath(path)	回傳絕對路徑。
basename(path)	回傳檔案名稱。
dirname(path)	回傳檔案路徑。
exists(path)	判斷檔案路徑是否存在，回傳 True 或 False。
getatime(path)	回傳最近訪問時間（浮點型秒數）
getmtime(path)	回傳最近修改檔案的時間 ( 1970 年 1 月 1 日 00:00:00 開始到修改檔案的秒數 )
getctime(path)	回傳建立檔案時間。
getsize(path)	回傳檔案大小。
isabs(path)	判斷是否為絕對路徑，回傳 True 或 False。
isfile(path)	判斷路徑是否為文件，回傳 True 或 False。
isdir(path)	判斷路徑是否為目錄，回傳 True 或 False。
join(path1, path2....)	把目錄和檔案名合成一個路徑
realpath(path)	回傳 path 的真實路徑
relpath(path, start)	從 start 計算相對路徑
samefile(path1, path2)	判斷兩個檔案或目錄是否相同
sameopenfile(fp1, fp2)	判斷 fp1 和 fp2 是否指向同一檔案
samestat(stat1, stat2)	判斷stat tuple stat1 和 stat2 是否指向同一個文件
split(path)	把路徑分割成 dirname 和 basename，返回一個元組
splitext(path)	分割路徑，返回路徑名和文件副檔名的檔案
'''
import os
path = 'D:\work\demo2.txt'
print(os.path.basename(path))   # demo2.txt
print(os.path.dirname(path))    # D:\work
print(os.path.exists(path))     # True
print(os.path.getatime(path))   # 1763438085.4469898
print(os.path.getmtime(path))   # 1763437773.2605913
print(os.path.getctime(path))   # 1763438085.4469898
print(os.path.getsize(path))    # 15
print(os.path.isabs(path))      # True
print(os.path.isfile(path))     # True
print(os.path.isdir(path))      # False
print(os.path.realpath(path))   # D:\work\demo2.txt
print(os.path.samefile(path, path))  # True
print(os.path.split(path))        # ('D:\\work', 'demo2.txt')
print(os.path.splitdrive(path))   # ('D:', '\\work\\demo2.txt')
print(os.path.splitext(path))     # ('D:\\work\\demo2', '.txt')
print(os.path.join('D:\\','work','demo2.txt'))   # content/drive/test.txt

'''
os.system(命令) 的效果等同於在電腦的終端機或 cmd 裡，輸入並執行系統命令，但由於作業系統的不同，命令也會有所不同，
下方列出一些 Windows 和 Linux 裡常用的指令：

Windows:
指令	說明
cd	切換資料夾位置
cls	清除螢幕
md/mkdir	建立資料夾
rd/rmdir	刪除資料夾
ren/rename	重新命名
dir	列出目錄與子目錄
del/erase	刪除一個或多個檔案
move	移動檔案
copy	複製檔案
xcopy	複製檔案與樹狀目錄

Linux:
指令	說明
cd	切換資料夾位置
pwd	顯示所在目錄
ls	列出檔案清單
clear	清除螢幕
mkdir	建立資料夾
rm	刪除檔案或資料夾
mv	移動/重新命名檔案
cp	複製檔案
'''
'''import os
os.system("mkdir test")          #建立資料夾
os.system("cp test.txt ./demo")  # 複製至 demo 資料夾裡 ( Windows 使用 copy )
os.system("rm test.txt/")        # 刪除檔案 ( Windows 使用 del )
os.system("open test.txt")       # 使用預設轉體開啟 test.txt'''