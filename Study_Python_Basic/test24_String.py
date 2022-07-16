s1 = "hello, PYTHON"
print(s1)
print(s1.capitalize()) #첫글자만 대문자, 나머지는 소문자로 변환
print(s1.title()) #각각의 문장마다 앞은 대문자로 변환 (,로 구분)
print(s1.upper()) #모든 문자를 대문자로
print(s1.lower()) #모든 문자를 소문자로

s2 = 'hello'
print(s2.center(10)) #10자리 중 s2를 가운데 출력
print(s2.center(10,'*')) #공백대신 *로 채움
print(s2.ljust(10,'*')) #오른쪽에 채움
print(s2.rjust(10,'*')) #왼쪽에 채움

print(s2.count('l')) #s2안에 l이 몇개 있는지 알려준다
print(s2.count('l',3)) #index 3번째 위치부터 l의 갯수 계산
print(s2.count('l',3,5)) #3번째부터 5번째 까지

s3 = 'this is a chair and that is a desk'
print(s3)
print(s3.index('is')) # >> 2
print(s3.rindex('is')) #거꾸로 시작해서 계산 >> 25
print(s3.index('is',10)) #index10번 이후의 'is'계산
print(s3.index('is',3,10)) # 3~9사이
#print(s3.index('kk'))

print(s3.find('is')) #있으면 index 반환
print(s3.find('kk')) #없으면 -1 반환

fruit = ['melon','apple','kiwi']
print(fruit)
print(type(fruit))
s4 = '***'
t4 = s4.join(fruit) #리스트 사이사이에 ***넣어서 새로운 문자열 탄샐
print(t4)
print(type(t4))

####################
book = ('java','python','c++') #튜플, 집합, 사전도 마찬가지
s5 = '~~~'
t5 = s5.join(book)
print(t5)

#####################
book = {'java','python','c++'} #집합은 마찬가지로 순서가 뒤죽박죽
s6 = '~~~'
t6 = s6.join(book)
print(t6)

####################
book = {'java':1,'python':2,'c++':3} #Key값만 결합을 한다. 따라서 반드시 문자열로 key값이 구성되어 있어야한다
s7 = '~~~'
t7 = s7.join(book)
print(t7)

####################
name = "Peter pen" #문자열은 문자 하나하나 다 조인한다
s8 = "**"
t8 = s8.join(name)
print(t8)

#####################
words = 'desk pencil computer book chair'
s = words.split()
print(s)
print(type(s))

words = 'desk-pencil-computer-book-chair'
s = words.split('-')
print(s)
s = words.split('-',2)
print(s)

########################
test = "           aaa      "
print(test)
print(test.strip()) #양쪽 모두 재거
print(test.rsplit()) #오른쪽 공백 제거
print(test.lstrip()) #왼쪽 공백 제거

##########################
x = "You should go to shcool today"
t = x.partition("go") #go를 중심으로 3개의 문자열을 가진 튜플로 반환 >>웹 크롤링에 많이 이용
print(type(t))
print(t[0])
print(t[1])
print(t[2])
