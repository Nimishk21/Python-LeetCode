#method 1:
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        n5, n10 = 0, 0
        for i in bills:
            if i == 5: 
                n5 += 1
            elif i == 10: 
                n10 += 1 
                n5 -= 1
            elif n10 > 0: 
                n10 -= 1 
                n5 -= 1
            else: 
                n5 -= 3
            if n5 < 0: return False
        return True
        
#method 2:
class Solution(object): #aw
    def lemonadeChange(self, bills):
        five = ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if not five: return False
                five -= 1
                ten += 1
            else:
                if ten and five:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True
