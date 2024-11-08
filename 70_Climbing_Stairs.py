# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
 

# Constraints:

# 1 <= n <= 45

class Solution_1:
    
    def climbStairs(self, n: int) -> int:
        a = 0 
        b = 1
        res = 0
        for _ in range(n):
            res = a + b
            a = b 
            b = res
        return res
    
class Solution_2:
    
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        else: 
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)