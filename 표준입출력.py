# print("python","java",sep="!",end="?")#sep를 사용하면 python과 java사의에 어떠한 값이 들어갈지 를 정해줌
# print("무엇이 더 재밌을까요?")

# import sys
# print("Python","java",file=sys.stdout)#stdout표준입력처리
# print("Python","java",file=sys.stderr)#stderr표준에러처리(

# socres={"수학":0,"영어":50,"코딩":100}
# for subject,socre in socres.items():
#     print(subject.ljust(8),str(socre).rjust(4),sep=":")#ljust(8)subject왼쪽으로 8칸뛰고 정렬

#은행 대기 순번표
#001,002,003,...
# for num in range(1,20):
#     print("대기번호 :"+str(num).zfill(3))#zfill앞에0을 채워줌

answer=input("아무 값이나 입력하세요 : ")
print("입력하신값은 :",answer,"입니다")