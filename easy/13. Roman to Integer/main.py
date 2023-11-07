class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.x = s
        romance_convert_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        romance_special = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        x_sum = 0
        for key, val in romance_special.items():
            if key in self.x:
                x_sum += val
                self.x = self.x.replace(key, '')
                print(x_sum)
            print(self.x)
        if self.x:
            x_lst = list(self.x)
            x_int_lst = [romance_convert_int[i] for i in x_lst]
            return x_sum + sum(x_int_lst)
        else:
            return x_sum



test = Solution()
print(test.romanToInt('MCMXCIV'))