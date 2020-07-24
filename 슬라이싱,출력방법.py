sentence='나는 소년입니다'
sentence2="나는 소년입니다"
print(sentence)
print(sentence2)
sentence3="""
나는 소년이고 
파이썬은 쉬워용
"""
print(sentence3)

#슬라이싱
jumin="090901-2313672"
print("성별:"+jumin[7])
print("연"+jumin[0:2])#0~2직전까지 즉 0,1
print("월"+jumin[2:4])
print("일"+jumin[4:6])
print("생년월일"+jumin[:6])#처음부터 6직전까지
print("뒤 7자리"+jumin[7:])#7부터 끝까지
print("뒤 7자리 뒤에서부터"+jumin[-7:])#맨뒤에서 7번째부터 끝까지

python="Python is Amazing"
print(python.lower())#소문자로 출력
print(python.upper())#대문자로 출력
print(python[0].isupper())#0번째에있는것이 대문자냐
print(len(python))
print(python.replace("Python","java"))#Python을 java로 바꾸어서 출력
index=python.index("n")#n의위치를 index변수에 저장
print(index)
index=python.index("n",index+1)#두번째n의위치를 저장시켜줌
print(index)
print(python.find("n"))#index는 찾고자하는 것이 없으면 에러 find는 찾고자 하는것이 없으면-1
print(python.count("n"))#n이 몇개들어있는지

#문자열 사용
print("a"+"b")
print("a","b")

#방법1
print("나는 %d살입니다" %20)
print("나는 %s를 좋아해요" % "파이썬")
#%d는 %s로 대체가능
print("Apple은 %c로 시작해여" %"a")
print("나는 %s색과 %s색을 좋아해요" %("파란","빨간"))

#방법2
print("나는{}살입니다" .format(20))
print("나는 {}색과 {}색을 좋아해요".format("파란","빨간"))
print("나는 {0}색과 {1}색을 좋아해요".format("파란","빨간"))
print("나는 {1}색과 {0}색을 좋아해요".format("파란","빨간"))#{}안에 숫자를 넣게되면format에있는 값들의 순서로받아옴

#방법3
print("나는 {age}살이며,{color}색을 좋아해요".format(age=20,color="빨간"))

#방법4 (v3.6이상)
age=20
color="빨간"
print(f"나는 {age}살이며,{color}색을 좋아해요")