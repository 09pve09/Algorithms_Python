from collections import deque
d = deque('ghi')                 # make a new deque with three items
for elem in d:                   # iterate over the deque's elements
    print elem.upper()

d.append('j')                    # add a new entry to the right side
d.appendleft('f')                # add a new entry to the left side

d.pop()                          # return and remove the rightmost item

d.popleft()                      # return and remove the leftmost item

list(d)                          # list the contents of the deque

d[0]                             # peek at leftmost item

d[-1]                            # peek at rightmost item


list(reversed(d))                # list the contents of a deque in reverse

d.extend('jkl')                  # add multiple elements at once

d.rotate(1)                      # right rotation
d.rotate(-1)                     # left rotation

deque(reversed(d))               # make a new deque in reverse order
d.clear()                        # empty the deque
d.pop()                          # cannot pop from an empty deque

d.extendleft('abc')              # extendleft() reverses the input order
