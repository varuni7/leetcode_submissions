class Solution:
    def sortColors(self, nums: List[int]) -> None:

        temp = 0
        for i in range(len(nums)):
            for j in range(0,len(nums)-1-i):
                if nums [j]> nums[j+1]:
                    temp = nums[j+1]
                    nums[j+1]= nums[j]
                    nums[j]= temp
                
        