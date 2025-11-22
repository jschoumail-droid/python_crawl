
import random

def playGame():
    print("======猜數字遊戲=======\n")
    min=1
    max=100
    count=0
    target=random.randint(min,max)
    print(target)
    while True:
        count+=1
        keyin=int(input(f"請輸入數字，範圍{min}~{max}:"))
        if min<=keyin<=max:
            if keyin==target:
                print(f"第{count}次猜對了,target:{target}")
                break
            elif keyin<target:
                min=keyin+1
                print("大一點")
            elif keyin>target:
                max=keyin-1
                print("小一點")
            else:
                print(f"已猜了{count}次")
        else:
            print("請輸入指示範圍數字")
        print(f"猜了{count}次")

def main():
    while True:
        playGame()
        cont=input("繼續嗎?y/n")
        if cont=='n':
            print("結束")
            break

if __name__=="__main__":
    main()