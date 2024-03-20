# # 전자 제품에는 저항이 들어간다. 저항은 색 3개를 이용해서 그 저항이 몇 옴인지 나타낸다.
#  처음 색 2개는 저항의 값이고, 마지막 색은 곱해야 하는 값이다.
# 저항의 값은 다음 표를 이용해서 구한다.
table ={
    "black":[0,1],
    "brown":[1,10],
    "red":[2,100],
    "orange":[3,1000],
    "yellow":[4,10000],
    "green":[5,100000],
    "blue":[6,1000000],
    "violet":[7,10000000],
    "grey":[8,100000000],
    "white":[9,1000000000]
}
color_1= input()
result= table[color_1][0]*10
color_2 = input()
result += table[color_2][0]
color_3 = input()
result*=table[color_3][1]
print(result)