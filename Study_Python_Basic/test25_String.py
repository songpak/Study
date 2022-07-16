s1 = 'hello java java java'
print(s1.replace('java','python',2)) #앞에서부터 2개만 대체한다

s2 = 'hello'
print(s2.zfill(10)) #문자열의 길이를 10로 만들고 부족한건 0으로 채운다, 숫자가 길이보다 작으면 영향X

'''
istitle() : 뮨자열을 구성하는 단어들 각각이 대문자로 시작하는지 판단
isalnum() : 문자열이 열문자 또는 숫자로만 구성이 되어있는지 판단
isalpha() : 문자열이 모두 알파벳인 경우인지 판단 
isdigit() : 문자열이 모두 숫자로 구성되어있는지 판단
isdentifier() : 문자열이 식별자로 사용할 수 있는지 판단 (변수명이 올바른지 판단)
islower() : 문자열이 모두 소문자인지 판단
isupper() : 문자열이 모두 대문자인지 판단
isspace() : 문자열이 모두 스페이스로 되어있는지 판단
'''

a = 1
a = eval('a+4') #식을 전달하면 그 결과를 반환
print(a)
#b = eval('a = a+1') #대입 연산은 불가능하다
exec('a = a+1') #문장을 전달하면 그 문장을 실행
print(a)
