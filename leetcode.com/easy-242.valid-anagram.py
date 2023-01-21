#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        print(Counter(s))
        print(Counter(t))
        return Counter(s) == Counter(t)
# @lc code=end
