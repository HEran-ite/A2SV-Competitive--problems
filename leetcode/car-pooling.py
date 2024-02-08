class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1]) 
        start=trips[0][1]
        end=trips[-1][2]
        arr=[0]*1000
        prefix_sum=0
        prefix_arr=[]
        
        print(trips)
        for i in range (len(trips)):
            arr[trips[i][1]-start]+=trips[i][0]
            if trips[i][2] != trips[-1][2]:
                arr[trips[i][2]-start]-=trips[i][0]

        for i in range(len(arr)):
            prefix_sum+=arr[i]
            prefix_arr.append(prefix_sum)
        print(prefix_arr)
        for i in range (len(prefix_arr)):
            if prefix_arr[i]> capacity:
                return False
        return True