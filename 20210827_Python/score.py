## 학점 산출 프로그램

# 입력값이 0~100까지만 받을 것 --> 음수나 100초과 --> 다시 입력하라는 문구 출력
# 입력값이 0~100 사이에 있을 때
#   90~100 --> A
#   80~89 --> B
#   70~79 --> C
#   60~69 --> D
#   60 미만 --> F
#   종료가 될 때까지 반복

while 1:

    score=int(input("성적을 입력하세요(0~100) : "))


    # score가 음수와 100 초과 수가 아닐 때까지 반복
    if score < 0 or score > 100:
        while 1:
            if score > 0 and score <= 100:
                break
            else:
                score=int(input("성적을 다시 입력하세요(0~100) : "))

    '''            

    # 조건문 없이 while문에 조건을 쓰는 방법
    while score < 0 or score > 100:
        score=int(input("성적을 다시 입력하세요(0~100) : "))
    '''
        
    
    '''
    # 음수 이후에 100을 초과하는 수 입력 --> 오류발생
    if score < 0 or score > 100:
        score=int(input("성적을 다시 입력하세요(0~100) : "))
    '''   
        
    if score >= 90 :
         print("축하합니다. A입니다.")
    elif score >= 80 :
         print("축하합니다. B입니다.")
    elif score >= 70 :
         print("축하합니다. C입니다.")
    elif score >= 60 :
         print("축하합니다. D입니다.")
    else :
         print("축하합니다. F입니다.")
