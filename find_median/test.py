# Enter your code here. Read input from STDIN. Print output to STDOUT
import heapq

minHeap = []
maxHeap = []

N = int(input())
first = float(input())
heapq.heappush(minHeap, first)
print(first)
for i in range(2, N + 1):
    cur = float(input())
    if cur > minHeap[0]:
        heapq.heappush(minHeap, cur)
    else:
        heapq.heappush(maxHeap, -cur)
    if len(maxHeap) - len(minHeap) > 1:
        maxs = heapq.heappop(maxHeap)
        heapq.heappush(minHeap, -maxs)
    elif len(minHeap) - len(maxHeap) > 1:
        mins = heapq.heappop(minHeap)
        heapq.heappush(maxHeap, -mins)

    # print "min", minHeap
    # print "max", maxHeap
    if i % 2 == 1:
        if len(minHeap) > len(maxHeap):
            print(minHeap[0])
        else:
            print(-maxHeap[0])
    else:
        print((minHeap[0] - maxHeap[0]) / 2)
