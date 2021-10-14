
## Python 능력단위 과제: 미니 포토샵 프로그램 제작

from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *
from wand.image import *


## 함수 정의 부분
# 이미지 준비
def displayImage(img, width, height):
    global window, canvas, paper, photo, photo2, oriX, oriY

    '''
    # window 크기를 전체화면 크기로 지정
    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()
    '''
    window.geometry(str(width) + "x" + str(height))

    if canvas != None:
        canvas.destroy()

    canvas = Canvas(window, width=width, height=height)
    paper = PhotoImage(width=width, height=height)
    canvas.create_image((width / 2, height / 2), image=paper, state="normal")

    blob = img.make_blob(format='RGB')
    for i in range(0, width):
        for k in range(0, height):
            r = blob[(i * 3 * width) + (k * 3) + 0]
            g = blob[(i * 3 * width) + (k * 3) + 1]
            b = blob[(i * 3 * width) + (k * 3) + 2]
            paper.put("#%02x%02x%02x" % (r, g, b), (k, i))

    canvas.pack()

# 이미지 열기
def func_open() :
    global window, canvas, paper, photo, photo2, oriX, oriY

    redFp = askopenfilename(parent=window, filetypes=(("모든 그림 파일", "*.jpg;*.jpeg;*.bmp;*.png;*.tif;*.gif"), ("모든 파일", "*.*")))
    photo = Image(filename=redFp)

    oriX = photo.width
    oriY = photo.height

    photo2 = photo.clone()
    newX = photo2.width
    newY = photo2.height

    displayImage(photo2, newX, newY)

# 다른 이름으로 이미지 저장
def func_save_as() :
    global window, canvas, paper, photo, photo2, oriX, oriY  # 전역변수를 함수 안에서 사용하기 위해 선언

    if photo2 == None:
        return

    saveFp = asksaveasfile(parent=window, mode="w", defaultextension=".jpg", filetypes=(("JPG 파일", "*.jpg;*.jpeg"), ("모든 파일", "*.*") ))
    savePhoto = photo2.convert("jpg")
    savePhoto.save(filename=saveFp.name)

# 프로그램 종료
def func_exit() :
    window.quit()
    window.destroy()

def func_zoomin() :
    pass

def func_zoomout() :
    pass

def func_flip() :
    pass

def func_flop() :
    pass

def func_rotate() :
    pass

def func_brightness() :
    pass

def func_clear() :
    pass

def func_unclear() :
    pass

def func_bw() :
    pass

def func_border() :
    # https://www.geeksforgeeks.org/wand-border-function-python/
    pass

def func_revert() :
    pass

def func_deskew() :
    # https://www.geeksforgeeks.org/wand-deskew-function-python/
    pass

def func_distort() :
    # https://www.geeksforgeeks.org/python-distort-method-in-wand/
    pass

def func_crop() :
    pass

def func_blur() :
    pass

def func_gb() :
    pass

def func_sharpen() :
    pass

def func_mosaic() :
    pass

def func_sketch() :
    pass


# 변수 선언 부분
window,canvas, paper = None, None, None
photo, photo2 = None, None
oriX,oriY = 0,0


# 메인 코드 부분
window = Tk()
window.geometry("250x250")
'''
# 창 크기를 fullscreen으로 설정
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()
window.geometry("%dx%d" % (screenWidth, screenHeight))
'''

window.title("Simple Photoshop v.1.1")

mainMenu = Menu(window)
window.config(menu=mainMenu)

photo = PhotoImage()
pLabel = Label(window, image=photo)
pLabel.pack(expand=1, anchor=CENTER)
'''
photoWidth = photo.width()
photoHeight = photo.height()
pLabel.place(x=((screenWidth/2)-(photoWidth/2)), y=((screenHeight/2)-(photoHeight/2)))
print((screenHeight/2)-(photoHeight/2))
'''

# 메뉴 구성
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Open", command=func_open) # 이미지 열기
# fileMenu.add_command(label="Save", command=func_save) # 저장
fileMenu.add_command(label="Save As...", command=func_save_as) # 다른 이름으로 저장
fileMenu.add_command(label="Revert", command=func_revert) # 되돌리기
fileMenu.add_command(label="Exit", command=func_exit) # 프로그램 종료

editMenu = Menu(mainMenu)
transformMenu = Menu(editMenu)
flipMenu = Menu(editMenu)
mainMenu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Stroke",command=func_border)
editMenu.add_cascade(label="Transform", menu=transformMenu)
transformMenu.add_command(label="Rotate", command=func_rotate)
transformMenu.add_command(label="Remove Skew", command=func_deskew)
transformMenu.add_command(label="Distort", command=func_distort)
editMenu.add_cascade(label="Flip", menu=flipMenu)
flipMenu.add_command(label="Flip Horizontal", command=func_flip)
flipMenu.add_command(label="Flip Vertical", command=func_flop)

imageMenu = Menu(mainMenu)
mainMenu.add_cascade(label="Image", menu=imageMenu)
imageMenu.add_command(label="Greyscale", command=func_bw)
imageMenu.add_command(label="Brightness", command=func_brightness)
imageMenu.add_command(label="채도", command=func_clear)
imageMenu.add_command(label="Crop", command=func_crop)

filterMenu = Menu(mainMenu)
blurMenu = Menu(filterMenu)
noiseMenu = Menu(filterMenu)
mainMenu.add_cascade(label="Filter", menu=filterMenu)
filterMenu.add_cascade(label="Blur", menu=blurMenu)
blurMenu.add_command(label="Blur", command=func_blur)
blurMenu.add_command(label="Gaussian Blur", command=func_gb)
filterMenu.add_command(label="Sharpen", command=func_sharpen)
filterMenu.add_command(label="Mosaic", command=func_mosaic)
filterMenu.add_command(label="Sketch", command=func_sketch)

viewMenu = Menu(mainMenu)
mainMenu.add_cascade(label="View", menu=viewMenu)
viewMenu.add_command(label="Zoom In", command=func_zoomin)
viewMenu.add_command(label="Zoom out", command=func_zoomout)


'''
image1Menu.add_command(label="확대", command=func_zoomin)
image1Menu.add_command(label="축소", command=func_zoomout)
image1Menu.add_separator()
image1Menu.add_command(label="상하 반전", command=func_flip)
image1Menu.add_command(label="좌우 반전", command=func_flop)
image1Menu.add_command(label="회전", command=func_rotate)

image2Menu = Menu(mainMenu)
mainMenu.add_cascade(label="이미지 처리(2)", menu=image2Menu)
image2Menu.add_command(label="밝게", command=func_bright)
image2Menu.add_command(label="어둡게", command=func_dark)
image2Menu.add_separator()
image2Menu.add_command(label="선명하게", command=func_clear)
image2Menu.add_command(label="탁하게", command=func_unclear)
image2Menu.add_separator()
image2Menu.add_command(label="흑백이미지", command=func_bw)
'''

window.mainloop()

