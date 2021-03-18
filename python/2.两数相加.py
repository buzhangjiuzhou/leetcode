#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        start = None
        while l1 != None or l2 != None:
            if l1 == None:
                temp_l1 = 0
            else:
                temp_l1 = l1.val
            if l2 == None:
                temp_l2 = 0
            else:    
                temp_l2 = l2.val

            temp_sum = temp_l1 + temp_l2 + carry
            carry = temp_sum // 10
            temp_sum = ListNode(val=temp_sum%10)
            
            if start == None:
                start = temp_sum
                l_pre = start
            else:
                l_pre.next = temp_sum
                l_pre = l_pre.next
            
            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next
        if carry != 0:
            temp = ListNode(val=carry)
            l_pre.next = temp
        return start
# @lc code=end

# Accepted
# 1568/1568 cases passed (84 ms)
# Your runtime beats 18.06 % of python3 submissions
# Your memory usage beats 37.28 % of python3 submissions (14.9 MB)