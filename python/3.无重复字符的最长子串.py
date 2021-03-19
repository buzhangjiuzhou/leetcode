#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        s = list(s)
        for i, char in enumerate(s):
            print(i, char, start, end)
            if end == i:
                # add length
                if char not in s[start:end]:
                    end = i + 1
            else:
                # add length
                print(i-end+start)
                if char not in s[i-end+start:i] and len(set(s[i-end+start:i])) == len(s[i-end+start:i]):
                    start += i - end
                    end = i + 1 
        return end - start
# @lc code=end

# 不需要知道最长的是那些字符串，所以可以只考虑当前字符所在的可行字符串。