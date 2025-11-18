#ex1
print('=====ex1=====')
'''
鍵值不可重複,所以只有一個Terry鍵值
'''
names=['Graham','John','Terry','Eric','Terry']
print({k:len(k) for k in names})

#ex2
print('=====ex2=====')
'''
建立一個學生成績單
'''
names=['Vivian','Racheal','Tom','Adrian']
scores=[70,82,80,79]
transcrip={names[i]:scores[i] for i in range(4)}
print(transcrip)