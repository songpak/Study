twice = ['나연','정연','모모','다현','채영','쯔위']
print(twice)
print("인원수: ",len(twice))

print(twice[0])
print(twice[1])
print(twice[2])
print(twice[3])
print(twice[4])
print(twice[5])

idx = twice.index('정연')
print(idx)
print("바꾸기 전 id: ", id(twice))

#데이터 바꾸기 가능
twice[idx] = '유또검정연'
print(twice)
print("바꾼 후 id: ", id(twice))

#맨 뒤에 데이터 추가
twice.append("효연")
print(twice)

#맨 뒤 데이터 삭제
twice.pop()
print(twice)

#인덱스 지정가능
twice.pop(1)
print(twice)

#특정 위치에 데이터 삽입 가능
twice.insert(1,'정연')
print(twice)

#특정 데이터 삭제, 앞에서 부터 찾아서 삭제한다
twice.append('정연')
print(twice)
twice.remove('정연')
print(twice)

#리스트 연장 twice2엔 지장이 없다
twice2 = ['사나','지효','미나']
twice.extend(twice2)
print(twice)
print(twice2)

#리스트 슬라이싱
print(twice[:3])
print(twice[3:6])
print(twice[6:])
print(twice[len(twice)-3:]) #끝에서 3개의 값을 구할때 사용

#데이터를 역순으로 만들어서 자기 자신한테 저장
twice3 = twice.reverse()
print(twice3) #따라서, twice3에 값이 전달되지 않는다
print(twice)
twice.reverse()
print(twice)

#
twice.sort(reverse=True) #내림차순으로 정렬
print(twice)
twice.sort(reverse=False) #오름차순으로 정렬
print(twice)

#
twice3 = ['쯔위','쯔위','쯔위']
twice.extend(twice3)
print(twice.count('쯔위')) #인수가 몇개 있는지 출력