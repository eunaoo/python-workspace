#학생 이름과 국어,영어,수학 점수를 입력받아 출력하시오
name=input('학생 이름 : ')
korScore=int(input('국어 점수 : '))
engScore=int(input('영어 점수 : '))
mathScore=int(input('수학 점수 : '))
totalScore=korScore+engScore+mathScore

print('\n{:=^46}'.format('학생 정보'))        # {:=^50} : 50칸 확보, 가운데 정렬, 남은 자리 =로 채움
print('이름\t국어\t영어\t수학\t합계\t평균')
print('-'*50)
print('{}\t{}\t{}\t{}\t{}\t{}'.format(name, korScore, engScore, mathScore, totalScore, round(totalScore/3, 2)))




