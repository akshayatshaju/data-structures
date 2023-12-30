def bubble(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                
my_list=[64,34,56,22,24,74,12,89]
bubble(my_list)
print(my_list)                