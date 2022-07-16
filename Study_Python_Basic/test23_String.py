s1 = "Hello,python!!"
print(ord(s1[0])) #s1[0]의 값에 해당하는 아스키코드 값으로 변환
print(chr(72)) #n의 값에 해당하는 문자로 변환
print(len(s1)) #s1의 길이를 반환

print(max(s1)) #s1의 문자 중 아스키코드값이 제일 큰 문자를 반환
print(min(s1)) #가장 작은

#print(sorted(s1)) #아스키 코드값으로 오름차순 정렬하여 list타입으로 반환
s2 = sorted(s1)
print(s2)
print(type(s2))

#print(sorted(s1, reverse=True))
s3 = sorted(s1, reverse=True) #내림차순
print(s3)
print(type(s3))

s4 = reversed(s1) #문자열 역순할때 사용, 사용시에는 반드시 list로 변환해서 사용한다
s5 = list(s4)
print(s4)
print(type(s4))
print(s5)




