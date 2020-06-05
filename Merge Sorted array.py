#method 1:
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
          nums1_copy=nums1[:m]
          nums1[:]=[]
          p1=p2=0
          while p1<m and p2<n:
            if nums1_copy[p1]<nums2[p2]:
                nums1.append(nums1_copy[p1])
                p1+=1
            else:
                nums1.append(nums2[p2])
                p2+=1
          if p1<m:
              nums1[p1+p2:]=nums1_copy[p1:]
          if p2<n:
              nums[p1+p2:]=nums2[p2:]
            
#method 2:
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
          nums1[m:]=nums2[:n]
          nums1.sort()
