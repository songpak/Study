twice = {'나연','정연','모모','다현','채영','쯔위'}
print(twice)
print(type(twice))

twice2 = set()
print(twice2)
print(type(twice))
twice = ['나연','정연','모모','다현','채영','쯔위','정연','다현','모모']
print(twice)
twice2 = set(twice) #twice의 중복된 데이터를 제거후 twice2에 들어간다
print(twice2)

print("쯔위가 멤버에 있습니까?","쯔위" in twice2)
print("쯔위가 멤버에 없습니까?","쯔위" not in twice2)

twice3 = {'나연','정연','사나','지효','미나'}
#중복된 것은 빼고 합친다 (합집합)
print(twice2.union(twice3))
#교집합
print(twice2.intersection(twice3))
#차집합
print(twice2 - twice3)
#or표시는 합집합이다
print(twice2 | twice3)
#and표시는 교집합이다
print(twice2 & twice3)

twice = {'나연','정연','사나','지효','미나'}
#위치는 자기 마음대로 추가
twice.add("고연")
print(twice)
twice.discard("고연")
print(twice)

