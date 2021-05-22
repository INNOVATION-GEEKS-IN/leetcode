# URL : https://leetcode.com/problems/reverse-integer/

# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21
# Example 4:

# Input: x = 0
# Output: 0
 

# Constraints:

# -231 <= x <= 231 - 1

class Solution:
    def reverse(self, x: int) -> int:def reverse(self, x):
            
        isNegative = x < 0
        ret = 0
        x = abs(x)
        while x > 0:
            ret *= 10
            ret += x % 10
            x /= 10
        if ret > 1<<31:
            return 0
    
        if isNegative:
            return 0 - ret
        else:
            return ret
    
    
                    


sol = Solution()
print(sol.reverse(123))
print(sol.reverse(-123))
print(sol.reverse(0))
print(sol.reverse(1534236469))
