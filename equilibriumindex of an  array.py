arr=[-7,1,5,2,-4,3,0]
n = len(arr)
leftsum=0
rightsum=0
x=int(n/2)
for i in range(0,x):
    leftsum=leftsum+arr[i]
for j in range(x+1,n):
    rightsum=rightsum+arr[j]
if leftsum==rightsum:
    print(x)
else:
    print(-1)
