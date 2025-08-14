def threeSum(self, nums):
    """
    Find all unique triplets that sum to zero.
    
    Args:
        nums: List of integers
        
    Returns:
        List[List[int]]: All unique triplets [a,b,c] where a+b+c=0
        
    Time: O(n²), Space: O(1) excluding output
    """
    # Sort the array to enable two-pointer technique and make duplicate handling easier
    nums.sort()
    result = []
    
    # Iterate through array, fixing the first element of each triplet
    # Stop at len(nums)-2 because we need at least 2 more elements for left/right pointers
    for i in range(len(nums) - 2):
        # Skip duplicate values for the first element to avoid duplicate triplets
        # Only skip if i > 0 to avoid skipping the very first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # For current nums[i], we need to find two numbers that sum to -nums[i]
        # This transforms the problem into a two-sum problem
        target = -nums[i]
        
        # Initialize two pointers for the remaining subarray
        left, right = i + 1, len(nums) - 1
        
        # Use two-pointer technique to find pairs that sum to target
        while left < right:
            current_sum = nums[left] + nums[right]
            
            # Found a valid triplet: nums[i] + nums[left] + nums[right] = 0
            if current_sum == target:
                # Add the triplet to results
                result.append([nums[i], nums[left], nums[right]])

                # Skip duplicate values from the left side
                # Move left pointer past all duplicate values
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                
                # Skip duplicate values from the right side
                # Move right pointer past all duplicate values
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                # Move both pointers inward after processing duplicates
                left += 1
                right -= 1

            # Current sum is less than target, need a larger sum
            elif current_sum < target:
                left += 1
            # Current sum is greater than target, need a smaller sum
            else:
                right -= 1
    
    return result
