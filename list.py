#리스트[]
subway=[10,20,30]
print(subway)

#조새호가 몇 번째 칸에 타고 있는가?
subway=["유재석","조새호","박명수"]
print(subway.index("조새호"))

#하하씨가 다음 정류장에서 다음 칸에 탐
subway.append("하하")
print(subway)

#정형돈씨를 유재석/조새호 사이에 넣기
subway.insert(1,"정형돈")
print(subway)

#지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop())#pop제일뒤에있는 것을빼줌 
print(subway)

#같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

##정렬도 가능
num_list=[5,6,3,4,1]
num_list.sort()
print(num_list)

#순서 뒤집기 가능
num_list.reverse()
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list)

#다양한 자료형 함께 사용'

mix_list=["조새호",2,True]
print(mix_list)

#리스트 확장
num_list.extend(mix_list)
print(num_list)