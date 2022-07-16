a = 10
print(id(a))

a = 20
print(id(a)) #값이 변경되어 주소가 바뀌었다

b = [100,200,300]
print(id(b))
b[1] = 500
print(id(b)) #변수의 값이 변경가능하여 주소가 바뀌지 않았다