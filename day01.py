#print( 20+ 200 )
#print( '안녕하세요' )
#print 괄호안의 내용을 출력하는 기능
print( 100 ); print( 2000 )
# '," :한줄의 문자열 처리
# ''', """ : 여러줄의 문자열 처리, 3개씩 써야함
'''
ESCAPE 문자
- 문자열 안에서 특수한 동작을 해주는 것
- \n : 엔터값과 비슷하다
- \t : tab크기만큼 커서를 오른쪽으로 이동
       (8칸 확보 후 사용하고 남은 칸만큼 띄어놓음)
- \" : "(큰따옴표) 출력
- \' : '(작은 따옴표) 출력
- \\ : \
'''
print( "안\n녕\n하\n세\n요" )
print( 'Have \ta \tgood \ttime' )
print( '1234567\t1\t12345678\t55' )

print(" '안녕' ''''' " )
print(" \"안녕\" " )
print(' ""안녕"" ' )
print(' \'안녕\' ' )
print( '\\' )
print( "c:\0.공유\ " )
print( "c:\\0.공유\ " )
print( "c:/0.공유/ " )

print( '안녕' , 123+100 )

print( '12 + 54 = ', 12+54, ' 입니다' )
print( f'12+54={12+54} 입니다' )   #f중괄호 안은 숫자로 연산

print( '12+54={} 입니다' .format(12+54) )  #format다음값이 중괄호{}안에 들어감

print( '{} + {} = {}' .format(10,20,30) )   #차례대로 {}에 들어감
print( '{2} + {1} = {0}' .format(10,20,30) )    #순서 지정 가능

print( "{:,}" .format(100000000000000) )    # :, 

print("{:<10}왼쪽정렬{:0<10}" .format('안녕', '하세') )
print("{:>10}오른쪽정렬{:8>10}" .format('안녕', '하세') )
print("{:^10}가운데정렬{:8^10}" .format('안녕', '하세') )
    # :<10 열칸 확보하고 왼쪽 정렬
    # :>10 열칸 확보하고 오른쪽 정렬
    # :^10 열칸 확보하고 가운데 정렬
    # :0<10 열칸 확보하고 빈공간은 0으로 채움
    



'''
변수
- 데이터를 저장하기 위한 공간
- 데이터는 언제든지 변경 가능하다
변수 작명 규칙
- 의미를 부여해서 만든다
- 키워드(예약어)는 사용할 수 없다
- 한글로도 만들 수 있으나 영어로 만드세요
'''

num = 33
print(num, "입니다.")
print(f'저장값 {num} 입니다.')
print('저장값 {} 입니다.' .format(num))

num = 5
print('변경 후 :', num)

num = num + 100
print('연산 후 :', num)    #105

num1=5
num2=10
n_sum = num1+num2 #15
print('n1:', num1) #5
print('n2:', num2) #10
print('sum:', n_sum) #15
print(sum([1,2,3,4,5,6]))















