#파이썬,c언어,Java 3과목의 점수를 저장하고 합계와 평균을 구하는 프로그램 작성
python=90
c=85
java=70
sum_=python+c+java
print(f'파이썬 : {python}점, c언어 : {c}점, Java : {java}점 입니다.')
print('점수의 합계 : {} \n점수의 평균 : {}'.format(sum_, round((sum_)/3,2) ))

print('\n')

#11개의 지하철 역을 지나왔다. 출발역에서 도착역까지 37분 걸림, 한역 지나는데 걸리는 시간은?
time=37
station=11
print('한역을 지나는데 걸린 시간은 ', round(time/station,2),'분 입니다.')

print('\n')

#호텔 한 층의 높이는 260cm,  14개의 층을 쓰고 있으며 1층은 500.23cm라면 이 건물의 높이는 총 몇 m?
floor_h = 260
first_h = 500.23
floor_n = 13
print('이 건물의 높이는 ', round((first_h+floor_h*floor_n)/100,3), 'm 입니다.')
