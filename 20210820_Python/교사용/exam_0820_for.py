#for 문을 이용해서 1에서부터 n까지의 합을 구하는 팩토리얼 
i, hap = 0, 0
num = 0

num = int(input("값 입력:"))

# for 문을 이용한 반복문 
# for 변수 in range(시작값, 끝값+1, 증가값)
'''
for i in range(1, num+1, 1) :
    hap = hap + i
    #hap += i
'''
# while 문을 이용한 반복문 
# 변수 = 시작값
# while 변수값 < 끝값+1 :
# 변수 = 변수 + 증가값
i=1
while i < num+1:
    hap = hap + i
    i=i+1
    
print("1에서 %d까지 합 : %d" % (num, hap))





