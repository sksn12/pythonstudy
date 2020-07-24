# 줄바꿈\n
print("백문이 불여일견 \n백견이 불여일타")

# \" \' : 문장 내에서 따옴표
#저는 "나도코딩"입니다
print('저는 "나도코딩"입니다')
print("저는 \"나도코딩\"입니다")

# \\:문장내에서\
print("C:\\Users\\youngman\\Desktop\\프로그래밍\\파이썬스터디2>")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine") #PineApple

#\b : 백스페이스 (한 글자 삭제)
print("Redd\bApple")

# \t : 탭 (들여쓰기)
print("Red\tApple")

#퀴즈 
# 예)http://naver.com
# 규칙 1 : http://부분 제외 =>naver.com
# 규칙 2 : 처음 만나는 점(.) 이후 부분은 제외 =>naver
# 규칙 3 : 남은 글자 중 처음  세자리+ 글자 갯수 +글자 내 'e'갯수 +"!"로 구성
#                 (nav)                (5)             (1)         (!)
# 예 ) 생성된 비밀번호 :nav51!
    
# 내가만든코드 (규칙1,규칙2를 무시햇음)
site="http://naver.com"
naver="naver"
print("생성된 비밀번호는"+str(site[7:10])+str(len(naver))+str(naver.count("e"))+"!입니다")

#답지
url="http://naver.com"
my_str=url.replace("http://","")#규칙1
my_str=my_str[:my_str.index(".")]#규칙2
password=my_str[:3]+str(len(my_str))+str(my_str.count("e"))+"!"
print("{0}의 비밀번호는{1}".format(url,password))

