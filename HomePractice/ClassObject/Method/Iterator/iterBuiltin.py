'''
Python Iterator 的定義為：符合 Python 中的 Iterator Protocol,
或是一個有 __iter__() 和 __next__() methods 的 object。
'''
#ex1
print('=====ex1=====')

vowels = ['a', 'e', 'i', 'o', 'u']
print(hasattr(vowels, '__iter__')) #True
print(hasattr(vowels, '__next__')) #False

# 可以用 iter() 來宣告 iterator object
vowels_iter = iter(vowels)
print(hasattr(vowels_iter, '__iter__')) #True
print(hasattr(vowels_iter, '__next__')) #True

#ex2
print('=====ex2=====')
'''

'''
class Interrogator():
    def __init__(self,questions):
        self.questions=questions

    def __iter__(self):
        return self.questions.__iter__()
    
questions=['Q1 ?','Q2 ?','Q3 ?','Q4 ?']
onePerson=Interrogator(questions)

for question in onePerson:
    print(question)
