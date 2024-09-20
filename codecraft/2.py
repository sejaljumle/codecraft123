def three_sum(nums):
    nums.sort()  # Sort the array to help with the two-pointer technique
    triplets = []
    
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            # Skip the same element to avoid duplicate triplets
            continue
        
        left, right = i + 1, len(nums) - 1
        
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            
            if total == 0:
                triplets.append([nums[i], nums[left], nums[right]])
                
                # Move the left pointer to the right, skipping duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # Move the right pointer to the left, skipping duplicates
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1
                
            elif total < 0:
                # If the total is less than 0, move the left pointer to increase the sum
                left += 1
            else:
                # If the total is greater than 0, move the right pointer to decrease the sum
                right -= 1
    
    return triplets

# Test the function with a sample input
nums = [-1, 0, 1, 2, -1, -4]
result = three_sum(nums)
print(result)