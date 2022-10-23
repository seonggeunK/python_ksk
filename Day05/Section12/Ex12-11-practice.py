import random
import time

pot = [n for n in range(1, 46)]
jackpot = []

for n in range(1, 7):
    random.shuffle(pot)
    pick = pot.pop()
    print('{}번째 당첨번호는 ()입니다.'.format.pick))
    jackpot.append(pick)
    time.sleep(2)

jackpot.sort() #sort 차순 정렬
print('이번 당청번호는 {} 입니다'.format(jackpot))