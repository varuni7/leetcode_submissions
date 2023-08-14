class Solution:
    import heapq
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums=[-ele for ele in nums]
        # heapq.heapify(nums)
        # for i in range(k):
        #     ele = heapq.heappop(nums)
        # return abs(ele) 
        
        k_ele_max_heap=[]
        for ele in nums:
            if len(k_ele_max_heap)<k:
                heapq.heappush(k_ele_max_heap,ele)
            else:
                if ele > k_ele_max_heap[0]:
                    heapq.heappop(k_ele_max_heap)
                    heapq.heappush(k_ele_max_heap,ele)
        return k_ele_max_heap[0]
                    
                    
        
        
        
        
            
        
        
    
    
        
        
        