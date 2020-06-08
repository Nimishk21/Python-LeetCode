class Solution:
    def reverse(self, x: int) -> int:
        x_str=str(x)
        negative=True if x_str.startswith('-') else False
        reverse_x=str(abs(x))[::-1]
        result='-'+reverse_x if negative else reverse_x
        final=int(result)
        if final>=-2**31 and final <2**31-1:
          return final
        else:
          return 0
#method 2:
class Solution:
    def reverse(self, x: int) -> int:
        if x>0:
            a=int(str(x)[::-1])
        else:
            a=(-1)*(int(str(x*-1)[::-1]))
        min_a=-2**31
        max_a=2**31-1
        if a not in range(min_a,max_a):
            return 0
        else:
            return a
