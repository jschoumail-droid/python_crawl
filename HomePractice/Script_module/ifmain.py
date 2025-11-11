#if __name__ == '__main__': 應用
#當本程式檔案(script)被其它程式檔案(script)呼叫，不會執行print()那一行ststement
#但直接執行本程式檔案(script)時，則print()那一行ststement將會執行

def sum1To10():
    result=0
    for n in range(1,11):
        result+=n

    if __name__ == '__main__':
        print('result= ',result)

    return result

if __name__ == '__main__':
        print('sum1To10 =',sum1To10())