
#ex1
import sys

squares = []
for arg in sys.argv[1:]:
    squares.append(int(arg) ** 2)
print(squares)

#ex2(與ex3結果相同)
'''
>python odds.py 11 8 9 5 4 6 3 2
['11', '9', '5', '3']
'''
import sys

odds = []
for arg in sys.argv[1:]:
    if int(arg) % 2:
        odds.append(arg)
print(odds)

#ex3(與ex2結果相同)
import sys

odds = [arg for arg in sys.argv[1:] if int(arg) % 2]
print(odds)