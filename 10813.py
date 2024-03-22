basket =[]

#첫째 줄에 N (1 ≤ N ≤ 100)과 M (1 ≤ M ≤ 100)이 주어진다.
N,M = map(int,input().split())
# 1번부터 N번까지 번호가 매겨져 있다. 바구니에는 공이 1개씩 들어있고, 처음에는 바구니에 적혀있는 번호와 같은 번호가 적힌 공이 들어있다.
basket=[i+1 for i in range(N)]
#M개의 줄에 걸쳐서 공을 교환할 방법이 주어진다
for i in range(M):
    # 방법은 두 정수 i j로 이루어져 있으며, i번 바구니와 j번 바구니에 들어있는 공을 교환한다는 뜻
    i,j =map(int,input().split())
    basket[i-1],basket[j-1]=basket[j-1],basket[i-1]

print(' '.join(map(str,basket)))