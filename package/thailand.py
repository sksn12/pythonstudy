class ThailandPackage:
    def detail(self):
        print("[태국 패키지 3박5일]방콬,파타야 여행 (야시장 투어) 50만원")

if __name__ =="__main__":#thailand.py에서 직접 실행하면 if문동작
    print("Thailand 모둘을 직접 실행")
    print("이 문장은 모듈을 직접 실행할 때만 실행돼요")
    trip_to=ThailandPackage()
    trip_to.detail()
else: # 외부 즉 다른 패키지나파일에서 thailand.py를 쓰면 else문이 동작
    print("Thailand 외부에서 모듈 호출")