def f(i):
    return [i]

print(f(2))

str = ["eat","tea","tan","ate","nat","bat"]
s = "tan"
if s in str:
    print("True")
xMap = {}
# print(len(xMap))

nums = [0,0,1,1,1,2,2,3,3,4]

for i in range(len(nums)):
    xMap[nums[i]] = 1 + xMap.get(nums[i], 0)
print(len(xMap))
print(xMap.keys())

x = [3,1,4]
print(sorted(x))

# added some comments

print(nums.index(3))