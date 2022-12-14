'''내장 데이터 유형
프로그래밍에서 데이터 유형
변수는 다른 유형의 데이터를 저장할 수 있으며
다른 유형은 다른작업을 수행할 수 있다.
Python에는 이런한 범주에 기본적으로 다음 데이터 유형이 내장되어 있다.

덱스트 유형 : str
숫자 유형 : int, float, complex
시퀀스 유형 : list, tuple, rage
매핑 유형 : dict
세트 유형 : set, frozenset
바이너리 유형 : bytes, bytearray, memoryview
없음 유형 : NoneType
 '''

# str
x = "Hello World"
print(type(x))
# int
x = 20
print(type(x))
# float
x = 20.5
print(type(x))
# complex
x = 1j
print(type(x))
# list
x =["피카츄", "라이츄", "파이리"]
print(type(x))
# tuple
x =["피카츄", "라이츄", "파이리"]
print(type(x))
# range
x = range(6)
print(type(x))
# dict
x = {"name" : "피카츄", "기술" : "백만볼트!!!"}
print(type(x))
# set
x = {"피카츄", "라이츄", "파이리"}
print(type(x))
# frozenset
x = frozenset({"피카츄", "라이츄", "파이리"})
print(type(x))
# bool
x = True

'''
      *
     ***
    *****
   *******
  *********      
     | |
'''
a, b, c, d, e, f = "      *", "     ***", "    *****", "   *******", "  *********      ", "     | |"
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)