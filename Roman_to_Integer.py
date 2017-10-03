Roman to Integer
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"];
        dividers =  [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        our_string = s
        number = 0
        i = 0
        while i < len(romans):
            if romans[i] == our_string[0:len(romans[i])]:
                number = number + dividers[i]
                our_string = our_string[len(romans[i]):]
            else:
                i += 1
        return number
