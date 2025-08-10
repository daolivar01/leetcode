def isValid(self, s):
    """
    Determine if string has valid parentheses/brackets.
    
    Args:
        s: String containing only '(){}[]'
        
    Returns:
        bool: True if all brackets are properly matched and nested
        
    Time: O(n), Space: O(n)
    """
    stack = []
    for char in s:
        if char in '([{':
            stack.append(char)
        else:
            if not stack:
                return False
            if (char == ')' and stack[-1] != '(') or (char == ']' and stack[-1] != '[') or  (char == '}' and stack[-1] != '{'):
                return False
            stack.pop()

    return not stack
