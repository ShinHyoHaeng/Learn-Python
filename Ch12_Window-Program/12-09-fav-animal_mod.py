
## 좋아하는 동물 투표 프로그램
# 라디오버튼을 선택했을 때 이미지가 바로 변하도록 코드 변경
# '사진 보기' 버튼 삭제

from tkinter import *
window = Tk()
window.geometry("400x400")
window.title("좋아하는 동물 투표")

# 함수 정의 부분
# var 변수의 값에 따라 윈도우 하단 이미지라벨 영역의 이미지 변경
def myFunc() :
    if var.get() == 1 :
        labelImage.configure(image=photo1)
    elif var.get() == 2 :
        labelImage.configure(image=photo2)
    else :
        labelImage.configure(image=photo3)

# 메인 코드 부분
# 타이틀 텍스트 생성
# 라벨(텍스트): '좋아하는 동물 투표'라는 텍스트를 폰트 사이즈 20, 글씨체는 나눔고딕, 파란색으로 설정해 출력
labelText = Label(window, text = "좋아하는 동물 투표 ", fg = "blue", font=("나눔고딕 bold", 20))

var = IntVar() # IntVar() : 정수형 형식의 변수를 생성하는 함수

# 3개의 라디오 버튼 생성
# '강아지'라는 내용이 적힌 rb1 버튼을 선택하면 var 값으로 1이 대입
rb1 = Radiobutton(window, text = "강아지", variable = var, value = 1, command = myFunc)

# '고양이'라는 내용이 적힌 rb2 버튼을 선택하면 var 값으로 2가 대입
rb2 = Radiobutton(window, text = "고양이", variable = var, value = 2, command = myFunc)

# '토끼'라는 내용이 적힌 rb3 버튼을 선택하면 var 값으로 3이 대입
rb3 = Radiobutton(window, text = "토끼", variable = var, value = 3, command = myFunc)

# 3개의 이미지 추가: 각각 강아지, 고양이, 토끼 이미지 추가
# 각각의 라디오 버튼과 연결된 이미지를 지정
photo1 = PhotoImage(file="gif/dog4.gif")
photo2 = PhotoImage(file="gif/cat.gif")
photo3 = PhotoImage(file="gif/rabbit.gif")

# Label() 옵션에서 image 속성을 지정 --> 사이즈는 200x200, 배경색은 노랑, 초기값으로는 이미지 X
# 라디오버튼 중 하나를 선택 --> 사진보기 버튼을 클릭 --> labelImage 영역에 해당 값에 대입된 이미지 출력
labelImage = Label(window, width = 200, height = 200, bg = "yellow", image=None)

# 텍스트와 3개의 라디오 버튼, 1개의 버튼, 이미지 영역 출력
# padx: 좌우 여백(padding-left, padding-right)
# pady: 상하 여백(padding-top, padding-bottom)
labelText.pack(padx = 5, pady = 5)
rb1.pack(padx = 5, pady = 5)
rb2.pack(padx = 5, pady = 5)
rb3.pack(padx = 5, pady = 5)
labelImage.pack(padx = 5, pady = 5)

window.mainloop()