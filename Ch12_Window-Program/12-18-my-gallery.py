
## 사진 앨범 보기 프로그램
# 여행 가고 싶은 나라 사진들로 사진 앨범 만들기

from tkinter import *

# 변수 선언 부분
fnameList = ["paris1.png"] # 첫번째 파일만 넣은 배열 생성
for i in range(2,7) : # 두번째 이미지부터는 반복문으로 처리
    fnameList.append("paris"+str(i)+".png")

num = 0

# 함수 정의 부분
# '다음' 버튼을 클릭하면 실행되는 함수
def clickNext() :
    global num
    num += 1
    if num > 5:
        num = 0
    photo = PhotoImage(file="paris/"+fnameList[num])
    pTitle.configure(text=fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image=photo

# '이전' 버튼을 클릭하면 실행되는 함수
def clickPrev() :
    global num
    num -= 1
    if num < 0:
        num = 5
    photo = PhotoImage(file="paris/"+fnameList[num])
    pTitle.configure(text=fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image=photo

# PageUp키를 누르면 실행되는 함수
def pageUp(event) :
    clickNext()

# PageDown키를 누르면 실행되는 함수
def pageDown(event) :
    clickPrev()

# 메인 코드 부분
window = Tk()
window.geometry("597x690")
window.title("Paris")
window.configure(background="#fff")

# 버튼 키보드 이벤트
window.bind("<Prior>", pageUp)
window.bind("<Next>", pageDown)

# 버튼 이미지 준비
prevImg = PhotoImage(file="ui/prev.png")
nextImg = PhotoImage(file="ui/next.png")

# 버튼을 눌렀을 때 함수와 연결
btnPrev = Button(window, image=prevImg, command=clickPrev, bd=0, highlightthickness=0)
btnNext = Button(window, image=nextImg, command=clickNext, bd=0, highlightthickness=0)

# 프로그램 최초 실행 시 첫번째 이미지 출력
photo = PhotoImage(file="paris/"+fnameList[0])
pTitle = Label(window, text=fnameList[0], font=("Century", 12), fg="#000", bg="#fff") # 좌측 상단 파일명
paris = Label(window, text="Paris, France", font=("BrushScript BT", 55), fg="#000", bg="#fff") # 이미지 하단 텍스트
pLabel = Label(window, image=photo)

# 버튼과 이미지 배치
btnPrev.place(x=450, y=30)
btnNext.place(x=550, y=30)
pTitle.place(x=20, y=28)
pLabel.place(x=20, y=70)
paris.place(x=175, y=510)
window.mainloop()