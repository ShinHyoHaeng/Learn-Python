
## 위젯을 고정 위치에 배치(for문으로 수정(과정))

from tkinter import *

window = Tk()
window.geometry("210x210")

# Step 1. 이미지 준비
'''
photo1 = PhotoImage(file="gif/puz1.gif")
photo2 = PhotoImage(file="gif/puz2.gif")
photo3 = PhotoImage(file="gif/puz3.gif")
photo4 = PhotoImage(file="gif/puz4.gif")
photo5 = PhotoImage(file="gif/puz5.gif")
photo6 = PhotoImage(file="gif/puz6.gif")
photo7 = PhotoImage(file="gif/puz7.gif")
photo8 = PhotoImage(file="gif/puz8.gif")
photo9 = PhotoImage(file="gif/puz9.gif")
'''
# for문으로 변경
photoList = [None]*10
for i in range(1,10) : # 시작값을 1로 설정
    photoList[i] = PhotoImage(file="gif/puz"+str(i)+".gif")


# Step 2. 이미지를 입힌 버튼 생성
'''
btn1 = Button(window, image=photo1)
btn2 = Button(window, image=photo2)
btn3 = Button(window, image=photo3)
btn4 = Button(window, image=photo4)
btn5 = Button(window, image=photo5)
btn6 = Button(window, image=photo6)
btn7 = Button(window, image=photo7)
btn8 = Button(window, image=photo8)
btn9 = Button(window, image=photo9)
'''
# for문으로 변경
btnList = [None]*10
for i in range(1,10) :
    btnList[i] = Button(window, image=photoList[i])


# Step 3. 버튼 배치
'''
btn1.place(x=0, y=0)
btn2.place(x=70, y=0)
btn3.place(x=140, y=0)
btn4.place(x=0, y=70)
btn5.place(x=70, y=70)
btn6.place(x=140, y=70)
btn7.place(x=0, y=140)
btn8.place(x=70, y=140)
btn9.place(x=140, y=140)
'''

# 이중 for문으로 변경
xPos, yPos = 0, 0 # place의 x, y 좌표값
i = 1 # 버튼의 인덱스 초기화
for col in range(1,4) : # 행의 개수만큼 반복
    for row in range(1,4) : # 열의 개수만큼 반복
        btnList[i].place(x=xPos, y=yPos)
        xPos += 70 # 버튼을 x축으로 70씩 증가시켜 배치
        i += 1 # 버튼의 인덱스 증가
    xPos = 0 # 열의 개수만큼 반복이 끝나면(줄바꿈) 0으로 초기화
    yPos += 70 # 버튼을 세로로 70씩 증가시켜 배치

window.mainloop()