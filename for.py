for waiting_no in[0,1,2,3,4,]:  
    print("대기 번호 : {0}".format(waiting_no))
for waiting_no in range(5): # 0,1,2,3,4
    print("대기 번호 : {0}".format(waiting_no)) 
starbucks={"아이언맨","토르","그루트"}
for customer in starbucks:
    print("주문하신 손님은 : {0}".format(customer))
stundes =[1,2,3,4,5]
print(stundes)
stundes=[i+100 for i in stundes]
print(stundes)
students =["아이언맨","그루트","토르"]
print(students)
students=[len(i) for i in students ]#students에 있는 값들을 하나씩 확인하면서 그값들을 길이로 출력
print(students)

#퀴즈
from random import *
cnt=0
for customer in range(1,51):
    time=randrange(5,51)
    if time <=15:
        print("[o]{0}번째 손님 (소요시간 : {1}분)".format(customer,time))
        cnt+=1
    else :
        print("[]{0}번째 손님 (소요시간 : {1}분)".format(customer,time))
print("총 탑승인원은{0}입니다".format(cnt))


