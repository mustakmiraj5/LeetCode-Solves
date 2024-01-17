nums = [4,2,5,3,2]
target = 7
prvMap = {}

for i, n in enumerate(nums):
    diff = target - n
    if diff in prvMap:
        print([prvMap[diff], i])
    prvMap[n] = i