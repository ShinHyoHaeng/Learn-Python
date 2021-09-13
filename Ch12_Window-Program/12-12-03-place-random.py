
## 위젯을 고정 위치에 배치(응용: 이미지 배치 랜덤)

from tkinter import *
import random # 이미지를 랜덤하게 출력하기 위해 random 모듈 활용

window = Tk()
window.geometry("210x210")

# 변수 선언
xPos, yPos = 0, 0 # place의 x, y 좌표값
i = 0

# 리스트에 랜덤 이미지 배치
fnameList = ["gif/puz1.gif"]
for i in range(2,10) :
    fnameList.append("gif/puz"+str(i)+".gif")
    random.shuffle(fnameList) # 리스트 섞기

# 섞인 이미지 및 이미지를 입힐 버튼 준비
photoList = [None]*10 # 리스트는 0부터 시작
btnList = [None]*10
for i in range(1,10) : # 시작값을 1로 설정
    photoList[i] = PhotoImage(file=fnameList[i-1]) # 랜덤함수로 재배치된 이미지 리스트 호출
    btnList[i] = Button(window, image=photoList[i])

# 버튼 배치
i = 1 # 버튼의 인덱스 초기화
for col in range(1,4) : # 행의 개수만큼 반복
    for row in range(1,4) : # 열의 개수만큼 반복
        btnList[i].place(x=xPos, y=yPos)
        xPos += 70 # 버튼을 x축으로 70씩 증가시켜 배치
        i += 1 # 버튼의 인덱스 증가
    xPos = 0 # 열의 개수만큼 반복이 끝나면(줄바꿈) 0으로 초기화
    yPos += 70 # 버튼을 세로로 70씩 증가시켜 배치

window.mainloop()