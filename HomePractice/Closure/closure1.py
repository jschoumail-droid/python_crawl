'''
閉包，從字面的意思翻譯就是一個「封閉的包裹」，
在包裹外的人，無法拿到包裹裡的東西，如果你在包裹裡，
就能盡情取用包裹內的東西，閉包可以保存在函式作用範圍內的狀態，
不會受到其他函式的影響，且無法從其他函式取得閉包內的資料，
也可避免建立許多全域變數互相干擾。

閉包的定義：

A 函式中定義了 B 函式。
B 函式使用了 A 函式的變數。
A 函式回傳了 B 函式。
'''

#ex1
print('=====ex1=====')
def a(msg):
    i = '!!!'         # ------------------------ 閉包開始
    def b():          # A 函式內定義了 B 函式
        print(msg + i)  # B 函式使用了 A 函式的變數
    return b          # 將 B 函式當作回傳值 ------- 閉包結束
s = a('hello')                   
#呼叫變數s所指向的閉包B函式，此時B函式記住了
#'hello'(來自A函式的msg)和'!!!'(來自A函式的i )，
#因此輸出'hello!!!'
s()
s=a('World')
s()
a('bye')

'''
作用域 Scope 指的是變數、常數、函式或其他定義語句可以「被存取得到」
的範圍,Python 總共定義了四種作用域,從內而外分別是Local(區域 )、
Enclosing(閉包外函式)、Global(全域)和Built-in(內置預設),
內部的作用域無法影響到外部作用域。
'''

#ex2
print('=====ex2=====')
'''
下方的程式碼，會建立一個 avg 函式的閉包，執行後雖然 test() 執行了三次，
但因為每次執行時保留下一個作用域的繫結關係，所以會不斷將傳入的數值進行計算，
最後就會得到 11 的結果。
'''
def count():                # 建立一個 count 函式
    a = []                    # 函式內有區域變數 a 是串列
    def avg(val):             # 建立內置函式 avg ( 閉包 )
        a.append(val)           # 將參數數值加入變數 a
        print(a)                # 印出 a
        return sum(a)/len(a)    # 回傳 a 串列所有數值的平均
    return avg                # 回傳 avg

test = count()
test(10)      # 將 10 存入 a
test(11)      # 將 11 存入 a
test(12)      # 印出 11
print(test(13))

'''
Functions in Python
1. 普通函式 (Regular Functions)
  這是 Python 中最基本的函式形式，接收參數並返回值。
'''
print('=====ex3.1=====')
def hello(name):
    return f"Hello, {name}!"
print(hello("Yusinz"))  # Output: Hello, Yusinz!

'''
2. 函式作為變數被傳遞 (First-Class Functions)
  函式在 python中是一級公民,也被稱為 First-class function,
  它可以做為變數去傳遞，甚至作為其他函式的參數或返回值。
'''
print('=====ex3.2=====')
def hello(name):
    return (f"Hello, {name}!")

say_hi = hello
print(say_hi("Yusinz"))  # # Output: Hello, Yusinz!

'''
3. 函式可以作為參數 (Function as Arguments)
  函式可以被傳遞給另一個函式，這也是 closure 和 decorator 可以實現的重要概念。
'''
print('=====ex3.3=====')
def call_func(func):
    return func("Yusinz")

def hello(name):
    return (f"Hello, {name}!")

print(call_func(hello))  # Output: Hello, Yusinz!

'''
4. 函式可以返回函式 (Function Returning Functions)
一個函式可以返回另一個函式。而外部函式返回內部函式正是閉包的核心。
'''
print('=====ex3.4=====')
def outer_function():
    def inner_function():
        return "Hello!, Yusinz!"
    return inner_function

hello = outer_function()
print(hello())  # Output: Hello, Yusinz!

'''
5. 作用域和變數的可見性 (Scope and Variable Visibility)
區域變數或是全域變數大家應該耳熟能詳，就不多作介紹。

enclosing Scope
  作用域:在函式內部的函式中。
  可見性：內部函式可以訪問外部函式的變數。

Built-in Scope
  作用域:Python 的內建名稱和函式，如 print()、len() 等。
  可見性：在整個 Module 中都可見，即使在其他作用域內部也可以訪問。
'''
print('=====ex3.5=====')
global_name = "Global Yusinz"

def hello():
    enclosing_name = "Enclosing Yusinz"
    def say_hello():
        local_name = "Local Yusinz" 
        print(f"Hello {global_name}!") #Output: Hello Global Yusinz!
        print(f"Hello {enclosing_name}!") #Output: Hello Local Yusinz!
        print(f"Hello {local_name}!") #Output: Hello Enclosing Yusinz!
    say_hello()

hello()

'''
閉包(closure)是指當外層的函式把一個內層的函式返回時，它會「記住」它所在的外層函式的變數，
即使外層函式已經執行完畢。這讓內層函式能在外層函式結束後，繼續使用外部函式中的變數。

外層函式 (outer_function) 宣告了 name = "Yusinz"
內層函式 (inner_function) 被宣告在外層函式裡面，並使用了外層函式的變數 name。

當我們 call closure_example() 時,outer_function 會返回 inner_function,
  照理來說我們返回的 inner_function 裡面的 name 在執行完 outer_function
  後生命週期就結束，我們單純要 closure_example() 去 call inner_function()
  他應該讀不到外層的 name 才對，但實際執行後會發現，他還是可以印出 Hello, Yusinz!
  這是因為返回的 inner_function 是一個 closure,它可以記憶住 name 的值。
  所以就算 outer_function 已經執行完畢了,closure 仍然可以使用 name。

這個被記憶住的變數 name,我們可以叫他 captured variable,使用 captured variable
  的函式 inner_function 和 closure_example 就是 closure。
'''
print('=====ex3.6=====')
def outer_function():
    name = "Yusinz"
    def inner_function():
        print(f"Hello, {name}!")
    return inner_function

closure_example = outer_function()
closure_example()  # Output: Hello, Yusinz!

'''
captured variable 在使用時，如果需要賦值，會出現 UnboundLocalError,
這是因為賦值之後 captured variable 會被轉換為區域變數，這時候它就會拿不到
外層函式的變數。但要解決也很簡單使用 nonlocal 宣告變數後就能對它做操作了。
'''
print('=====ex3.7=====')
def create_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

counter = create_counter()
print(counter())  # Output: 1
print(counter())  # Output: 2

'''
closure 可以很多個嗎?
答案是可以，每個 closure 都是獨立的，以 counter 為例，可以看到 second_counter() 的值還會是 1。
'''
print('=====ex3.8=====')

counter = create_counter()
second_counter = create_counter()
print(counter())  # Output: 1
print(counter())  # Output: 2
print(counter())  # Output: 3
print(second_counter())  # Output: 1