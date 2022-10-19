flt=123.567
print(flt)

#round : 소숫점이하를 반올림
print('round(flt) : ', round(flt))
print('round(flt,1) : ', round(flt,1))
print('round(flt,2) : ', round(flt,2))

# day02quiz01.py

#문자끼리 연산 가능
st='py'; st1='thon'
print(st+st1)

# day02quiz02.py

#자료형 : type명령어에 입력하면 알려줌
num=100
st='안녕하세요'
print(type(num))    # int, integer
print(type(1.123))  # float
print(type(st))     # str, string

print(type(str(num)))   # str(num) : num을 str으로 형변환, int->str
print('안녕하세요' + str(num))

# day02quiz03.py

# input 으로 입력받기
num=input('숫자 입력 : ')
print('입력 받은 수 : ',num)

print("두 수의 합을 구해 줍니다!!!")
n1=input('수 입력 : ')     #5
n2=input('수 입력 : ')     #6
n3=n1+n2
print('두 수의 합 : ', n3)  #=>56 으로 나옴 -> str상태, int로 변환 필요
# day02quiz04.py 에서 풀이함.

# input으로 받은 값은 str, 형변환 해줘야함.
name = input('이름 입력 : ')
age = int(input('나이 입력 : '))
flt = float(input('실수 입력 : '))
print(f'{name}\t, type:{type(name)}')
print(f'{age}\t, type:{type(age)}')
print(f'{flt}\t, type:{type(flt)}')

# day02quiz05.py







