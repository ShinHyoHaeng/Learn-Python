score=int(input("점수를 입력하세요 : "))
'''
if   score >= 90 :
     print("A")
elif score >= 80 :
     print("B")
elif score >= 70 :
     print("C")
elif score >= 60 :
     print("D")
else :
     print("F")
'''

if   score >= 90 :
     print("A")
if score >= 80 and score < 90 :
     print("B")
if score >= 70 and score < 80 :
     print("C")
if score >= 60 and score < 70 :
     print("D")
if score < 60  :
     print("F")

print("학점 입니다. ^^")
