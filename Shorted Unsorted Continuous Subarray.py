class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_num=sorted(num)
        start,end=0,0
        for i in range(0,len(nums)):
            if nums[i]!=sorted_nums[i]:
                start=i
                break
        for i in range(len(nums),-1,-1):
            if nums[i]!=sorted_nums[i]:
                end=i
                break
         ans=end-start
         if ans>0:
            return ans+1
          else:
            return 0
