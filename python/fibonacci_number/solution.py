class Solution:
    def fib(self, n):
        """
        Problem Type: Recursion - Classic Fibonacci Sequence

        Approach:
            Implement the Fibonacci sequence using pure recursion.
            This method relies solely on the recursive definition:

                F(0) = 0
                F(1) = 1
                F(n) = F(n-1) + F(n-2)

            Base cases:
                - If n is 0, return 0
                - If n is 1, return 1

            Recursive case:
                - For n > 1, return fib(n-1) + fib(n-2)

            Note:
                This approach demonstrates recursive thinking and function call trees,
                but has exponential time complexity due to overlapping subproblems.

        Time Complexity: O(2^n)
            - Each call spawns two more calls until base cases are reached.
            - Highly inefficient for large `n` due to repeated computation.

        Space Complexity: O(n)
            - Due to the depth of the call stack (at most `n` deep)

        Args:
            n (int): Index in the Fibonacci sequence (0-based)

        Returns:
            int: The nth Fibonacci number
        """
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib(n - 1) + self.fib(n - 2)
