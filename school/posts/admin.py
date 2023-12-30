def Good_pairs(nums):
    ans=(i,j)
    for j in nums:
        for i in j:
            if nums[i] == nums[j]:
                return ans
            
        
        
    
    
nums=[1,2,3,1,1,3]    
result=Good_pairs(nums)
print(result)
        
            
            
    



     