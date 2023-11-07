class Solution(object):
    def __init__(self, x):
          self.x = x
    def isPalindrome(self):
        x_str = str(self.x)
        x_chars = list(x_str)
        print(x_chars)
        x_length = len(x_str)
        if x_length % 2 != 0:
            firstpart, secondpart = x_str[:x_length//2], x_str[x_length//2 + 1:]
        else:
            firstpart, secondpart = x_str[:x_length//2], x_str[x_length//2:]
        print(firstpart, secondpart)
        if firstpart == secondpart[::-1]:
            return True
        else:
            return False
        # for i in range(len(x_chars)):
        #     if x_chars[i] != x_chars[len(x_chars) - 1 - i]:
        #         return print(f"{self.x} is NOT Palindrome")
        # return print(f"{self.x} is Palindrome")
        # x_str = str(self.x)
        # x_chars = list(x_str)

test = Solution(323)
print(test.isPalindrome())
print([*"123"][:2])
##### 123 321