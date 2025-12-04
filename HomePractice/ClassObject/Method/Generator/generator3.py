'''
yield 是Python 的一個關鍵字，用於建立一個生成器，而不是一次性回傳所有值，
  而是以惰性求值的方式逐步生成值。 當函式中使用 yield 時，它會暫停執行並
  回傳一個值，並記住目前狀態。 下一次呼叫時，會從上次暫停的地方繼續執行，
  直到遇到下一個 yield。 
yield 的特點與優勢
  記憶體效率高： 不會一次性將所有資料載入記憶體，特別適合處理大量資料，
  例如影像、大型檔案或資料串流。 
延遲執行： 函式在被呼叫時不會立即執行，而是回傳一個生成器物件。 只有在遍歷
  生成器時，程式碼才會開始執行。 
保持狀態： 每次 yield 回傳值後，函式會暫停執行並保存所有局部變數的狀態，
  確保下次呼叫時能從中斷點繼續執行。 
替代 return: return 會中斷函式的執行，而 yield 則允許函式暫停並在之後繼續執行。 
yield 的使用情境
  處理大型資料集： 例如，當你需要處理成千上萬張圖片時，使用 yield 可以逐張載入
  並處理，而不需要一次將所有圖片讀入記憶體。
建立無限序列： 生成器可以被設計成產生無限序列，因為它只在需要時才產生下一個值。
管道(Pipeline)設計： yield 非常適合用於建立資料處理的管道，其中一個生成器的
  輸出可以作為另一個生成器的輸入，實現資料的逐步處理和傳遞。 
'''

print('=====ex1=====')
def simple_generator():
    print('Step 1')
    yield 1
    print('Step 2')
    yield 2
    print('Step 3')
    yield 3

# 呼叫函式不會執行，而是回傳一個生成器物件
my_gen = simple_generator()
print(type(my_gen))

# 第一次呼叫 next()，執行到第一個 yield
print(next(my_gen))

# 第二次呼叫 next()，從上次暫停的地方繼續執行
print(next(my_gen))

# 也可以用 for 迴圈遍歷生成器
print('my_gen---')
for value in my_gen:
    print(value)
print('my_gen1---')
my_gen1 = simple_generator()
for value in my_gen1:
    print(value)

# 當生成器用盡時，會引發 StopIteration 錯誤
# print(next(my_gen))