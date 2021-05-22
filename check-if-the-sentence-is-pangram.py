# URL : https://leetcode.com/problems/check-if-the-sentence-is-pangram/

# Example 1:

# Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
# Output: true
# Explanation: sentence contains at least one of every letter of the English alphabet.
# Example 2:

# Input: sentence = "leetcode"
# Output: false
 

# Constraints:

# 1 <= sentence.length <= 1000
# sentence consists of lowercase English letters.


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return list(map(ord, sorted(set(sentence.upper())))) == list(range(65, 91))
        

        

sol = Solution()
print(sol.checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))
print(sol.checkIfPangram("leetcode"))