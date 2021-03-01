'''
Assign tasks to workers so that the time it takes to complete all the tasks is minimized given a count of workers
and an array where each element indicates the duration of a task.

We wish to determine the optimal way in which to assign tasks to some workers.
Each worker must work on exactly two tasks.
Tasks are independent of each other, and each task takes a certain amount of time.
'''


A = [6, 3, 2, 7, 5, 5]

A = sorted(A)

for i in range(len(A)//2):
    print(A[i], A[~i])

'''
Explanation #
Yes, the implementation was that simple! After sorting the array using sorted on line 3,
the for loop on line 5 iterates for half the length of the array and prints out the pairs using indexing.
So ~i on line 6 is the bitwise complement operator which puts a negative sign in front of i.
Thus, the negative numbers as indexes mean that you count from the right of the array instead of the left.
So, A[-1] refers to the last element, A[-2] is the second-last, and so on. In this way,
we are able to pair the numbers from the beginning of the array to the end of the array.
'''