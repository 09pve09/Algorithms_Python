The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
Subscribe to see which companies asked this question.


class Solution(object):
    def convert(self, s, numRows):
        count = 1
        convLib = {}
        while count <= numRows:
          convLib[count] = ""
          count += 1
        i = 0
        runner = 1
        up = False
        if numRows == 1 or numRows >= len(s):
            return s
        else:
            while i < len(s):
                if runner <= numRows and up == True and runner != 1:
                    convLib[runner] = convLib[runner] + s[i]
                    runner -= 1
                    i += 1

                elif runner == 1 and up == True:
                    convLib[runner] = convLib[runner] + s[i]
                    runner += 1
                    up = False
                    i += 1

                elif runner >= 1 and runner != numRows:
                    convLib[runner] = convLib[runner] + s[i]
                    runner += 1
                    i += 1

                elif runner <= numRows:
                    convLib[runner] = convLib[runner] + s[i]
                    runner -= 1
                    i += 1
                    up = True

            convString = ""
            for key, value in convLib.iteritems():
                convString = convString + value
        return convString
