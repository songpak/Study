s1 = 'Hello'
print(s1)
print(s1[0]) #인덱스로 접근할 수 있다
print(s1[4])

print(s1[-1]) #음수 인덱스 가능, -1은 문자열의 맨 끝
print(s1[-5])

print(s1[1:]) #s1[1]부터 끝까지
print(s1[:3]) #처음부터 s1[3] 전까지
print(s1[:]) #처음부터 끝까지
print(s1[1:3]) #1번째부터 3 전까지
print(s1[::2]) #0번째부터 끝까지 2칸씩 이동하면서 출력 >> Hlo
print(s1[1:4:2]) #1번째부터 4위치까지 2칸씩 이동하면서 출력

print(s1[::-1]) #거꾸로 출력
print(s1[-2:-5:-2])

"""s1[0] = 'h'
print(s1)
문자열은 바꾸지 못한다"""

print("수정전 s1: ", id(s1))
s1 = 'h' + s1[1:]
print(s1)
print("수정후 s1: ",id(s1))
