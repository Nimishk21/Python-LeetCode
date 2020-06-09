class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        unique=set(nums)
        nums=list(unique)
    
        if len(nums) < 3:
            return max(nums)
        else:
            nums.sort(reverse=True)
        return nums[2]
        
        
        
#method 2:
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        x=list(set(nums))
        if len(x)<3:
            return max(x)
        else:
            x.remove(max(x))
            x.remove(max(x))
            return max(x)
