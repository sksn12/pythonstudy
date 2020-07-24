print(1+1)
print(6/3)#2 
print(5/3) #1.66666666667
print(2**3)#2^3=8
print(5%3)#2
print(10%2)
print(5//3)#나머지가 있을때에 몫만 출력해줌

print(10>3) #True
print(4>=7) #False
print(10<3) #False
print(3==3) #True
print(3+4==7) #True

print(1 != 3) #True
print(not(1!=3))#False
#앤드
print((3>0)and (3<5)) #True
print((3>0)&(3<5))#True
#오알
print((3>0) or (3<0)) # True
print((3>0) | (3<0))# True

print(5>4>3) #True
print(5>4>7) #False

#연산자
print(abs(-5))#5 절대값 연산자
print(pow(4,2))#4^2=16
print(max(5,12))# 12
print(min(3,29))#5
print(round(3.14))#3
print(round(4.6))#5 반올림

from math import*
print(floor(4.99))#4 내림
print(ceil(3.14))#4 올림
print(sqrt(16))#4 제곱근 이세가지는 위에 함수를 임포트해야 사용가능

#랜덤함수
from random import*
print(random())#0.0~1.0미만의 임의의 값 생성
print(random()*10)#0.0~10.0미만의 임의의 값 생성
print(int(random()*10))#0~10미만의 임의의 값 생성

#로또함수
print(int(random()*45)+1)#1~45이하의 임의의 값 생성
print(randrange(1,46))#1~46미만의 임의의 값 생성
print(randint(1,45))#1~45이하의 임의의 값 생성

#퀴즈
from random import*
print("오프라인 스터디 모임 날짜는 매월"+str(randint(4,28))+"일로 선정되었습니다")

