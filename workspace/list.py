# output - (676,[43, 54, 91, 90])

def A_subset(A, n):
    sum = 0
    for x in A:
        sum += x
    return (sum, A[:n])

n = 4
A = [43,54,91,90,78,76,69,60,79,36]
print(A_subset(A,n))

