class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        res = 0
        people.sort()
        l, r = 0, len(people) - 1

        while l <= r:
            reminder= limit-people[r]
            res+=1
            r-=1
            if l<=r and reminder >= people[l] :
                l+=1
        return res 

