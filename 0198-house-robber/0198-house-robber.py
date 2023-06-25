class Solution:
    def rob(self, nums: List[int]) -> int:
        
        prev=0
        curr=0
        for ele in nums:
            temp=prev
            prev=curr
            curr=max(ele+temp,prev)
        return curr
            
        