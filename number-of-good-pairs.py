# URL : https://leetcode.com/problems/number-of-good-pairs/

# Example 1:

# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
# Example 2:

# Input: nums = [1,1,1,1]
# Output: 6
# Explanation: Each pair in the array are good.
# Example 3:

# Input: nums = [1,2,3]
# Output: 0

class Solution:
    def numIdenticalPairs(self, nums:list) -> int:
        triangle_number = lambda x: x*(x-1)//2 
        util_dict = {}
        for num in nums:
            if num in util_dict:
                util_dict[num] += 1 
            else:
                util_dict[num] = 1
        return sum(list(map(triangle_number, util_dict.values())))

sol = Solution()
print(sol.numIdenticalPairs([1,2,3,1,1,3]))
print(sol.numIdenticalPairs([1,1,1,1]))
print(sol.numIdenticalPairs([1,2,3]))