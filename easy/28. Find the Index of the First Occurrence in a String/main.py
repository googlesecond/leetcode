class Solution:
    def strStr(self, haystack, needle) -> int:
        if needle not in haystack:
            return -1
        else:
            length = len(needle)
            for i, val in enumerate(haystack):
                if val == needle[0]:
                    n = 1
                    for j in range(i + 1, i + length):
                        if haystack[j] == needle[n]:
                            n += 1
                            continue
                        else:
                            break
                    if n == length:
                        return i

haystack = "mississippi"
needle = "issip"

test = Solution()
print(test.strStr(haystack, needle))

