from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cnt1=Counter(nums1)
        cnt2=Counter(nums2)
        ans = []
        for key in cnt1:
            for i in range(min(cnt1[key], cnt2[key])):
                ans.append(key)
        return ans
    
    
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a=[]
        for i in nums1:
            if i in nums2:
                nums2.remove(i)
                a.append(i)
        return a

