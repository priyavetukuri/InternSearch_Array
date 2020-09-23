Arr = [1,2,-1,3]
Maximum = Arr[0]
sum = Arr[0]
for i in range(1,len(Arr)):
    sum = sum+Arr[i]
    sum = max(sum,Arr[i])
    Maximum = max(Maximum,sum)
print(Maximum)

