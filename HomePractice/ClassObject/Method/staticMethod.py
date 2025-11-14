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