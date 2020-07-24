try:
    print("나누기 전용 계산기입니다")
    nums=[]
    nums.append(int(input("첫 번째 숫자를 입력하세요")))
    nums.append(int(input("두 번째 숫자를 입력하세요")))
    nums.append(int(nums[0]/nums[1]))
    print("{0}/{1}={2}".format(nums[0],nums[1],nums[2]))
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다")
except ZeroDivisionError as err: #나누기숫자에 0을넣었을때 발생하는 에러
    print(err) # err을 적으면 발생하는 에러를 고대로 표시 
except: #Exception as err:#try문에서 에러가 발생했을때 우리가 설정해준 ValueError나ZeroDivisionError를 제외하고 나머지 모든에러가 발생할시 except구문 발생
    print("알 수 없는 에러가 발생하였습니다")
    print(err)