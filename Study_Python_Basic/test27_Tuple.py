twice = ('나연', '정연', '모모', '다현', '채영', '쯔위')
print(twice)

print(twice[0])     #특정값을 반환
print(twice[1])
print(twice[2])
print(twice[3])
print(twice[4])
print(twice[5])

print("인원수 : ", len(twice))
idx = twice.index('정연')
print(idx)

#twice[idx] = '유또검정연'   튜플은 리스트와 유사하지만 수정이 안된다
#print(twice)

twice2 = ('사나', '지효', '미나')
twice += twice2
print(twice)

print(twice[:3])
print(twice[3:6])
print(twice[len(twice)-3:])

twice3 = ('쯔위', '쯔위', '쯔위')
twice += twice3
print(twice)
print(twice.count("쯔위"))
#리스트는 값을 변경하는 곳에서 사용이 되고, 튜플은 값을 검색하는 곳에서 주로 사용

a, b = 10, 20   #(10, 20)
print(a, b)
c = (10, )
print(type(c))