import random

def step1():
    print('싸움이 시작됩니다')
    print('1. 주먹으로 때린다\n2. 발로 찬다\n3. 머리로 박는다\n4. 도구를 쓴다')
    num = input("선택: ")
    if num == '1':
        print("몬스터가 데미지를 입었다 또는 피했다")
    elif num == '2':
        print("발로차 소농민 골~")
    elif num == '4':
        print("도구 사용 메뉴")
        item = itemlist()  # 랜덤하게 아이템을 전달해주는 함수
        print(f"{item}을 사용했습니다.")

def step2():
    print("도망간다")

def itemlist():
    # print("1.커져라총 2.공기포 3.대나무헬리콥터 4.투명망또")
    l = ['커져라총', '공기포', '대나무헬리콥터', '투명망또']
    # print(random.choice(l)) #a
    return random.choice(l)

