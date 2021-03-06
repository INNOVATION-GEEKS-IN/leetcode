# // URL :  https://leetcode.com/problems/median-of-two-sorted-arrays/


# // Example 1:

# // Input: nums1 = [1,3], nums2 = [2]
# // Output: 2.00000
# // Explanation: merged array = [1,2,3] and median is 2.
# // Example 2:

# // Input: nums1 = [1,2], nums2 = [3,4]
# // Output: 2.50000
# // Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
# // Example 3:

# // Input: nums1 = [0,0], nums2 = [0,0]
# // Output: 0.00000
# // Example 4:

# // Input: nums1 = [], nums2 = [1]
# // Output: 1.00000
# // Example 5:

# // Input: nums1 = [2], nums2 = []
# // Output: 2.00000
 

# // Constraints:

# // nums1.length == m
# // nums2.length == n
# // 0 <= m <= 1000
# // 0 <= n <= 1000
# // 1 <= m + n <= 2000
# // -106 <= nums1[i], nums2[i] <= 106

class Solution:
	def findMedianSortedArrays(self, nums1, nums2) :
		res = sorted(nums1+nums2)
		l = len(res)
		if(l%2==1):
			return float(res[l//2])
		else:
			return float((res[l//2] + res[l//2-1]))/2




sol = Solution()

print(sol.findMedianSortedArrays([1,3] , [2, 7]))


