class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        common=[]
        indexSumList=[]
        res=[]
        minIndex=len(list1)+len(list2)
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i]== list2[j]:
                    indexSum=i+j
                    common.append(list1[i])
                    indexSumList.append(indexSum)
        if len(common)<2:
            return common
        for i in range (len(indexSumList)):
            minIndex=min(minIndex,indexSumList[i])
        for i in range (len(indexSumList)):
            if minIndex == indexSumList[i]:
                res.append(common[i])
        return res
            

            

