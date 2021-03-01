def spirale_sprint(array, size, l=2, m=0, n=0, direction='r', res=[]):
    if len(res) == size:
        return res

    if direction == 'r':
        if n <= l:
            res.append(array[m][n])
            n += 1
        else:
            m += 1
            n -= 1
            direction = 'd'
    elif direction == 'd':
        if m < l:
            res.append(array[m][n])
            m += 1
        else:
            m -= 1
            n -= 1
            direction = 'l'
    elif direction == 'l':
        if n >= 0:
            res.append(array[m][n])
            n -= 1
        else:
            n = 0
            m -= 1
            direction = 'u'
    elif direction == 'u':
        if m > 0:
            res.append(array[m][n])
            m -= 1
        else:
            m += 1
            n = 1
            direction = 'r'

    return spirale_sprint(array, size, l, m, n, direction, res)


array = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]]

def recur(l):
    if not l: # keep going until list is empty
        return 0
    else:
        return recur(l[1:]) + len(l[0])

size = recur(array)
l = len(array[0])-1
print(spirale_sprint(array, size, l))
