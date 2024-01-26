class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numMap = {}
        for i in range(len(nums)):
            numMap[nums[i]] = 1 + numMap.get(nums[i], 0)
        sortedMap = dict(sorted(numMap.items(), key=lambda item: item[1]))
        ans = []
        for key in reversed(sortedMap):
            if k == 0:
                break
            ans.append(key)
            k -= 1
        return ans