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