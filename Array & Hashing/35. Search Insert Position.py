class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = len(nums)
        if target in nums:
            return nums.index(target)
        else:
            if target < nums[0]:
                return 0
            elif target > nums[l-1]:
                return l
            else:
                t = target
                for i in range(l):
                    t -= 1
                    if t in nums:
                        return nums.index(t) + 1