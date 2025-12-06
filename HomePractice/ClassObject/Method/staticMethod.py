'''
Python類別中有@staticmethod裝飾詞(Decorator)的方法(Method),
  可以接受任意的參數,也因為它沒有self及cls參數,所以靜態方法
  (Static Method)無法改變類別(Class)及物件(Object)的狀態，

Static Method 不論透過類別(Class)或物件(Object)皆可呼叫,
Python編譯器於執行期間(Runtime)不會傳入self及cls參數
至靜態方法(Static Method)。
使用靜態方法(Static Method)有幾個優點是，在開發過程中可以
避免新加入的開發人員意外改變類別(Class)或物件(Object)的狀態
(因為方法中無self及cls參數)，而影響到類別(Class)原始的設計。
其二則是靜態方法(Static Method)在類別中是獨立的，所以有助於
單元的測試。
'''

#靜態方法類似於實例方法，不同之處在於
#  實例方法的第一個位置引數self傳遞的是物件實例，靜態方法不會傳遞位置引數self。
#  與類別方法一樣，可以使用修飾器(@staticmethod)宣告靜態方法。
import datetime

class Diary():
    def __init__(self,birthday,christmas):
        self.birthday=birthday
        self.christmas=christmas

    @staticmethod
    def formatDate(date):
        return date.strftime('%d-%b-%y')

    def showBirthday(self):
        return self.formatDate(self.birthday)
    def showChristmas(self):
        return self.formatDate(self.christmas)
    
myDiary=Diary(datetime.date(2025,5,14),datetime.date(2025,12,25))
print('birthday: ',myDiary.showBirthday())
print('christmas day: ',myDiary.showChristmas())