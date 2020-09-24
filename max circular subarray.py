Arr = [8, -8, 9, -9, 10, -11, 12]
n = len(Arr)
x = 0
Maximum = Arr[0]
sum = Arr[0]
for i in range(1,n):
    sum = sum+Arr[i]
    sum = max(sum,Arr[i])
    Maximum = max(Maximum,sum)
x = Maximum
max_circular = 0
for i in range(0,n):
    max_circular+=Arr[i]
    Arr[i] = -Arr[i]
max_circular = max_circular+Maximum
if(max_circular>x):
    print(max_circular)
else:
    print(x)
    


