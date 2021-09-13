
## 위젯을 고정 위치에 배치(9개의 버튼을 3*3의 형태로 배치)

from tkinter import *

window = Tk()
window.geometry("150x150")

xPos, yPos = 0, 0
i = 0

btnList = [None]*10
for i in range(1,10) : # 시작값을 1로 설정
    btnList[i] = Button(window, text="버튼"+str(i))

# 버튼 배치
i = 1 # 버튼의 인덱스 초기화
for col in range(1,4) : # 행의 개수만큼 반복
    for row in range(1,4) : # 열의 개수만큼 반복
        btnList[i].place(x=xPos,y=yPos)
        xPos += 50  # 버튼을 x축으로 50씩 증가시켜 배치
        i += 1  # 버튼의 인덱스 증가
    xPos = 0  # 열의 개수만큼 반복이 끝나면(줄바꿈) 0으로 초기화
    yPos += 50  # 버튼을 세로로 50씩 증가시켜 배치

window.mainloop()