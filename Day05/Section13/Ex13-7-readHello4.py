file = open('hello.txt', 'rt')

line_list = file.readlines()
# print(line_list)
for line in line_list:
    print(line, end='')

file.close()
