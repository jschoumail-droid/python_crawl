'''
any 參數接收一個迭代器,只要迭代器有任何一個元素的值為True,
那麼any函數的值就為True,否則為False。
注意若參數本身為空列表any的值則為False
'''
print(any([2>5,5>0,0>2]))
print(any([-1,0,[]])) #數字0才會被視為False，-1是非0數字，視為True
print(any([]))