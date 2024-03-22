#첫째 줄부터 열번째 줄 까지 숫자가 한 줄에 하나씩 주어진다.
input_num= []
for _ in range(10):
    input_num .append( int(input()))

# 출력
# 첫째 줄에, 42로 나누었을 때, 서로 다른 나머지가 몇 개 있는지 출력한다.
res =[]
for i in range(10):
    res.append(input_num[i]%42)

print(len(set(res)))