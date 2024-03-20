T = int(input())
Computer = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for _ in range(T):
    a, b = map(int, input().split())
    data = pow(a % 10, b, 10)
    print(Computer[data - 1])