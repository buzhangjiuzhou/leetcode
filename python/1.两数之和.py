#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start    
class Solution:
    def twoSum(self, nums, target: int):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[j] == target - nums[i] and i != j:
                    temp_list = []
                    temp_list.append(i)
                    temp_list.append(j)
                    return temp_list


# @lc code=end

if __name__ == '__main__':
    # begin
    s = Solution()
    print (s.twoSum([0, 2, 0], 0))