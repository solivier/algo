from statistics import median


def find_median(lst):
    if len(lst) % 2 == 1:
        return lst[len(lst)//2]
    else:
        return (lst[len(lst)//2] + lst[len(lst)//2 - 1])/2


my_list = [12, 23, 235, 1255, 6, 9, 0, 33, 76, 332, 87, 99]

print(find_median(sorted(my_list)))
print(median(my_list))
print(sorted(my_list))
