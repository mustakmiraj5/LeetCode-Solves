s = 'anagram'
t = 'nagaram'
flag = True

s = sorted(s)
print(s)
for c in s:
    if c in t:
        flag = True
    else:
        flag = False
        break
if flag:
    print("TRUE")
else:
    print('FALSE')

if len(s) != len(t):
    print("Hoy nai vaag..")


# with hash table : 
    
countS, countT = {},{}

for i in range(len(s)):
    countS[s[i]] = 1 + countS.get(s[i],0)
    countT[t[i]] = 1 + countT.get(t[i],0)

print(countS)
print(countT)