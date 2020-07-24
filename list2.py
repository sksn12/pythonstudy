# cabinet={3:"유재석",100:"김태호"}
# print(cabinet[3])
# print(cabinet[100])

# print(cabinet.get(3))
# print(cabinet.get(5,"사용가능"))

# print(3 in cabinet) # True
cabinet={"a":"유재석","b":"김태호"}
print(cabinet["a"])

# 새 손님
print(cabinet)
cabinet["a"]="김종국"
cabinet["c"]="조세호"
print(cabinet)

# 간 손님
del cabinet["a"]
print(cabinet)

#key값만 출력
print(cabinet.keys())

#value값출력
print(cabinet.values())

#key,value 쌍으로 출력
print(cabinet.items())

#목욕탕 폐점
cabinet.clear()
print(cabinet)