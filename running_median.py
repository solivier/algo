import heapq

L, H = [], []


def running_median(lst):
    result = []
    for a in lst:
        if not H:
            heapq.heappush(H, a)
        else:
            if len(H) > len(L):
                if H[0] < a:
                    b = heapq.heappushpop(H, a)
                    heapq.heappush(L, -b)
                else:
                    heapq.heappush(L, -a)
            else:
                if -L[0] > a:
                    b = -heapq.heappushpop(L, -a)
                    heapq.heappush(H, b)
                else:
                    heapq.heappush(H, a)

        if len(H) > len(L):
            result.append("%.1f" % H[0])
        else:
            result.append("%.1f" % ((H[0] - L[0]) / 2))

    return result


if __name__ == '__main__':

    a_count = int(input())

    a = []

    for _ in range(a_count):
        a_item = int(input())
        a.append(a_item)

    result = running_median(a)
    print(result)


# input
#6
#12
#4
#5
#3
#8
#7

# EXPECTED RESULT
#12.0
#8.0
#5.0
#4.5
#5.0
#6.0
