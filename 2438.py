#첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
N= int(input())
#첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.
for i in range(N):
    print("*"*int(i+1))