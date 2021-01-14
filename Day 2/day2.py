a0 = [list of the first number, all numbers]
a1 = [list of the second number]
a2 = [the letter searched]
a3 = [the password itself]
b0 = []
for x in a0:
    b0.append(x-1)

b1 = []
for x in a1:
    b1.append(x-1)

i = 0
j = 0

while i < 1001:
    if a3[i].find(a2[i],b0[i],b0[i+1]) == b0[i] and a3[i].find(a2[i],b1[i],b1[i+1]) != b1[i]:
        j += 1
        print("iteration:",i,"correct (a0 true a1 false):")
        print(b0[i], b1[i], a2[i], a3[i])
        print(j)
        i += 1      
    elif a3[i].find(a2[i],b0[i],b0[i+1]) != b0[i] and a3[i].find(a2[i],b1[i],b1[i+1]) == b1[i]:
        j += 1
        print("iteration:",i,"correct (a0 false a1 true):")
        print(b0[i], b1[i], a2[i], a3[i])
        print(j)
        i += 1
    elif a3[i].find(a2[i],b0[i],b0[i+1]) == b0[i] and a3[i].find(a2[i],b1[i],b1[i+1]) == b1[i]:
        print("iteration:",i,"incorrect (all true):")
        print(b0[i], b1[i], a2[i], a3[i])
        print(j)
        i += 1
    else:
        print("iteration:",i,"incorrect (all false):")
        print(b0[i], b1[i], a2[i], a3[i])
        print(j)
        i += 1