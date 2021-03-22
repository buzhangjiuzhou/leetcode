#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_nums = list(nums1 + nums2)
        new_nums = sorted(new_nums)
        if len(new_nums) % 2 == 0:
            result = (new_nums[len(new_nums)//2] + new_nums[len(new_nums)//2 -1]) / 2
        else:
            result = new_nums[len(new_nums)//2]
        return result
# @lc code=end

