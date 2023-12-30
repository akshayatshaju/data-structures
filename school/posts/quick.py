def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[0]
    left=[]
    right=[]
    for x in arr[1:]:
        if x in arr[1:]:
            if x<pivot:
                left.append(x)
            else:
                right.append(x)
    return quick_sort(left)+[pivot]+quick_sort(right)

my_list=[64,34,56,22,24,74,12,89]
sorted_list=quick_sort(my_list)
print(sorted_list)             