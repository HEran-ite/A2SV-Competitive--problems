class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        arr=[0]*n
        prefix_sum=0
        prefix_arr=[]
        for i in range (len(bookings)):
            arr[bookings[i][0]-1]+=bookings[i][2]
            if bookings[i][1]!=n:
                arr[bookings[i][1]]-=bookings[i][2]
        for i in range (len(arr)):
            prefix_sum +=arr[i]
            prefix_arr.append(prefix_sum)
        return prefix_arr