strs = ["eat","tea","tan","ate","nat","bat"]

sortedArray = []
anagramArray = []
sortedMap = {}
idx = 0


for i in range(len(strs)):
    s1 = sorted(strs[i])
    if s1 in sortedMap:
        anagramArray[sortedMap[s1]].append(strs[i])
    else:
        sortedMap[s1] = idx
        anagramArray[idx].append(strs[i])
        idx = idx+1
print(anagramArray)
