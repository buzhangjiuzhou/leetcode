#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        step = max(2*numRows -2, 1)
        out = [[]for i in range(numRows)]
        for i in range(len(s)):
            res = i % step
            if res >= numRows:
                res = step - res
            out[res].append(s[i])
        final_out = ""
        for i in range(numRows):
            for j in range(len(out[i])):
                final_out += out[i][j]
        return final_out

# @lc code=end

