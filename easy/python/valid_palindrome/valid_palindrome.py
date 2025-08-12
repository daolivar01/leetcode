def isPalindrome(self, s):
    """
    Check if string is palindrome (alphanumeric only, case-insensitive).
    
    Args:
        s: Input string
        
    Returns:
        bool: True if palindrome, False otherwise
        
    Time: O(n), Space: O(1)
    """
    # Initialize two pointers at opposite ends of string
    left, right = 0, len(s) - 1

    # Continue until pointers meet in the middle
    while left < right:
        # Skip non-alphanumeric characters from the left
        # Keep left < right check to avoid crossing pointers
        while left < right and not s[left].isalnum():
            left += 1

        # Skip non-alphanumeric characters from the right
        # Keep left < right check to avoid crossing pointers
        while left < right and not s[right].isalnum():
            right -= 1

        # Compare characters (case-insensitive)
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True
