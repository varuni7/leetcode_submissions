class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ps=[arr[0]]
        ans=0
        for ele in arr[1::]:
            ps.append(ps[-1]+ele)
        print(ps)
        for i in range(0,len(arr)-k+1):
            
            if ((ps[i+k-1]-ps[i])+arr[i])//k>=threshold:
                print(arr[i])
                print(arr[i+k-1])
                ans+=1
        return ans 
             