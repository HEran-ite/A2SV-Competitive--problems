class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort(reverse=True)
        processorTime.sort()
        pt=0
        maxPt=0

        for i in range(len(processorTime)):
            pt=tasks[i*4]+processorTime[i]
            maxPt=max(maxPt,pt)
        return maxPt