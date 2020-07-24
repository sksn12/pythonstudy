#프로그램상에서 사용한는 데이터를 파일형태로 저장
# import pickle
# profile_file=open("profile.pickle","wb")#쓰기목적인 w와 바이너리타입인b설정 따로 utf8설정필요없음 pickle사용을위해선 항상 b를 붙여야함
# profile={"이름":"박명수","나이":30,"취미":["축구","농구","배구"]}
# print(profile)
# pickle.dump(profile,profile_file)#profile에 있는 정보를 file에저장
# profile_file.close()