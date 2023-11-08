strs = ["flower","flow","flight",'flew']
#strs = ["reflower","flow","flight"]

class Solution:
    def longestCommonPrefix(self, strs):
        self.strs = strs
        str_min_length = self.strs[0]
        min_length = len(str_min_length)
        common_prefix = ''
        checker = 0
        if len(strs) == 1:
            return strs[0]
        else:
            for i in range(1, len(self.strs)):
                if len(self.strs[i]) < min_length:
                    min_length = len(self.strs[i])
                    str_min_length = self.strs[i]
            strs.remove(str_min_length)

            for i in range(len(str_min_length)):
                for str in strs:
                    if str_min_length[i] == str[i]:
                        checker = 1
                        print(str_min_length[i], "in",str, common_prefix)
                    else:
                        return common_prefix
                if checker == 1:
                    common_prefix += str_min_length[i]
            return common_prefix


test = Solution()
print(test.longestCommonPrefix(strs))