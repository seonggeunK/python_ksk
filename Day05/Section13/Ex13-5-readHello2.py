file = open('hello.txt', 'rt')

while True:
    str =file.read(5)
    # print(str)#5개씩 나오는지 확인하려면 print 한번찍어보자
    if not str:
        break
    print(str, end='')

file.close()