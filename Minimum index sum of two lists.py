class Solution(object):
    def findRestaurant(self, list1, list2):
        set1=set(list1)
        set2=set(list2)
        commons={}
        for name in (set1 & set2):
            sum=list1.index(name)+list2.index(name)
            if sum not in commons:
                commons[sum]=[]
            commons[sum].append(name)
        return commons[min(commons.keys())]
            
