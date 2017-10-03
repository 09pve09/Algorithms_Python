Write a function that takes two strings as arguments and returns a string containing only
the characters found in both strings. Have them write 2 versions — one that is O(n) and one that is O(n^2).

def Solution(s1,s2):
  result = ''
  counter = 0
  dict1 = {}
  dict2 = {}
  if not s1 or not s2:
    return False
  while counter < len(s1) or counter < len(s2):
    if counter < len(s1):
      if s1[counter] in dict2 and dict2[s1[counter]] > 0:
        result = result + s1[counter]
        dict2[s1[counter]] -= 1
      else:
        if s1[counter] not in dict1:
          dict1[s1[counter]] = 1
        else:
          dict1[s1[counter]] += 1
    if counter < len(s2):
      if s2[counter] in dict1 and dict1[s2[counter]] > 0:
        result = result + s2[counter]
        dict1[s2[counter]] -= 1
      else:
        if s2[counter] not in dict2:
          dict2[s2[counter]] = 1
        else:
          dict2[s2[counter]] += 1
      counter += 1
  return result


str1 = 'PisdksaCaahu'
str2 = 'CPUikkavCnxheru'

print Solution(str1,str2)
