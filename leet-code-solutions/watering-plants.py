class Solution(object):
    def wateringPlants(self, plants, capacity):
        """
        :type plants: List[int]
        :type capacity: int
        :rtype: int
        """
        moves=0
        maxCapacity=capacity
        for i in range (len(plants)):
            if plants[i]<= capacity:
                capacity-=plants[i]
                moves+=1
            else:
                capacity=maxCapacity
                capacity-=plants[i]
                moves+= 2*i+1
        return moves

                