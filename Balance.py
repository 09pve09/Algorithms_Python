#!/bin/python

import sys
def balance(s):
    opens = ['(','{','[']
    closes = [')','}',']']
    hash = []
    i = 0
    while i in range(len(s)):

        if s[i] in opens:
            hash.append(s[i])

        elif s[i] in closes and len(hash) == 0:

            return "NO"
        elif s[i] in closes:

            if s[i] == ')' and hash[len(hash) - 1] == '(':
                hash.pop()

            elif s[i] == '}' and hash[len(hash) - 1] == '{':
                hash.pop()

            elif s[i] == ']' and hash[len(hash) - 1] == '[':
                hash.pop()

        i += 1
    if len(hash) == 0:
        return "YES"
    else:

        return "NO"

t = int(raw_input().strip())
for a0 in xrange(t):
    s = raw_input().strip()
    print balance(s)
