# https://leetcode.com/problems/find-common-characters/

# Example 1:

# Input: ["bella","label","roller"]
# Output: ["e","l","l"]
# Example 2:

# Input: ["cool","lock","cook"]
# Output: ["c","o"]
 

# Note:

# 1 <= A.length <= 100
# 1 <= A[i].length <= 100
# A[i][j] is a lowercase letter

class Solution:
    def commonChars(self, A: list) -> list:
        util_dict = {}
        res = []
        for ch in A[0]:
            if ch in util_dict:
                util_dict[ch] += 1
            else : util_dict[ch] = 1 

        for ch in util_dict:
            for item in A[1:]:
                if item.count(ch) == util_dict[ch]:
                    continue
                else:
                    util_dict[ch] = min(util_dict[ch] , item.count(ch) )
        res = []
        for ch in A[0]:
            if util_dict[ch] == 0:
                continue
            if ch in util_dict:
                res.append(ch)
                util_dict[ch] -= 1

        return res

sol = Solution()
print(sol.commonChars(["bella","label","roller"]))
print(sol.commonChars(["cool","lock","cook"]))
