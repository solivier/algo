A1 = [1, 4, 9]
A2 = [9, 9, 9]

''' Solution below work but it won't be asked during an interview '''
# s = ''.join(map(str, A))
# print(int(s) + 1)

'''
To solve this problem add 1 to the last value of the array,
if we have 10 set 0 and carry the + one to the left value
'''
def plus_one(A):
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i-1] += 1
    if A[0] == 10:
        A[0] = 1
        A.append(0)
    return A


print(plus_one(A1))
print(plus_one(A2))
