n = int(input("초를 입력: "))
h, k = divmod(n,3600)
m, s = divmod(k,60)

print(n,"초는 ",h,"시간",m,"분",s,"초입니다")