class Solution:
   
    def climbStairs(self, n: int) -> int:
#         if n ==0:
#             return 1
#         if n ==1:
#             return 1

#         return self.climbStairs(n-1)+self.climbStairs(n-2)
        
        
        prev1=1
        prev2=1
        curr_i=1
        for i in range(2,n+1):
            curr_i=prev1+prev2
        
            prev1=prev2
            prev2=curr_i
        return curr_i
        
        
        
    
    
        
        
        