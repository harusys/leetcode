#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_hash = {}
        for i, num in enumerate(nums):
            potentialMatch = target - num
            if potentialMatch in num_hash.keys():
                return [num_hash[potentialMatch], i]
            num_hash[num] = i
# @lc code=end
