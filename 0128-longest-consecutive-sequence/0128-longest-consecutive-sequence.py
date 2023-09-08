class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #input : list->an unsorted array of int 
        #output : int -> longest inc subsequence 
        
        set_nums=set(nums) # converting nums to a set so lookup takes O(1)
        max_length=0
        for num in nums:
            
            if num-1 in set_nums:
                
                continue 
            
            else: # it is the start of a new subsequence 
                
                subseq_length=0
                num_in_subsequence = num
                while num_in_subsequence in set_nums:
                    subseq_length +=1
                    
                    num_in_subsequence+=1
                max_length=max(subseq_length,max_length)
                    
        return max_length
                    
                
                
            
            