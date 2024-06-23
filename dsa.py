A = [3,34,[5,3],6]
print(A)
for i in A:
    print(i)
    if A[1] == i:
        A[1] = 23
    print(A)
print("done")
