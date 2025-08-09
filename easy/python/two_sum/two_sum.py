def twoSum(self, nums, target):
    """
    Find indices of two numbers that add up to target.
    
    Args:
        nums: List of integers
        target: Target sum
        
    Returns:
        List[int]: Indices [i, j] where nums[i] + nums[j] = target
        
    Time: O(n), Space: O(n)
    """
    seen = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], index]
        seen[num] = index
