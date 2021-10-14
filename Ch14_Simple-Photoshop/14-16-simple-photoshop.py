## 미니 포토샵 프로그램 제작 완성 코드

## 1. 사용할 라이브러리 혹은 모듈 가져오기
from tkinter import *
from tkinter.filedialog import *  # 파일 입출력을 위한 모듈
from tkinter.simpledialog import *  # 숫자나 문자를 입력받기 위한 모듈
from wand.image import *  # 설치한 이미지 처리 기능을 제공하는 이미지매직의 라이브러리 가져오기

# GIF 뿐만 아니라 JPG, PNG 같은 이미지를 모두 처리하기 위해 외부 라이브러리인 이미지매직 사용


## 2. 변수 선언 부분(모든 함수들이 공통적으로 사용할 수 있도록 전역 함수로 선언)
window, canvas, paper = None, None, None
photo, photo2 = None, None  # photo: 원본 이미지 / photo2: 처리 결과를 저장할 변수
oriX, oriY = 0, 0  # 원본 이미지의 폭과 높이를 저장하는 변수

## 3. 함수 정의 부분(각 메뉴를 선택할 때 실행될 함수 선언)
'''
3.1. displayImage(이미지, 가로, 세로) 함수
    - 이미지를 화면에 출력하는 함수(메뉴를 선택할 때마다 실행 X)
    - 각 함수에서 처리한 결과 이미지의 세가지 정보를 넘겨받아 화면에 출력
    - displayImage() 함수의 처리 과정
        - 넘겨 받은 이미지의 크기와 동일하게 윈도우 창 크기 설정
        - 새 캔버스 생성, 기존의 이미지가 출력된 캔버스 초기화
        - 새 캔버스에 paper overlay --> 처리된 이미지를 그 위에 출력
        - paper에 이미지를 출력하기 위해 이미지 파일의 모든 점(픽셀)에 접근
        - 이미지 폭과 높이만큼 반복해 픽셀의 RGB값 추출
        - paper에 이미지의 픽셀을 컬러로 찍어 이미지 구현
        - 처리된 결과 이미지의 픽셀을 찍어둔 paper가 overlay된 캔버스를 화면에 출력
'''
def displayImage(img, width, height):
    global window, canvas, paper, photo, photo2, oriX, oriY

    # 넘겨받은 이미지의 크기와 동일하게 윈도우 창의 크기 설정
    window.geometry(str(width) + "x" + str(height))

    # 캔버스가 이미 존재한다면 기존 캔버스를 삭제
    if canvas != None:
        canvas.destroy()

    # 새 캔버스 생성(처리된 이미지의 가로, 세로 사이즈대로 생성)
    canvas = Canvas(window, width=width, height=height)

    # 새 캔버스에 overlay할 페이퍼 생성(처리된 이미지의 가로, 세로 사이즈대로 생성)
    # 새 페이퍼는 빈 이미지를 보여주기 때문에 PhotoImage()로 생성
    paper = PhotoImage(width=width, height=height)

    # 새 캔버스 위에 새 페이퍼를 overlay(이후 페이퍼 위에 처리된 이미지 출력 예정)
    # 생성 위치: 가로 세로 사이즈의 중간 위치
    canvas.create_image((width / 2, height / 2), image=paper, state="normal")

    # 새 캔버스와 새 페이퍼 위에 처리된 이미지 출력
    '''
    - func_open()에서 이미지를 불러오면 Wand 라이브러리의 Image()를 사용해 이미지 생성
    - Image()에 의해 생성된 이미지는 configure() 함수 적용 불가
    - make_blob(format=None): 이미지를 바이러니 코드로 변환해주는 함수로 값은 배열 형태로 저장
        - 이미지의 픽셀에 접근해 rgb값을 각 배열의 형태로 저장(ex. [blob[0]r,blob[0]g,blob[0]b,blob[1]r,blob[1]g,blob[1]b.......])
        - 이미지 픽셀 개수*3의 인덱스가 배열에 저장
    '''
    blob = img.make_blob(format='RGB')
    # print(type(blob)): blob 자료형 출력. blob의 자료형은 byte로 리스트 형태의 문자열 데이터 타입

    # 이미지의 폭과 높이만큼 반복해 픽셀의 RGB 값 추출
    for i in range(0, width):
        for k in range(0, height):
            r = blob[(i * 3 * width) + (k * 3) + 0]  # blob[0],blob[3],blob[6],blob[9]...의 값을 r에 저장
            g = blob[(i * 3 * width) + (k * 3) + 1]  # blob[0],blob[3],blob[6],blob[9]...의 값을 g에 저장
            b = blob[(i * 3 * width) + (k * 3) + 2]  # blob[0],blob[3],blob[6],blob[9]...의 값을 b에 저장

            # 종이에 컬러로 점을 찍어줌. 이미지의 폭과 높이만큼 반복
            paper.put("#%02x%02x%02x" % (r, g, b), (k, i)) # r,g,b값을 (02x)로 각각 두자리 16진수로 변환해 rgb값으로 결합한 후 (k, i)에 찍어줌

    # 처리된 종이를 붙인 캔버스 화면에 출력
    canvas.pack()

'''
3.2. 파일 열기
    - [파일 열기] 메뉴를 통해 선택된 원본 이미지는 photo에 저장
    - 함수에 의해 처리되어 화면에 보여질 이미지는 photo2에 저장
    - 작동 원리: 원본 이미지 photo의 정보에 대해 명령을 적용(photo2의 정보 X)
        - 함수를 거듭 실행하면 원본 이미지가 훼손되기 때문
    - 다음 함수를 실행하면 화면에 출력되는 photo2는 매번 원본 photo를 복제해 명령 처리
    - 함수를 실행할 때 복제 과정을 생략하면 직전 이미지에 적용
'''
def func_open():
    global window, canvas, paper, photo, photo2, oriX, oriY  # 전역변수를 함수 안에서 사용하기 위해 선언

    # askopenfilename()은 파일 열기 대화상자를 표시해 그림 파일 선택
    redFp = askopenfilename(parent=window, filetypes=(("모든 그림 파일", "*.jpg;*.jpeg;*.bmp;*.png;*.tif;*.gif"), ("모든 파일", "*.*")))

    # 이미지는 GIF, JPG, PNG를 불러와 모두 처리하기 위해 PhotoImage()가 아닌 Wand 라이브러리에서 제공하는 Image() 사용
    photo = Image(filename=redFp)  # 선택한 파일을 Image()로 열어 photo에 저장(photo: 처음 불러들인 원본 이미지)

    oriX = photo.width # 원본 이미지의 가로 사이즈를 oriX에 저장
    oriY = photo.height # 원본 이미지의 세로 사이즈를 oriY에 저장

    photo2 = photo.clone() # 원본 이미지(photo)를 복사해 Photo2에 저장(photo2: 처리 결과를 저장할 변수)

    # 결과 이미지 크기 계산
    newX = photo2.width
    newY = photo2.height

    # displayImage(출력할 이미지, 폭, 높이) 함수를 호출해 화면에 출력
    displayImage(photo2, newX, newY)


'''
3.3. 파일 저장
'''
def func_save():
    global window, canvas, paper, photo, photo2, oriX, oriY  # 전역변수를 함수 안에서 사용하기 위해 선언

    # photo2는 func_open() 함수를 실행했을 때 생성
    # photo2가 없다면(=파일을 열지 않았다면) [저장하기]를 눌렀을 때 함수를 빠져나감
    if photo2 == None:
        return

    # 대화 상자로부터 넘겨받은 파일의 정보를 saveFp에 저장
    saveFp = asksaveasfile(parent=window, mode="w", defaultextention=".jpg", filetypes=(("JPG 파일", "*.jpg;*.jpeg"), ("모든 파일", "*.*")))  # 저장할 파일을 입력 받음
    savePhoto = photo2.convert("jpg")  # 결과 이미지인 photo2를 convert("jpg") 함수를 이용해 jpg 파일로 변환
    savePhoto.save(filename=saveFp.name)  # save() 함수로 변환한 jpg 파일을 저장


'''
3.4. 프로그램 종료
'''
def func_exit():
    window.quit()
    window.destroy()


'''
3.5. 이미지 확대
    - Wand 라이브러리에서 제공하는 resize(가로, 세로) 함수를 사용 
'''
def func_zoomin():
    global window, canvas, paper, photo, photo2, oriX, oriY  # 전역변수를 함수 안에서 사용하기 위해 선언

    # askinteger() 함수를 실행해 대화 상자로 확대할 배수를 입력 받음(최소값 2, 최대값 4)
    scale = askinteger("확대배수", "확대할 배수를 입력하세요", minvalue=2, maxvalue=4)

    photo2 = photo.clone()

    # 원본 이미지의 가로 세로 사이즈에 배수를 곱하여 크기 변경
    photo2.resize(int(oriX * scale), int(oriY * scale))

    newX = photo2.width # 변경된 이미지의 가로 사이즈 newX에 저장
    newY = photo2.height # 변경된 이미지의 세로 사이즈 newY에 저장

    # 처리된 이미지의 이미지, 크기 정보를 displayImage() 함수에 넘겨줌
    displayImage(photo2, newX, newY)

'''
3.6. 이미지 축소
    - Wand 라이브러리에서 제공하는 resize(가로, 세로) 함수를 사용 
'''
def func_zoomout():
    global window, canvas, paper, photo, photo2, oriX, oriY  # 전역변수를 함수 안에서 사용하기 위해 선언

    # askinteger() 함수를 실행해 대화 상자로 축소할 배수를 입력 받음(최소값 2, 최대값 4)
    scale = askinteger("축소", "축소할 배수를 입력하세요", minvalue=2, maxvalue=4)

    photo2 = photo.clone()

    # 원본 이미지의 가로 세로 사이즈에 배수를 곱하여 크기 변경
    photo2.resize(int(oriX / scale), int(oriY / scale))

    newX = photo2.width  # 변경된 이미지의 가로 사이즈 newX에 저장
    newY = photo2.height  # 변경된 이미지의 세로 사이즈 newY에 저장

    # 처리된 이미지의 이미지, 크기 정보를 displayImage() 함수에 넘겨줌
    displayImage(photo2, newX, newY)

'''
3.7. 상하 반전
    - flip() 함수 사용
'''
def func_mirror1():
    global window, canvas, paper, photo, photo2, oriX, oriY  # 전역변수를 함수 안에서 사용하기 위해 선언

    photo2 = photo.clone()
    photo2.flip()

    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)


'''
3.8. 좌우 반전
    - flop() 함수 사용
'''
def func_mirror2():
    global window, canvas, paper, photo, photo2, oriX, oriY  # 전역변수를 함수 안에서 사용하기 위해 선언

    photo2 = photo.clone()
    photo2.flop()

    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

'''
3.9. 이미지 회전
    - 대화 상자를 통해 정수를 입력받아 그 수만큼 회전
    - Wand 라이브러리에서 제공하는 rotate(각도) 함수를 사용
'''
def func_rotate():
    global window, canvas, paper, photo, photo2, oriX, oriY  # 전역변수를 함수 안에서 사용하기 위해 선언

    degree = askinteger("회전", "회전할 각도를 입력하세요", minvalue=0, maxvalue=360)

    photo2.clone()
    photo2.rotate(degree)

    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

'''
3.10. 이미지 밝게/어둡게
    - 대화 상자를 통해 정수를 입력받아 그 수만큼 이미지의 명도 조정
    - Wand 라이브러리에서 제공하는 modulate(명도값, 채도값, 색상값) 함수를 사용
    - 명도는 modulate(명도값, 100, 100) 함수를 사용
    - 원본의 명도 값을 100으로 설정 --> 100 이상은 '밝게', 100 이하는 '어둡게' 처리
'''
def func_bright():
    global window, canvas, paper, photo, photo2, oriX, oriY  # 전역변수를 함수 안에서 사용하기 위해 선언

    # askinteger() 함수를 실행해 대화 상자로 명도값 받음(최소값 100, 최대값 200)
    value = askinteger("밝게", "값을 입력하세요(100~200)", minvalue=100, maxvalue=200)

    photo2.clone()
    photo2.modulate(value, 100, 100)

    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

def func_dark():
    global window, canvas, paper, photo, photo2, oriX, oriY  # 전역변수를 함수 안에서 사용하기 위해 선언

    # askinteger() 함수를 실행해 대화 상자로 명도값 받음(최소값 0, 최대값 100)
    value = askinteger("어둡게", "값을 입력하세요(0~100)", minvalue=0, maxvalue=100)

    photo2.clone()
    photo2.modulate(value, 100, 100)

    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

'''
3.11. 이미지 선명하게/탁하게
    - 대화 상자를 통해 정수를 입력받아 그 수만큼 이미지 채도 조정
    - Wand 라이브러리에서 제공하는 modulate(명도값, 채도값, 색상값) 함수를 사용
    - 채도는 modulate(100, 채도값, 100) 함수를 사용
    - 원본의 채도값이 100 --> 100 이상은 '선명하게', 100 이하는 '탁하게' 처리
'''
def func_clear():
    global window, canvas, paper, photo, photo2, oriX, oriY  # 전역변수를 함수 안에서 사용하기 위해 선언

    value = askinteger("선명하게", "값을 입력하세요(100~200)", minvalue=100, maxvalue=200)

    photo2.clone()
    photo2.modulate(100, value, 100)

    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

def func_unclear():
    global window, canvas, paper, photo, photo2, oriX, oriY  # 전역변수를 함수 안에서 사용하기 위해 선언

    value = askinteger("선명하게", "값을 입력하세요(0~100)", minvalue=0, maxvalue=100)

    photo2.clone()
    photo2.modulate(100, value, 100)

    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

'''
3.12. 흑백 이미지 처리
    - 이미지 type 값을 "grayscale"로 설정
'''
def func_bw():
    global window, canvas, paper, photo, photo2, oriX, oriY  # 전역변수를 함수 안에서 사용하기 위해 선언

    photo2.clone()
    photo2.type = "grayscale"

    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

'''
3.13. 되돌리기(추가 기능)
'''
def func_revert():
    global window,canvas, paper, photo, photo2, oriX, oriY,newX, newY  # 전역 변수 선언
    photo2 = photo.clone()
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)


## 4. 메인 코드 부분
window = Tk()
window.geometry("250x250")
window.title("Simple Photoshop_v0.1")

'''
4.1. 빈 이미지 출력
'''
photo = PhotoImage()
pLabel = Label(window, image=photo)
pLabel.pack(expand=1, anchor=CENTER)

'''
4.2. 메뉴 생성
    4.2.1. 메뉴 자체 생성
        - 메뉴 자체 = Menu(부모 윈도우)
        - 부모 윈도우.config(menu=메뉴 자체)
'''
mainMenu = Menu(window)
window.config(menu=mainMenu)

'''
    4.2.2. 상위 메뉴 생성
        - 상위 메뉴 = Menu(메뉴 자체)
        - 메뉴 자체.add_cascade(label="상위 메뉴 텍스트)", menu=상위 메뉴)
        - add_cascade() 함수는 상위 메뉴와 하위 메뉴를 연결
'''
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="파일", menu=fileMenu)

'''
    4.2.3. 하위 메뉴 생성
        - 상위메뉴.add_command(label="하위메뉴1", command=함수1)
          상위메뉴.add_command(label="하위메뉴2", command=함수2)
        - add_command() 함수는 기본 메뉴 항목 생성  
'''
fileMenu.add_command(label="파일 열기", command=func_open)
fileMenu.add_command(label="파일 저장", command=func_save)
fileMenu.add_separator() # 구분선 삽입
fileMenu.add_command(label="되돌리기", command=func_revert)
fileMenu.add_separator() # 구분선 삽입
fileMenu.add_command(label="프로그램 종료", command=func_exit)

image1Menu = Menu(mainMenu)
mainMenu.add_cascade(label="이미지 처리(1)", menu=image1Menu)
image1Menu.add_command(label="확대", command=func_zoomin)
image1Menu.add_command(label="축소", command=func_zoomout)
image1Menu.add_separator() # 구분선 삽입
image1Menu.add_command(label="상하 반전", command=func_mirror1)
image1Menu.add_command(label="좌우 반전", command=func_mirror2)
image1Menu.add_command(label="회전", command=func_rotate)

image2Menu = Menu(mainMenu)
mainMenu.add_cascade(label="이미지 처리(2)", menu=image2Menu)
image2Menu.add_command(label="밝게", command=func_bright)
image2Menu.add_command(label="어둡게", command=func_dark)
image2Menu.add_separator() # 구분선 삽입
image2Menu.add_command(label="선명하게", command=func_clear)
image2Menu.add_command(label="탁하게", command=func_unclear)
image2Menu.add_separator()
image2Menu.add_command(label="흑백이미지", command=func_bw)

window.mainloop()
