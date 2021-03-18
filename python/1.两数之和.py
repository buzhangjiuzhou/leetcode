#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start    
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[j] == target - nums[i] and i != j:
                    temp_list = []
                    temp_list.append(i)
                    temp_list.append(j)
                    return temp_list
# @lc code=end

# Accepted
# 53/53 cases passed (36 ms)
# Your runtime beats 85.18 % of python3 submissions
# Your memory usage beats 67.16 % of python3 submissions (14.9 MB)

# @lc code=start    
class BetterSolution:
    def twoSum(self, nums, target):
        seen = {}
        for i, value in enumerate(nums):
            remain = target - value
            if remain in seen:
                return [i, seen[remain]]
            else:
                seen[value] = i
# @lc code=end

# Accepted
# 53/53 cases passed (32 ms)
# Your runtime beats 95.42 % of python3 submissions
# Your memory usage beats 49.55 % of python3 submissions (14.9 MB)

if __name__ == '__main__':
    # begin
    s = BetterSolution()
    print (s.twoSum([0, 2, 0], 0))