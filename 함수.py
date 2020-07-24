def open_account():
    print("새로운 계좌가 생성되었습니다.")
open_account()

#전달값과 반환값 
def deposit(blance,money):
    print("입금이 완료 되었습니다")
    print("잔액은 {0}원입니다".format(blance+money))
    return blance+money

def withdraw(blance,money):
    if blance>=money:
        print("{0}출금하였습니다".format(money))
        print("남은 금액은 {0}입니다".format(blance-money))
        return blance-money
    elif blance<=money:
        print("계좌에 금액이 부족합니다")

def withdraw_night(blance,money):
    commison =100
    return commison,blance-money-commison

blance=0#잔액
blance =deposit(blance,1000)#함수를 호출하고 호출뒤에 남은 잔액을 blance에 저장하기위해 사용
blance=withdraw(blance,200)
commison,blance=withdraw_night(blance,500)
print("수수료 {0}원이며,잔액은{1}원입니다".format(commison,blance))










