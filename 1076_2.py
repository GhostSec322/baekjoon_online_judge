color=['black','brown','red','orange','yellow','green','blue','violet','grey','white']		
input_color_1 = input()
input_color_2 = input()
input_color_3 = input()
res= (color.index(input_color_1)*10+color.index(input_color_2))*(pow(10,color.index(input_color_3)))
print(res)