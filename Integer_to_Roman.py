Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.

class Solution(object):
    def intToRoman(self, num):
        romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"];
        dividers =  [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        number = num
        roman_word = ""
        for i in range(0, len(dividers)):
            if number == 0:
                return roman_word
            times = number / dividers[i]
            # 3999/1000 =3
            # 999/900 = 1
            # 99/500 = 0.153
            # ..
            # 99/90 = 1
            # ..
            # 9/9 = 1
            number = number % dividers[i]
            # 3999 % 1000 = 999
            # 999 % 900 = 99
            # 99 % 500 = 99
            # ..
            # 99 % 90 = 9
            # 9 % 9 = 0

            if times > 0:
                roman_word = roman_word + romans[i]*times
        return roman_word

        
