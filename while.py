customer ="토르"
index=5
while index >=1:
    print("{0},커피가 준비 되었습니다.{1}번 남았어요".format(customer,index))
    index-=1
    if index==0:
        print("커피는 폐기처분되었습니다")
customer="토르"
preson="unknown"
while preson!=customer:
    print("{0},커피가 준비되었습니다".format(customer))
    preson=input("이름이 어떻게 되시나요")
    if preson=="토르":
        print("확인되었습니다")
    else:
        print("주문하신손님이 아니네요")

    