class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit,Flyable):
    def __init__(self):
        super().__init__()
# super는 부모 클래스에서 사용된 함수의 코드를 가져다가 자식 클래스 함수에서 사용할때 사용
# 문제점은 class가 다중상속을 받을시에 super를 사용하게되면 맨처음에 있는 값만 super가 불러옴


#드랍쉽
dropship =FlyableUnit()