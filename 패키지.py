# import package.thailand #thailand부분은 모듈이나 패키지만 가능 클래스나 함수는 임포트를 직접할수없음
# #import package.thailand.ThailandPackage 이렇게는 사용이불가
# trip_to=package.thailand.ThailandPackage()
# trip_to.detail()


#이렇게 사용하면 패키지에 있는 모듈의 클래스를 바로 사용이가능함
# from package.thailand import ThailandPackage
# trip_to=ThailandPackage()
# trip_to.detail()

# from package import vietnam
# trip_to=vietnam.vietnamPackage()
# trip_to.detail()


from package import * #package패키지의 있는 모든값을 쓰겠다고 선언한건데 오류발생
# # why? : 개발자가 공개범위를 설정해줘야 사용이가능 package안에서 원하는것만 공개가능 
# trip_to = vietnam.vietnamPackage()
# trip_to.detail()

import inspect
import random 
print(inspect.getabsfile(random))#파일의 위치가 어디있는지를 알려줌
print(inspect.getabsfile(thailand))
