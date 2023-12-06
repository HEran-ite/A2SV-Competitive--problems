class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        indices=[]
        output=[]
        moves=0
        for i in range(len(boxes)) :
            if boxes[i]=='1':
                indices.append(i)
        for i in range (len(boxes)):
            moves=0
            for j in range(len(indices)):
                 moves+=abs(indices[j]-i)
            output.append(moves)
        return output
