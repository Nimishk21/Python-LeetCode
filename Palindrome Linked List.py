# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        l1=[]
        temp=head
        while(temp):
            l1.append(temp.val)
            temp=temp.next
        return l1==l1[::-1]
