
## 위젯의 배치와 크기 조절: 수평으로 정렬(for문 사용)

from tkinter import *
window = Tk()

# Step 1. 버튼 인스턴스 3개 생성
'''
button1 = Button(window, text="버튼1")
button2 = Button(window, text="버튼2")
button3 = Button(window, text="버튼3")
'''

# 리스트와 for문을 이용한 버튼 생성 및 출력
# 빈 리스트 생성
btnList = [None]*3 # btnList == [""]*3

# 리스트를 이용한 위젯을 for문으로 코드 간결화
for i in range(0, 3) :
    btnList[i] = Button(window, text="버튼"+str(i+1))
print(btnList)
# 리스트 생성 확인: [<tkinter.Button object .!button>, <tkinter.Button object .!button2>, <tkinter.Button object .!button3>]


# Step 2. 버튼 3개를 화면에 수평으로 정렬해 출력
'''
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
'''

# 2-1. for in range 방식
for i in range(0, 3) :
    btnList[i].pack(side=RIGHT)

# 2-2. 리스트 반복문(for 변수 in 리스트) 방식
for btn in btnList :
    btn.pack(side=RIGHT)


window.mainloop()