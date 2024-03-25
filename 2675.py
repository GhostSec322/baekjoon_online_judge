T = int(input())
for i in range(T):
    Num, STR = input().split()
    print(''.join([STR[j] * int(Num) for j in range(len(STR))]))
