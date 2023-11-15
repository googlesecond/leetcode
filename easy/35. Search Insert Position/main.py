class Solution:
    def searchInsert(self, nums, target: int) -> int:
        mark = 0
        while True:
            middle = len(nums)//2
            if middle != 0:
                if nums[middle] == target:
                    return middle + mark
                elif nums[middle] < target:
                    nums = nums[middle:]
                    mark += middle
                else:
                    nums = nums[:middle]
            else:
                if nums[middle] == target:  
                    return middle + mark
                elif nums[middle] < target:
                    return middle + mark + 1
                else:
                    return middle + mark

test = Solution()
print(test.searchInsert([1,3,5,7,9,10], 9))