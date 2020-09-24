i = 0
j = i+1
A = [1, 4, 20, 3, 10, 5]
for i in range(len(A)):
    for j in range(len(A)):
        if(A[i] + A[j]==23):
            print(i,j)
            
