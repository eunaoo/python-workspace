# 올해 년도와 태어난 년도를 구하여 나이 계산 프로그램
yearToday=int(input('올해의 년도를 4자리로 입력하세요? '))
yearBirth=int(input('당신이 태어난 년도를 4자리로 입력하세요? '))
print('당신의 나이는 {}살 입니다.'.format(yearToday-yearBirth+1))

print('\n')

#600kg제한의 엘베, 2개의 물건 무게를 실수로 입력 받아, 현재 더 적재가능한 무게 출력
weightMax=600
weight1=float(input('첫 번째 물건의 무게를 입력 하시오? '))
weight2=float(input('두 번째 물건의 무게를 입력 하시오? '))
print('\n현재 엘리베이터에 허용 무게는 {}kg입니다.'.format(weightMax-(weight1+weight2)))
