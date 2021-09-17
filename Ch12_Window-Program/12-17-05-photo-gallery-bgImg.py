
## 사진 앨범 보기 프로그램
# 수정 3-3: UI 디자인(배경 이미지 변경)

from tkinter import *

# 변수 선언 부분
fnameList = ["jeju1.gif"] # 첫번째 파일만 넣은 배열 생성
for i in range(2,10) : # 두번째 이미지부터는 반복문으로 처리
    fnameList.append("jeju"+str(i)+".gif") # append() 함수: 리스트 제일 뒤에 항목을 추가

num = 0

# 함수 정의 부분
def clickNext() : # '다음' 버튼을 클릭하면 실행되는 함수
    global num # 전역변수인 num을 함수 안에서 사용
    num += 1 # '다음' 버튼을 누를 때마다 index 1씩 증가(다음 사진 출력)
    if num > 8: # index의 최대값: 8 --> 8에서 '다음' 버튼을 누르면 0번 이미지 출력(loop)
        num = 0
    photo = PhotoImage(file="gif/"+fnameList[num]) # 변경된 이미지 인덱스에 해당하는 이미지가 출력되도록 수정
    pTitle.configure(text=fnameList[num]) # 변경된 이미지명에 따라 출력되는 텍스트 변경
    pLabel.configure(image=photo)
    pLabel.image=photo

def clickPrev() : # '이전' 버튼을 클릭하면 실행되는 함수
    global num
    num -= 1 # '이전' 버튼을 누를 때마다 index 1씩 감소(이전 사진 출력)
    if num < 0:
        num = 8
    photo = PhotoImage(file="gif/"+fnameList[num])
    pTitle.configure(text=fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image=photo

def pageUp(event) : # PageUp키를 누르면 실행되는 함수
    clickNext() # '다음' 버튼을 눌렀을 때와 동일한 액션 실행

def pageDown(event) : # PageDown키를 누르면 실행되는 함수
    clickPrev() # '이전' 버튼을 눌렀을 때와 동일한 액션 실행

# 메인 코드 부분
window = Tk()
window.geometry("705x700") # 배경 이미지 사이즈와 동일하게 변경
window.title("사진 앨범")
window.configure(background="#000")

# 배경 이미지 출력
bgImg = PhotoImage(file="ui/album_bg.png") # 배경 이미지 준비
bgLabel = Label(window, image=bgImg) # 이미지 생성
bgLabel.place(x=-2, y=-2) # 배경 이미지 배치(윈도우에 출력시 여백문제로 값을 -2로 설정)

# 윈도우 창에서 키보드 이벤트를 처리하도록 설정
window.bind("<Prior>", pageUp)
window.bind("<Next>", pageDown)

# 버튼 이미지 준비
prevImg = PhotoImage(file="ui/album_butprev.png")
nextImg = PhotoImage(file="ui/album_butnext.png")

# 버튼을 눌렀을 때 함수와 연결
# bd: border
# highlightthickness: box-shadow
btnPrev = Button(window, image=prevImg, command=clickPrev, bd=0, highlightthickness=0)
btnNext = Button(window, image=nextImg, command=clickNext, bd=0, highlightthickness=0)

# 프로그램 최초 실행 시 첫번째 이미지 출력
photo = PhotoImage(file="gif/"+fnameList[0])
pTitle = Label(window, text=fnameList[0], font=("Arial", 15), fg="#ffffff", bg="#000000")
pLabel = Label(window, image=photo)

# 버튼과 이미지 배치
# 배경 이미지에 맞춰 배치 변경
btnPrev.place(x=610, y=75)
btnNext.place(x=660, y=75)
pTitle.place(x=610, y=610)
pLabel.place(x=20, y=130)

window.mainloop()
