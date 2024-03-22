#첫째 줄에 N (1 ≤ N ≤ 100)과 M (1 ≤ M ≤ 100)이 주어진다.

N,M= map(int,input().split())
#바구니에는 1번부터 N번까지 번호가 순서대로 적혀져 있다. 
basket= [i+1 for i in range(N)]

for _ in range(M):
    i,j= map(int,input().split())
    basket[i-1:j] = reversed(basket[i-1:j])
 
print(" ".join(map(str , basket)))

