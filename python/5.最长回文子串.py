#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            # odd
            temp = self.findLongest(s, i, i)
            if len(temp) > len(res):
                res = temp
            # even
            temp = self.findLongest(s, i, i+1)
            if len(temp) > len(res):
                res = temp

        return res
    
    def findLongest(self, s, l, r):
        while l >= 0 and r < len(s) and s[l]==s[r]:
            l -= 1
            r += 1
        return s[l+1:r]
# @lc code=end

