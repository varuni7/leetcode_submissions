class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        
        number_frequency_dict = {}
        # dictionary to keep track of the frequency of each element in nums
        
        for num in nums:
            if num in number_frequency_dict:
                
                number_frequency_dict[num]+=1
            else:
                
                number_frequency_dict[num]=1
        
        k_pairs=sorted(number_frequency_dict.items(),key=lambda x:x[1], reverse=True)[:k]
        ans = [record[0] for record in k_pairs]
        return ans 
                
                
                