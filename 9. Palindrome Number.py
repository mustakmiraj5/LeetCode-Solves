class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)
        l = len(y)

        for i in range(l):
            if i > l/2 :
                break
            if y[i] != y[l-1-i]:
                return False
        return True

# Best solution
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#             x = str(x)
#             return x[::-1] == x