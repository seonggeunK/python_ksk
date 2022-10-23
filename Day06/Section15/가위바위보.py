'''가위바위보
'''

import random

select = ["가위", "바위", "보"]
ai = random.choice(select)


while True:
    user = input("가위 바위 보 중 하나를 선택하세요")
    if user in select:
        break
    print("잘못된 입력입니다. 다시 입력하세요.")

print("컴퓨터는 {}를 냈습니다.".format(ai))
print("당신은 {}를 냈습니다.".format(user))

if user == "가위" and ai == "보" or \
        user == "바위" and ai == "가위" or \
        user == "보" and ai == "바위":
    print("당신이 이겼습니다.")

elif user == "가위" and ai == "가위" or \
    user == "바위" and ai == "바위" or \
    user == "보" and ai == "보":
    print("무승부 입니다.")

else:
    print("당신이 졌습니다.")

# elif:
#     print("당신이 졌습니다.")
