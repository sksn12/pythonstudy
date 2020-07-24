absent=[2,5]#결석
no_book=[7]#책을깜빡함
for student in range(1,11):
    if student in absent:
        continue #continue문을 만나면 밑에 함수로 가지않고 다시 for문으로 돌아감
    elif student in no_book:
        print("오늘 수업 여기까지.{0}겨무실로".format(student))
        break 
    print("{0},책을 읽어봐".format(student))

       
 