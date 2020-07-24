#메소드 오버라이딩(자식클래스에서 정의한 메소드를 사용하고싶을때 메소드를 새롭게 정의해서 사용하는방법을 메소드 오버라이딩이라한다)
from random import *
#일반유닛 
class Unit:   #파이썬에서 생성자는 선언을해주지않아도 자동으로 만들어지지만 객체의 생성과 초기값을 주기위해서는 생성사를 선언해주어야한다
    def __init__(self,name,hp,speed):#__init__:생성자에서 멤버변수를 생성시켜준다 객체의 *초기화*담당
        self.name=name
        self.hp=hp
        self.speed=speed
        print("{0} 유닛이 생성되었습니다".format(name))#여기서 self.name을쓰던 name을쓰던 상관없음 왜냐하면 파라미터로받은 name값과 매개변수로받은 name값이 둘다있어서

    def move(self,location):
        print("[지상 유닛 이동]")
        print("{0}:{1} 방향으로 이동합니다 . [속도{2}]".format(self.name,location,self.speed))

    def damaged(self,damage):
        print("{0}:{1}데미지를 입었습니다".format(self.name,damage))
        self.hp-=damage
        print("{0}:현재 체력은 {1}압나다".format(self.name,self.hp))
        if self.hp<=0:
            print("{0}:파괴되었습니다".format(self.name))

# 공격 유닛
class AttackUnit(Unit):#파이썬은 상속받기위해서는 extends대신 클래스명(상속받을 클래스명표기)
    def __init__(self,name,hp,speed,damage):#Unit.__init__(self,name,hp,speed)클래스 Unit에서 __init__부분에 값들을 넘겨준다는 의미
        Unit.__init__(self,name,hp,speed)#상속받기위해서는 Unit.__init__()형태로사용 클래스 유닛에서 생성자에있는 내용을 사용하겠다는 의미
        self.damage=damage

    def attack(self,location):
        # 함수와 메소드의 차이는 함수는 독립적으로 사용이가능하지만 메소드는 항상 클래스내부에서 사용해야한다
        # #클래스안의 메소드에서는 self를앞에 적어야함
        print("{0}:{1} 방향으로 적군을 공격 합니다.[공격력{2}]".format(self.name,location,self.damage))
        #self를 사용하면 클래스내부의(멤버변수)값을 사용하는것이고 self를사용하지않으면 class외부의(전달받은)값을 받아서 사용한다

# 마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self,"마린",40,1,5)

    # 스팀팩 
    def stimpack(self):
        if self.hp>10:
            self.hp-=10
            print("{0} : 스팀팩을 사용합니다(hp 10감소)".format(self.name))
        else :
            print("{0} : 체력이 10이하여서 스팀팩을 사용할수없습니다".format(self.name))


# 탱크
class Tank(AttackUnit):
    seize_developed=False #시즈모드 개발여부
    def __init__(self):
        AttackUnit.__init__(self,"탱크",150,1,35)
        self.seize_mode=False
    def set_seize_mode(self):
        if Tank.seize_developed==False:
            return
        #현재 시즈모드가 아닐 때->시즈모드
        if  self.seize_mode ==False:
            print("{0} : 시즈모드로 전환합니다".format(self.name))
            self.damage *=2
            self.seize_mode=True
        #현재 시즈모드 일 때->시즈모드 해제
        else:
            print("{0} : 시즈모드를 해제 전환합니다".format(self.name))
            self.damage /=2
            self.seize_mode=False


# 날수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self,flying_speed):#self덕분에 함수호출시 self에 자동으로 호출한 객체가 전달된다
        self.flying_speed=flying_speed

    def fly(self,name,location):
        print("{0}:{1}방향으로 날아갑니다[속도{2}]".format(name,location,self.flying_speed))

#공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit,Flyable):
    def __init__(self,name,hp,damage,flying_speed):
        AttackUnit.__init__(self,name,hp,0,damage)#AttackUnit초기화작업(멤버변수초기화) 상속을 받아온 부모클래스의 멤버변수를 초기화시키기위해 사용
        Flyable.__init__(self,flying_speed)
    def move(self,location):#move함수 재정의 (메소드 오버라이딩)기존에있던 메소드를 또 재정의해서사용 (상속을받아 부모 클래스에있던 메소드를 재정의)
        print("[공중 유닛 이동]")
        self.fly(self.name,location)

class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self,"레이스",80,20,5)
        self.clocked=False #클로킹 모드 (해제 상태)
    def clocking(self):
        if self.clocked ==True:
            print("{0} : 클로킹 모드 해제합니다.".format(self.name))
            self.clocked=False
        else:
            print("{0} : 클로킹 모드 설정합니다.".format(self.name))
            self.clocked=True

def game_start():
    print("[알림] 새로운 게임을 시작합니다")
#pass의 또 다른사용 예제
def game_over():
    print("Player: gg")
    print("[Player]님이 게임에서 퇴정하셨습니다")
   

# 실제 게임 진행
game_start()

#마린 3기 생성
m1 =Marine()
m2 =Marine()
m3 =Marine()

#탱크 2기생성
t1=Tank()
t2=Tank()

#레이스 1기생성
w1=Wraith()

#유닛 일괄 정리(생성된 모든 유닛 append)
attack_unit=[]
attack_unit.append(m1)
attack_unit.append(m2)
attack_unit.append(m3)
attack_unit.append(t1)
attack_unit.append(t2)
attack_unit.append(w1)
 
#전군 이동
for unit in attack_unit:
    unit.move("1시")

# 탱크 시즈모드 개발
Tank.seize_developed=True
print("[알림] 탱크 시즈모드 개발이 완료되었습니다")

# 공격 모드 준비 (마린 : 스팀팩,탱크: 시즈모드, 레이스 : 클로킹)
for unit in attack_unit:
    if isinstance(unit,Marine):#isinstance지금만들어진 객체가 어떤클래스의 인스턴스인지확인,즉 현재의 유닛이라는 객체가 마린이라는 클래스의 인스턴스이면 스팀팩사용 
        unit.stimpack()
    elif isinstance(unit,Tank):
        unit.set_seize_mode()
    elif isinstance(unit,Wraith):
        unit.clocking()
# 전군 공격
for unit in attack_unit:
    unit.attack("1시")

# 전군 피해
for unit in attack_unit:
    unit.damaged(randint(5,21))# 공격은 랜덤으로 5~20받음

# 게임 종료
game_over()
# 벌처 
# vulture=AttackUnit("벌처",80,10,20)
#사용할 클래스명과 매개변수값을 vulture에 넣어주고 그 vulture를통하여 밑에서 처럼 사용할 메소드값을 불러와준다
#배틀크루저
# battlecruiser=FlyableAttackUnit("배틀크루저",500,25,3)

#지상유닛일 경우는 move함수를 사용하고 공중유닛일경우에는 매번 fly함수를 써야하니깐 구분하기 귀찮아서 메소드오바리이딩을 통해move함수만 사용해도 
#공중유닛이건 지상유닛이건 이동할수있게 만들어준다
# vulture.move("11시")
# battlecruiser.move("9시")