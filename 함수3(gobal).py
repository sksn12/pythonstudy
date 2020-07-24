#지역변수 (함수내에서만 사용가능)
#전역변수 (모든 장소에서 사용가능,대신 함수내에서 사용시 함수내에서 초기화를 해줘야 사용가능 or global함수로 사용이 가능하게하거나)
# gun=10
# def checkpiont(soldiers):
#     gun=gun-soldiers
#     print("[함수내]남은 총 :{0}".format(gun))

# print("전체 총 :{0}".format(gun))
# checkpiont(2)
# print("남은 총 : {0}".format(gun))
#이함수는 함수내에서 지역변수가 초기화되지않아 오류가 발생해서 사용이 불가능
# gun=10
# def checkpiont(soldiers):
#     global gun #전역 공간에 있는 gun사용
#     gun=gun-soldiers
#     print("[함수내]남은 총 :{0}".format(gun))

# def checkpiont_ret(gun,solders):
#     gun=gun-solders
#     print("[함수내]남은 총 :{0}".format(gun))
#     return gun#return gun을 사용함으써 함수 밖에 있는 gun=checkpiont_ret(gun,2)의 gun값에  gun=gun-solders값이 들어갈수있음
#     #함수내의 있는 지역변수 gun을 반환함으로 함수밖에잇는 곳에서 사용이가능함

# print("전체 총 :{0}".format(gun))
# #checkpiont(2)
# gun=checkpiont_ret(gun,2)
# print("남은 총 : {0}".format(gun))
#가급적 전역변수사용은 별로 안좋음

#퀴즈
# def std_weight(height,gender):
#     x=height*0.01
#     if gender=="men":
#         wight=x*x*22
#         print("키 {0}남자의 표준 체중은 {1}입니다.".format(height,wight))
#     elif gender=="girl":
#         wight=x*x*21
#         print("키 {0}여자의 표준 체중은 {1}입니다.".format(height,wight))
        

# std_weight(175,"girl")

#답지
def std_weight(height,gender):
    if gender=="men":
        return height*height*22
    else:
        return height*height*21

height=175
gender="men"
weight=round(std_weight(height/100,gender),2)
print("키 {0}cm {1}의  표준 체중은 {2}입니다.".format(height,gender,weight))





