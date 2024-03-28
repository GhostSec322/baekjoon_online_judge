input_Pis= list(map(int, input().split()))
pis=[1,1,2,2,2,8]
res=[]
for i in range(len(pis)):
    res.append(pis[i]-input_Pis[i])

print(' '.join(map(str,res)))