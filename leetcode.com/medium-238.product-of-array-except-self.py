#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        lprod = 1
        rprod = 1
        for i in range(len(nums)):
            res[i] *= lprod
            lprod *= nums[i]
            res[~i] *= rprod
            rprod *= nums[~i]
        return res
# @lc code=end
