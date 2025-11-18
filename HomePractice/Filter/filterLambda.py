# 語法與map一樣，filter(欲執行的function名稱, 可迭代物件的名稱)
# 同map，filter回傳一個生成器物件，可以將它轉換成list

names=['Karen','Jim','Kim']
lst1=list(filter(lambda name:len(name)==3,names))

nums=list(range(1000))
filtered=filter(lambda x:x%3==0 or x%7==0,nums)
sumOfFilter=sum(filtered)

print(lst1)
print(sumOfFilter)