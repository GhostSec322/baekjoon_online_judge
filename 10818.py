#N개의 정수가 주어진다

# 첫째 줄에 정수의 개수 N 
N = int(input())

# N개의 정수를 공백으로 구분해서 주어진다
ints = list(map(int, input().split()))


# 출력
# 첫째 줄에 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 출력한다.
print(min(ints),max(ints))