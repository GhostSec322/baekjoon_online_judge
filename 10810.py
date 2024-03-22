basket = []
# 입력
# 첫째 줄에 N (1 ≤ N ≤ 100)과 M (1 ≤ M ≤ 100)이 주어진다.
N,M= map(int , input().split())
basket = [0 for _ in range(N)]

# 방법은 세 정수 i j k로 이루어져 있으며, i번 바구니부터 j번 바구니까지에 k번 번호가 적혀져 있는 공을 넣는다는 뜻
for _ in range(M):
    i,j,k= map(int, input().split())
    basket[i-1:j] = [k] * (j - i + 1)

print(' '.join(map(str,basket)))