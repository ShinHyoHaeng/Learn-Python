## 리스트 조작 함수 사용

myList = [30,10,20]
print("현재 리스트 : %s" % myList)

# append(): 리스트 제일 뒤에 항목을 추가
myList.append(40) # 리스트 제일 뒤에 '40' 추가
print("append(40) 후의 리스트 :%s" % myList)

# pop(): 리스트 제일 뒤의 항목을 빼내고 빼낸 항목을 삭제 
print("pop()으로 추출한 값 : %s" % myList.pop()) 
print("pop() 후의 리스트 :%s" % myList)

# sort(): 리스트 항목을 오름차순으로 정렬
myList.sort()
print("sort() 후의 리스트 : %s" % myList)

# reverse(): 리스트 항목을 역순으로 정렬
myList.reverse()
print("reverse() 후의 리스트: %s" % myList)

# index(): 지정된 값의 위치 반환
print("20 값의 위치 : %d" % myList.index(20))

# insert(): 지정된 위치에 값을 삽입
myList.insert(2, 222) # myList의 myList[2] 자리에 '222' 삽입
print("insert(2,222) 후의 리스트 : %s" % myList)

# remove(): 리스트에서 지정한 값을 제거 --> 지정한 값이 여러 개일 경우 첫번째 값만 제거
myList.remove(222) # myList에서 '222' 삭제
print("remove(222) 후의 리스트 : %s" % myList)

# extend(): 리스트 뒤에 리스트 추가(리스트 + 연산과 동일)
myList.extend([77,88,77])
print("extend([77,88,77]) 후의 리스트 : %s" % myList)

# count(): 리스트에서 지정된 값이 몇 개 인지 카운트
print("77 값의 개수 : %d" % myList.count(77))

# del(): 리스트에서 해당 위치의 항목 삭제
del(myList[0]) # myList[0] 값 삭제
print("del(myList[0]) 후의 리스트 : %s" % myList)

# len(): 리스트에 포함된 전체 항목 개수 카운트
print("myList의 항목 개수 : %s" % len(myList))
