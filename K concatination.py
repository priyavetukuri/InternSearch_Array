Arr1 = [1,2]
Arr2 = []
k = 3
i = 0
j = 0
x = 0
for i in range(k):
    for j in range(len(Arr1)):
        Arr2.append(Arr1[j])
        x = Arr2
print(x)
Maximum = Arr2[0]
sum = Arr2[0]
for i in range(1,len(Arr2)):
    sum = sum+Arr2[i]
    sum = max(sum,Arr2[i])
    Maximum = max(Maximum,sum)
print(Maximum)
        
    


