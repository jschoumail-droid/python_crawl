import datetime

def currentDayTime():
    today=datetime.date.today()
    currentTime=datetime.datetime.now().time()
    if __name__ == '__main__':
        print(datetime.date.today())
        print(datetime.datetime.now().time())
        print('now():',datetime.datetime.now())
    
    return today,currentTime

if __name__ =='__main__':
    day,time=currentDayTime()
    print('currentDayTime :',day,time)