from collections import defaultdict


t=int(input())
for i in range (t):
    n=int(input())
    arr=list(map(int,input()))
    prefix_sum = 0
    dic =defaultdict(int)
    dic[0]=1
    count = 0

    for i in range(len(arr)):
        prefix_sum += arr[i]-1
        if prefix_sum in dic:
            count += dic[prefix_sum]
        dic[prefix_sum] = dic.get(prefix_sum, 0) + 1

    print (count)