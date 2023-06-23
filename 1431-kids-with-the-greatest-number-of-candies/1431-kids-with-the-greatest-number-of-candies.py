class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        results =[]
        max_candy = max(candies)
        for candy in candies :
            if extraCandies + candy >= max_candy:
                results.append(1)
            else:
                results.append(0)
        return results
        