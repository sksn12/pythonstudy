#모듈은 같은 파일에 존재해야 사용이 가능하다
# import 모듈
# 모듈.price(3) # 3명이서 영화보러갔을때 가격
# 모듈.price_morning(4)
# 모듈.price_soldier(2)

# import 모듈 as mv #모듈을 mv로 호출가능 모듈명이 길 경우 모듈명을 대체할 이름을 만들수있음
# mv.price(2)
# mv.price_morning(3)
# mv.price_soldier(4) 

# 이게 가장 편함
# from 모듈 import *
# price(3)
# price_morning(4)
# price_soldier(5)

from 모듈 import price,price_morning #어떤 함수만 가져다 쓸지 정할수있음
price_morning(2)
price(1)