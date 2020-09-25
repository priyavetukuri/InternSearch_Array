Arr = [1,0,2,0,1,0,3,1,0,2]
n = len(Arr)
water = 0
rain_trap = 0
left = n*[0]
right = n*[0]
left[0] = Arr[0]
left_max = Arr[0]
for i in range(0,n):
    if(left_max < Arr[i]):
        left_max = Arr[i]
        left[i] = left_max
    else:
         left[i] = left_max
right_max = Arr[-1]
for i in range(n - 1,-1,-1):
    if(right_max < Arr[i]):
        right_max = Arr[i]
        right[i] = right_max
    else:
         right[i] = right_max
for i in range(0,n):
    water = water+min(left[i],right[i]) - Arr[i]
    rain_trap = water
print(rain_trap)

        
        
