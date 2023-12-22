class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False
        inc=True
        dec=True
        for i in range (1,len(arr)):
            if arr[i]>=arr[i-1] :
                dec=False
            else:
                inc=False
        if dec or inc:
            return False
        # for i in range(len(arr)-1):
        #     if arr[i]==arr[i+1]:
        #         return False 
        up=True
        maxVal=max(arr)

        for i in range (1,len(arr)):
            if up:
                if arr[i]<=arr[i-1]:
                    return False
            else:
                if arr[i]>=arr[i-1]:
                    return False
            if arr[i]==maxVal:
                up=False
        return True 
           