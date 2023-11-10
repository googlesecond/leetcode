class Solution:
    def removeDuplicates(self, nums) -> int:
        for n, x in enumerate(nums):
            if n != len(nums) -1:
                if nums[n] == nums[n+1]:
                    nums[n] = '_'
        print(nums)
        step = startPoint = countDuplicate = 0
        for n, val in enumerate(nums):
            if nums[n] == '_':
                step += 1
                countDuplicate += 1
            else:
                if step != 0:
                    startPoint = n - step
                    nums[startPoint] = val
                    nums[n] = '_'
                
        return len(nums) - countDuplicate, nums
    
test = Solution()
num = [1, 2, 2, 2, 3, 3, 3, 3, 4]
print(test.removeDuplicates(num))

