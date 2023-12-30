def selction_sort(arr):
    n = len(arr)
    for i in range(n-1):
        
        min_idx = i
        
        for j in range(i+1,n):
            if arr[j]< arr[min_idx]:
                min_idx = j
                
        arr[i],arr[min_idx]= arr[min_idx],arr[i]
        
my_list=[5,8,7,41,2,69,45]
selction_sort(my_list)
print(my_list)                