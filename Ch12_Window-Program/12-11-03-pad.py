
## 위젯의 배치와 크기 조절: 위젯 사이에 여백 주기

from tkinter import *
window = Tk()

# Step 1. 버튼 인스턴스 3개 생성
# 리스트와 for문을 이용한 버튼 생성 및 출력
btnList = [None]*3 # btnList == [""]*3

# 리스트를 이용한 위젯을 for문으로 코드 간결화
for i in range(0, 3) :
    btnList[i] = Button(window, text="버튼"+str(i+1))


# Step 2. 버튼 3개를 화면에 수평으로 정렬해 출력
# padx=픽셀값: 픽셀값만큼 위젯 사이의 좌우 여백 조절
# pady=픽셀값: 픽셀값만큼 위젯 사이의 상하 여백 조절
for btn in btnList :
    btn.pack(side=TOP, fill=X, padx=10, pady=10)

window.mainloop()