from collections import Counter
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        from fractions import gcd
        vals=Counter(deck).values()
        return reduce(gcd,vals)>=2
