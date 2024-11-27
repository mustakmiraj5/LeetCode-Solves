class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        res = nums[0]
        diff = abs(nums[0] - 0)
        for i in nums:
            if abs(i-0) < diff:
                res = i
                diff = abs(i-0)
            if abs(i-0) == diff:
                res = max(i, res)
        return res
    

# -> measure the difference from 0
# -> keep track of minimum distance ans store in response(res) variable
# -> if the difference for 2 or more value is same then store the biggest one