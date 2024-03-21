# 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.
N,X= map(int,input().split())
#둘째 줄에 수열 A를 이루는 정수 N개가 주어진다
A = map(int,input().split())
res =  [v for v in A if v < X] ## list comprehension 이용
# 결과 출력
for num in res:
    print(num, end=' ')