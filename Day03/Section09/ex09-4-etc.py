'''
내장함수 보충
'''

# format()
result = format(10000) # str(10000)과 같다 문자열
print(result)
result = format(10000, ',') # 천단위 쉼표
print(result)

# abs() 절대값
result = abs(10)
print(result)
result = abs(-10)
print(result)

# max() 최대값 반환
# min() 최소값 반환
result = max(1, 10)
print(result)
Li = [5, 3, 4, 2, 1]
result = max(Li)
print(result)
result = min(Li)
print(result)

# pow() 거듭제곱 함수
result = pow(10, 2)
print(result)

# sorted() 함수
my_li = [5, 6, 3, 4, 1, 2]
result = sorted(my_li)
print(result)
result = sorted(my_li, reverse=True)
print(result)

names = ['james', 'emily', 'amanda']
scores = [60, 70, 80]
for student in zip(names, scores): #zip은 2개를 묶어줌
    print(student)

names = ['james', 'emily', 'amanda']
scores = [60, 70, 80]
for name, score in zip(names, scores): #zip은 2개를 묶어줌
    print('{}의 점수는 {}점 입니다.'.format(name, score))