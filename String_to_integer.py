Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.


MY SOLUTION
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        max_number = 2147483647
        min_number = -2147483648
        if len(str) < 1:
            return 0
        elif str.isdigit():
            if int(str) > max_number:
                return max_number
            else:
                return int(str)
        else:
            stop = len(str)
            print type(str)
            if len(str) > 1:
                foundNum = ""
                for e in str:
                    if e.isdigit():
                        foundNum = e
                    if foundNum.isdigit() and e.isdigit() == False:
                        stop = str.index(e)
                        break
            try:
                float(str[0:stop])
                if int(float(str[0:stop])) > max_number:
                    return max_number
                elif int(float(str[0:stop])) < min_number:
                    return min_number
                else:
                    return int(float(str[0:stop]))
            except:
                return 0





ANOTHER SOLUTION W REGEX

class Solution:
    # @return an integer
    def atoi(self, str):
        str = str.strip()
        str = re.findall('(^[\+\-0]*\d+)\D*', str)

        try:
            result = int(''.join(str))
            MAX_INT = 2147483647
            MIN_INT = -2147483648
            if result > MAX_INT > 0:
                return MAX_INT
            elif result < MIN_INT < 0:
                return MIN_INT
            else:
                return result
        except:
            return 0
