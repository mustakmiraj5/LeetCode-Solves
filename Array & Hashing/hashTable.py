data = {
    'books' : 120,
    'paper' : 140,
    'pen' : 400,
    'scale' : 20,
    'pencil' : 300,
    'eraser' : 340,
    'sharpner' : 450
}

# print(data['books'])

s = 'anagram'
t = 'nagaram'

countS, countT = {}, {}

for i in range(len(s)):
    countS[s[i]] = 1 + countS.get(s[i], 0)
    countT[t[i]] = 1 + countT.get(t[i], 0)

# print(countT.get(t[1]))

testString = ''