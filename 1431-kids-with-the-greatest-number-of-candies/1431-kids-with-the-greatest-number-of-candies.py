class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        results =[0]*len(candies)
        max_candy = max(candies)
        for index,candy in enumerate(candies) :
            if extraCandies + candy >= max_candy:
                results[index]=1
 
        return results
        