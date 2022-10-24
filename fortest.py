# 입력받은 단수로 구구단 출력하기
dan = 5  # input으로 바꿔서 해보기
for i in range(9):
    dab = dan * (i+1)
    print(f"{dan} x {(i+1)} = {dab}")

# 헬로 월드를 10번 출력 해보기
print("hello world")
print("hello world")
print("hello world")
'...10번'
for i in range(10):
    print("hello world")
# 헬로 월드를 앞에 숫자를 붙여서 카운팅
'1. hello world'
'2. hello world'
'3. hello world'
'... 몇번'
for i in range(10):
    print(f"{i+1}. hello world")
# 조건문까지 합쳐서
# 10번찍어서 안넘어가는 나무 없다
# 1번찍고 ~ 2번찍고~ ...
# 만약 10번을 찍었을때 
# 나무가 넘어 간다~ 출력
for i in range(10):
    print(f"{i+1}찍고~")
    if i == 9:
        print('나무가 넘어 간다~')


