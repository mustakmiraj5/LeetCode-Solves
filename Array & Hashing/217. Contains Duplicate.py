list = [1,2,3,4,1]
seen = set()

def duplicateNum(list) -> bool:
    for num in list:
        if num in seen:
            return True
        seen.add(num)
    return False

if duplicateNum(list):
    print('TRUE')
else:
    print('FALSE')