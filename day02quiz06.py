# 다음과 같은 방법으로 표준 체중을 구할 수 있다. 표준체중=(현재 키-100)*0.9
# 비만도 비율은 다음과 같은 방법으로 구할 수 있다. 비만도(%)=(현재체중/표준체중)*100
heigh=int(input('키를 입력하세요? '))
myWeight=float(input('현재 체중을 입력하세요?'))

commonWeight=(heigh-100)*0.9
overWeight=(myWeight/commonWeight)*100

print('표준 체중은 {}이고 비만도는 {}% 입니다.'.format(commonWeight, round(overWeight,2)))







