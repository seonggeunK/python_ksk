'''
[회원가입]
아이디를 입력하세요 (3글자 이상) >>>
> 3글자 이상 입력해 주세요.

아이디를 입력하세요 (3글자 이상) >>>

패쓰워드를 입력하세요(영문 숫자 포함 8자이상) >>>
> 영문 숫자 포함 8자이상 입력해 주세요.

패쓰워드 한번 더 입력하세요 >>>
> 일치하지 않습니다. 다시 입력해 주세요.

패쓰워드를 입력하세요(영문 숫자 포함 8자이상) >>>

패쓰워드 한번 더 입력하세요 >>>

회원가입 완료!!

[로그인]
아이디를 입력하세요 >>>
> 아이디가 일치하지 않습니다.

아이디를 입력하세요 >>>

패쓰워드를 입력하세요 >>>
> 패쓰워드가 일치하지 않습니다.

패쓰워드를 입력하세요 >>>

로그인 완료!!
'''
id = input('아이디를 입력하세요(3글자이상)')
id = qwe123
ch_count = 0
num_count = 0
for ch in id:
    if ch.isalpha():
        ch_count += 1
    elif ch.isnumeric():
        num_count += 1

if ch_count > 2 and num_count > 0:
    print('가능한 아이디 입니다.')
else:
    print('3글자 이상 입력해 주세요.')

# pwd = input('비밀번호를 입력하세요 >>> ')
pwd = 'abcdefg10'
ch_count = 0
num_count = 0

for ch in pwd:
    if ch.isalpha():
        ch_count += 1
    elif ch.isnumeric():
        num_count += 1

if ch_count > 0 and num_count > 0:
    print('가능한 비밀번호 입니다.')
else:
    print('불가능한 비밀번호 입니다.')