def removeDuplicates(self, nums):
    """
    Remove duplicates from sorted array in-place.
    
    Args:
        nums: Sorted list of integers
        
    Returns:
        int: Length of array after removing duplicates
        
    Time: O(n), Space: O(1)
    """
    # Handle edge case of empty array
    if not nums:
        return 0
    
    # Slow pointer tracks the position for next unique element
    # Initialize at 0 since first element is always unique
    slow = 0
    
    # Fast pointer scans through array starting from index 1
    for fast in range(1, len(nums)):
        # Found a new unique element (different from element at slow)
        if nums[slow] != nums[fast]:
            # Move slow pointer to next position for unique elements
            slow += 1
            # Place the new unique element at the slow position
            nums[slow] = nums[fast]
    
    # Return length of unique elements array
    # slow is 0-indexed, so add 1 to get count
    return slow + 1
