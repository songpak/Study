a = 10
print(a)

a = -10
print(a)
print(abs(a)) #abs함수 : 절대값 출력

b = 3
print("몫: ", a//b, ",나머지: ", a%b)

c,d = divmod(a,b) #몫은 c, 나머지는 d에 반환이 된다
print("몫: ",c, ",나머지: ",d)
#자바와 달리 return값이 두개 이상 가능하다

a = 2
b = 4
print(pow(a,b)) #a의 b승