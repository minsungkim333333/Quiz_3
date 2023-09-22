score=[90,45,64,9,17,29]
a=[]
for i in score :
    if i >= 71:
        a.append('A')
    elif i >= 41:
        a.append('B')
    elif i >= 11:
        a.append('C')
    else:
        a.append('D')
print(a)



