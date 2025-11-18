#ex1
print('=====ex1=====')
'''
比較list與set
'''
print([a+b for a in [0,1,2,3] for b in [4,3,2,1]])
print({a+b for a in [0,1,2,3] for b in [4,3,2,1]})

#ex2
print('=====ex2=====')
'''
集合(Set)Comprehension的用法和串列(List)Comprehension幾乎一樣,
不同的地方是集合(Set)使用 {} 符號，並且其中的元素不會重覆
'''
titles = "Learn Code With Mike"
result = {letter for letter in titles if letter == "e"}
print(result)  # 執行結果：{'e'}