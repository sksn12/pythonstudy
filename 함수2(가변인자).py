# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이: {1}\t주 사용 언어 : {2}".format(name,age,main_lang))
#     return(name,age,main_lang)

# profile("유재석",21,"파이싼")
# profile("김태호",22,"자바")

# #같은 학교 같은 학년 같은 반 같은 수업.
# def profile(name, age=21, main_lang="자바"):
#     print("이름 : {0}\t나이: {1}\t주 사용 언어 : {2}".format(name,age,main_lang))
#     return(name,age,main_lang)
# profile("유재석")
# profile("유재환")

# def pro(name, age, lang1,lang2,lang3,lang4,lang5):
#     print("이름:{0}\t 나이:{1}\t".format(name,age),end=" ")#end=" "출력되고나서 줄바꿈이 되지않고 밑에있는문장이 계속해서 출력됨
#     print(lang1,lang2,lang3,lang4,lang5)

#가변인자(함수자체의 값을 추가할때)
def pro(name, age, *langeuge):
    print("이름:{0}\t 나이:{1}\t".format(name,age),end=" ")#end=" "출력되고나서 줄바꿈이 되지않고 밑에있는문장이 계속해서 출력됨
    for lang in langeuge:
        print(lang, end=" ")
    print()

pro("유재석",20,"파이썬","자바","c","c++","c#","javescript")
pro("김태호",20,"c","ss"," "," "," ")



