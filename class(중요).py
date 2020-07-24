# 마린 
# name="마린"
# hp=40
# damage=5
# print("{0}유닛이 생성되었습니다".format(name))
# print("체력 {0},공격력{1}\n".format(hp,damage))

# tank_name="탱크"
# tank_hp=150
# tank_damage=35
# print("{0}유닛이 생성되었습니다".format(tank_name))
# print("체력 {0},공격력{1}\n".format(tank_hp,tank_damage))

# def attack(name,location,damage):
#     print("{0}:{1} 방향으로 적군을 공격합니다 [공격력{2}]".format(name,location,damage))

# attack(name,"1시",damage)
# attack(tank_name,"1시",tank_damage)
#일반 유닛(부모클래스)
class Unit:
    def __init__(self,name,hp):#__init__:생성자 
        self.name=name#맴버변수:클래스내에서 만들어진 변수
        self.hp=hp

#공격유닛 (자식클래스) 다중상속: 부모클래스가 2이상 즉,여러곧에서 상속을 받아야함
class AttackUnit(Unit):#파이썬은 상속받기위해서는 extends대신 클래스명(상속받을 클래스명표기)
    def __init__(self,name,hp,damage):
        Unit.__init__(self,name,hp)#상속받기위해서는 Unit.__init__()형태로사용 클래스 유닛에서 생성자에있는 내용을 사용하겠다는 의미
        self.damage=damage

    def attack(self,location):
        # 함수와 메소드의차이는 함수는 독립적으로 사용이가능하지만 메소드는 항상 클래스내부에서 사용해야한다
        # #클래스안의 메소드에서는 self를앞에 적어야함
        print("{0}:{1} 방향으로 적군을 공격 합니다.[공격력{2}]".format(self.name,location,self.damage))
        #self를 사용하면 클래스내부의(멤버변수)값을 사용하는것이고 self를사용하지않으면 class외부의(전달받은)값을 받아서 사용한다

    def damaged(self,damage):
        print("{0}:{1}데미지를 입었습니다".format(self.name,damage))
        self.hp-=damage
        print("{0}:현재 체력은 {1}압나다".format(self.name,self.hp))
        if self.hp<=0:
            print("{0}:파괴되었습니다".format(self.name))
# 날수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self,flying_speed):#self덕분에 함수호출시 self에 자동으로 호출한 객체가 전달된다
        self.flying_speed=flying_speed

    def fly(self,name,location):
        print("{0}:{1}방향으로 날아갑니다[속도{2}]".format(name,location,self.flying_speed))
#공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit,Flyable):
    def __init__(self,name,hp,damage,flying_speed):
        AttackUnit.__init__(self,name,hp,damage)#AttackUnit초기화작업(멤버변수초기화) 상속을 받아온 부모클래스의 멤버변수를 초기화시키기위해 사용
        Flyable.__init__(self,flying_speed)#Flyable초기화작업(멤버변수초기화)
# 발키리
valkyrie=FlyableAttackUnit("발키리",200,6,5)
valkyrie.fly(valkyrie.name,"3시")



#파이어뱃
# firebat1=AttackUnit("firebat",50,16)
# firebat1.attack("5시")
# firebat1.damaged(25)
# firebat1.damaged(25)

#마린
# marine1=Unit("마린",40,5)
# marine2=Unit("마린",40,5)

#탱크
# tank=Unit("탱크",150,35)

#레이스
# wraith1 =Unit("레이스",80,5)
# print("유닛이름:{0},공격력:{1}".format(wraith1.name,wraith1.damge))#맴버변수를 외부에서 사용할수있다

#클로킹기능이 업그레이드된 레이스
# wraith2 =Unit("레이스",80,5)
# wraith2.clocking=True
# #파이썬은 객체에  변수를 추가로 외부에서 만들어서 사용이가능함
# if wraith2.clocking==True:
#     print("{0}는 현재 클로킹 상태입니다".format(wraith2.name))

