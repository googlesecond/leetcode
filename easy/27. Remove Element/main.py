class Solution:
    def removeDuplicates(self, nums, val) -> int:
        for n, x in enumerate(nums):
            if x == val:
                nums[n] = '_'

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
num = [3,2,2,3]
print(test.removeDuplicates(num, 3))