class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        import heapq
        stones = [-stone for stone in stones]
        while len(stones)>1:
            
            heapq.heapify(stones)
            largest_stone = heapq.heappop(stones)
            scnd_largest_stone = heapq.heappop(stones)
            if largest_stone == scnd_largest_stone and len(stones)>0:
                continue 
            elif largest_stone == scnd_largest_stone and len(stones)==0:
                return 0
                
            else:
                heapq.heappush(stones,-abs(largest_stone-scnd_largest_stone))
        return abs(stones[0])
        
        