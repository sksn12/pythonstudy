#커피숍
menu={"커피","우유","주스"}
print(menu,type(menu))

menu=list(menu)
print(menu,type(menu))

menu=tuple(menu)
print(menu,type(menu))

menu=set(menu)
print(menu,type(menu))

#퀴즈4
#치킨은 1,커피3
#조건1: 댓글은 20명이 작성했고 아이디는 1~20이라고 가정
#조건2: 댓글 내용과 상관없이 무작위로 추첨하되 중복 불가
#조건3:random 모듈의 shuffle과 sample을 활용
#내답
from random import*
lst=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
shuffle(lst)
print("치킨 당첨자 : "+str(sample(lst,1)))#lst에서 랜덤으로 1개를 뽑아라
print("커피 당첨자 : "+str(sample(lst,3)))

#답지
users=range(1,21)
users=list(users)
print(users)
shuffle(users)
print(users)

winners=sample(users,4)#4명중에서 1명은 치킨 3명은커피
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))

