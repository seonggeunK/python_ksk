while True:
        id = input('아이디를 입력하세요 (3글자 이상) >>>')
        ch_count = 0
        num_count = 0

        for ch in id:
            if ch.isalpha():
                ch_count += 1
            elif ch.isnumeric():
                num_count += 1

        if ch_count > 0 and num_count > 0 and len(id) > 2:
            print('가능한 아이디 입니다.')
            break
        else:
            print('3글자 이상 입력해 주세요.')

while True:
    pwd = input('패쓰워드를 입력하세요(영문 숫자 포함 8자이상)>>>')
    ch_count = 0
    num_count = 0

    for ch in pwd:
        if ch.isalpha():
            ch_count += 1
        elif ch.isnumeric():
            num_count += 1
    # isContainAlpah
    # isContainNumeric
    # for ch in pwd:
    # if ch.isalpha():
    #     isContainAlpha = True
    # elif ch.isnumeric():
    #     isContainNumric = True
    if ch_count > 0 and num_count > 0 and len(pwd) > 7:
        print('사용가능한 패쓰워드입니다. >>>')
        pwd2 = input('패쓰워드 한번 더 입력하세요 >>>')

    if pwd == pwd2:
             print('회원가입 완료!!')
             break
    elif  pwd != pwd2:
             print('일치하지 않습니다. 다시 입력해 주세요.')
    else:
        print('영문 숫자 포함 8자이상 입력해 주세요.')

# [로그인]
while True:
    lg1 = input('아이디를 입력하세요>>>')
    if id == lg1:
           break
    else:
        print('아이디가 일치하지않습니다.')

while True:

    lg2 = input('비밀번호를 입력하세요>>>')
    if lg2 == pwd:
        print('로그인 완료!!')
        break
    else:
         print('패쓰워드가 일치하지 않습니다.')

