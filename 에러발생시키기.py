#파이썬에서 제공하는 에러말고 에러를 정의해주는함수
class BigNumberError(Exception):
    def __init__(self,msg):
        self.msg=msg
    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기입니다")
    num1=int(input("첫 번째 숫자를 입력하세요"))
    num2=int(input("두 번째 숫자를 입력하세요"))
    if num1 >= 10 or num2>=10:
        raise BigNumberError("입력값 : {0},{1}".format(num1,num2)) #error발생시에 input으로 받은값들을BigNumberError클래스의
    #"입력값 : {0},{1}".format(num1,num2)"이 하나의 msg가되서 메소드의 인자값으로 들어간다
    print("{0}/{1}={2}".format(num1,num2,int(num1/num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다 한 자릿수만 입력하세요")
except BigNumberError as err:
    print("에러가 발생하였습니다 한 자리 숫자만 입력하세요")
    print(err)
finally:#try문의 마지막에 위치하며 에러가 발생하던 에러가 발생하지않던 무조건적으로 출력된다
    print("계산기를 이용해 주셔서 감사합니다")