class Solution(object):
    def isValid(self, s):
        """
        Checks if the input string 's' has valid parentheses.

        :type s: str
        :rtype: bool
        """
        stack = []  # Stack to track opening parentheses

        for char in s:
            if char in '([{':  # If it's an opening parenthesis, push to the stack
                stack.append(char)
            else:
                if not stack:  # If stack is empty and we get a closing parenthesis, it's invalid
                    return False
                # # Check if stack is empty or if the closing parenthesis matches the top of the stack
                if (not stack) or (char == ')' and stack[-1] != '(') or (char == ']' and stack[-1] != '[') or (char == '}' and stack[-1] != '{'):
                    return False
                stack.pop()  # Pop the matched opening parenthesis
        # If the stack is empty, all parentheses were valid and matched
        return len(stack) == 0
