class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        if start> destination:
            end= start
            start=destination
            destination=end
        dis= min(sum(distance[0:start])+sum(distance[destination:]),sum(distance[start:destination]))
        return dis

