# URL  : https://leetcode.com/problems/shuffle-string/

# Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
# Output: "leetcode"
# Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.
# Example 2:

# Input: s = "abc", indices = [0,1,2]
# Output: "abc"
# Explanation: After shuffling, each character remains in its position.
# Example 3:

# Input: s = "aiohn", indices = [3,1,4,2,0]
# Output: "nihao"
# Example 4:

# Input: s = "aaiougrt", indices = [4,0,2,6,7,3,1,5]
# Output: "arigatou"
# Example 5:

# Input: s = "art", indices = [1,0,2]
# Output: "rat"
 

# Constraints:

# s.length == indices.length == n
# 1 <= n <= 100
# s contains only lower-case English letters.
# 0 <= indices[i] < n
# All values of indices are unique (i.e. indices is a permutation of the integers from 0 to n - 1).



class Solution:
    def restoreString(self, s: str, indices: list) -> str:
        res = '' 
        for ind in range(len(s)):
            res += s[indices.index(ind)]
        return res


sol = Solution()

print(sol.restoreString("codeleet" ,[4,5,6,7,0,2,1,3] ))

print(sol.restoreString("abc" ,[0,1,2] ))

print(sol.restoreString("aiohn" ,[3,1,4,2,0] ))

print(sol.restoreString("aaiougrt" ,[4,0,2,6,7,3,1,5] ))

print(sol.restoreString("art" ,[1,0,2] ))
        