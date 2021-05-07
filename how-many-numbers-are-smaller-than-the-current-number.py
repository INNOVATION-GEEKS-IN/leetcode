# URL : https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

# Example 1:

# Input: nums = [8,1,2,2,3]
# Output: [4,0,1,1,3]
# Explanation: 
# For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
# For nums[1]=1 does not exist any smaller number than it.
# For nums[2]=2 there exist one smaller number than it (1). 
# For nums[3]=2 there exist one smaller number than it (1). 
# For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
# Example 2:

# Input: nums = [6,5,4,8]
# Output: [2,1,0,3]
# Example 3:

# Input: nums = [7,7,7,7]
# Output: [0,0,0,0]
 

# Constraints:

# 2 <= nums.length <= 500
# 0 <= nums[i] <= 100


class Solution:
    def smallerNumbersThanCurrent(self, nums: list) -> list:
        res = []
        for ind, item in enumerate(nums):
            cnt = 0
            for ind_x in range(len(nums)):
                if ind == ind_x:
                    continue 
                else:
                    if nums[ind_x] < item:
                        cnt += 1
            res.append(cnt)
        return res

sol = Solution()

print(sol.smallerNumbersThanCurrent([8,1,2,2,3]))
print(sol.smallerNumbersThanCurrent([6,5,4,8]))
print(sol.smallerNumbersThanCurrent([7,7,7,7]))