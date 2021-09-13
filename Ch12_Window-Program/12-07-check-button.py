
## 윈도우 프로그램의 기본 위젯: 체크버튼

from tkinter import *
from tkinter import messagebox # 파이썬 3.6. 이후 버전에서 messagebox 오류 해결 방법


window = Tk()
window.title("체크버튼 연습") # 윈도우 창에 제목 표시


# 함수 정의 부분
# chk.get() 함수로 체크버튼에 설정된 값을 가져와 메시지 출력
def myFunc() :
    if chk.get() == 0 :
        messagebox.showinfo("", "체크버튼이 꺼졌어요.")
    else :
        messagebox.showinfo("", "체크버튼이 켜졌어요.")

    
# 메인 코드 부분
# IntVar() : 정수형 형식의 변수를 생성하는 함수
chk = IntVar() 

# Checkbutton 위젯으로부터 체크버튼 cb 인스턴스 생성
cb = Checkbutton(window, text = "클릭하세요", variable = chk, command = myFunc)
# 체크버튼을 켜면 chk에 1, 끄면 chk에 0이 대입 --> myFunc 실행

# 체크버튼 출력
cb.pack()

window.mainloop()
