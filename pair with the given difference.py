i = 0
j = i+1
A = [5, 20, 3, 2, 50, 80]
for i in range(len(A)):
    for j in range(len(A)):
        if(A[i] - A[j]==78):
            print(A[i],A[j])
            
