# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
T= int(input())
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
for i in range(T):
    #각 테스트 케이스마다 "Case #x: A + B = C" 형식으로 출력 (C는 A+B이다)
    A,B =map(int, input().split())
    print(f"Case #{i+1}: {A} + {B} = {A+B}")