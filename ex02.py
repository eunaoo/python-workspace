print( '12 + 54 = ', 12+54, ' 입니다' )
print( '268 - 42 = ', 268-42, ' 입니다' )
print( '2 * 23 = ', 2*23, ' 입니다' )
print( '120 / 3 = ', 120/3, ' 입니다' )

print( f'12 + 54 = {12+54} 입니다' )   #f중괄호 안은 숫자로 연산

print( '12 + 54 = {} 입니다' .format(12+54) )  #format다음값이 중괄호{}안에 들어감

print( '{} + {} = {} 입니다' .format(12,54,12+54) )   #차례대로 {}에 들어감
print( '{1} + {2} = {0} 입니다' .format(12+54,12,54) )    #순서 지정 가능
