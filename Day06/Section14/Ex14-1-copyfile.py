'''
파일복사
    원본 -> 변수(Memory) -> 복사본


'''
buffer_size = 1024 #1024byte로 1KB를 의미합니다.
with open('hello.txt', 'rb') as source:
    with open('hello2.txt', 'wb') as copy:
        while True:
            buffer = source.read(buffer_size)
            if not buffer: #if buffer == '':
                break
            copy.write(buffer)
print('hello2.txt 파일이 복사 되었습니다.')