score_file=open("score.txt","w",encoding="utf8") # w를사용하면 텍스트파일에 적는용도
print("수학 : 0",file=score_file)
print("영어 : 50",file=score_file)
score_file.close()
#score_file이라는 텍스트가 옆에 생기면서 수학:0과 영어:50이라는 것이 적힘

score_file=open("score.txt","a",encoding="utf8")#존재하는파일에 이어서 적고싶으면 a를사용
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close()

score_file=open("score.txt","r",encoding="utf8")#r을사용하면 파일에있는 내용을 읽음
print(score_file.read())#모든내용을 읽음
print(score_file.readline())#줄별로 읽기, 한줄 읽고 커서는 다음 줄로 이동
score_file.close()

score_file=open("score.txt","r",encoding="utf8")
lines=score_file.readlines()
for line in lines:
    print(line,end="")
score_file.close()