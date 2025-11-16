'''
class Product:
    def __init__(self, name:str, qty:int):
        self.name = name
        self.qty = qty

Python 3.7 新增的 dataclasses 功能以後，我們只需要寫成像下方的 code：

from dataclasses import dataclass
 
@dataclass
class Product:
    name: str
    qty: int
'''
#ex1
print("=====ex1=====")
import dataclasses

@dataclasses.dataclass
class Point:
    x: int
    y: int

p=Point(x=10,y=20)
print(p)
p2=Point(x=10,y=20)
print(p==p2)
print(dataclasses.asdict(p))

#ex2
#dataclasses 被創建時，__init__() 會呼叫 __post_init__ 方法，所以你可以利用 __post_init__ 來執行在創建時你想做的事情
#  amount: int = field(init=False) 代表著在 __init__ 時不需要輸入此屬性，他會在 __post_init__ 時創建
print("=====ex2=====")
from dataclasses import dataclass, field
 
@dataclass
class Product:
    name: str
    price: int
    qty: int
    amount: int = field(init=False)
 
    def __post_init__(self):
        self.amount = self.price * self.qty
 
 
itemA = Product(name="itemA", price=100, qty=10)
print(itemA)

#ex3
print("=====ex3=====")
'''
pandas.DataFrame 可以接收 dict-like container for Series objects，
所以使用上只需將 object 放在 list 裡面，然後再 df = pd.DataFrame(products)，
就可以搭配 pandas 使用
'''
from dataclasses import dataclass
import pandas as pd
 
@dataclass
class Product:
    name: str
    qty: int
 
products = []
for i in range(10):
    products.append(Product(name=i, qty=i*2))
 
df = pd.DataFrame(products)
print(products)
print(df)

#ex3
print("=====ex4=====")
'''
dataclasses 使用上就像一般的 class,所以我們也可以自己加上方法，像下面的例子，
我們增加了 revenue 的方法，可以快速計算出所購買的商品總數
'''
from dataclasses import dataclass
from typing import List
 
@dataclass
class Product:
    name: str
    qty: int
    price: int
 
@dataclass
class Purchase:
    products: List[Product]
 
    def revenue(self):
        total_revenue = 0
        for product in self.products:
            total_revenue += product.qty * product.price
        return total_revenue
 
user_A = Purchase(
    products=[
        Product(name="item1", qty=1, price=30),
        Product(name="item1", qty=2, price=20),
        Product(name="item1", qty=3, price=10),
    ]
)
 
print(user_A.revenue())

#ex3
print("=====ex5=====")
'''
在裝飾詞上加上 frozen=True,當屬性被建立之後，就會無法被修改，
變成 immutable dataclasses
'''
from dataclasses import dataclass
 
@dataclass(frozen=True)
class Product:
    name: str
    qty: int
    price: int
 
itemA = Product("itemA", 10, 100)
itemA.name = "itemB"
