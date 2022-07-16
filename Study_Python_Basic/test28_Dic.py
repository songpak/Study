dicTwice = {10: '나연', 20: '정연', 30: '모모'}
print(dicTwice)
print(type(dicTwice))
print(dicTwice[10]) #key를 넣으면 value값이 나온다

dicTwice[15] = '사나' #key값이 없으면 추가
print(dicTwice)

dicTwice[15] = '힘쎈사나'   #key값이 존재하면 수정
print(dicTwice)

del dicTwice[15]    #key값으로 삭제
print(dicTwice)


