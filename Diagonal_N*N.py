nums = [3,3,1,2,3,4,5,6,7,8,9]

def Solution(list):
  rows = list[0]
  columns = list[1]
  list = list[2:]
  pointer = 0
  result = []
  while pointer < len(list):
    if pointer != 0 and pointer % columns == 0:
      pointer += columns-1
      rows -= 1
      continue
    sub_list = [list[pointer]]
    if pointer != 0:
      for i in range(1,rows):
        if pointer+(i*columns) < len(list) and ((pointer - i)+(i*columns)+ 1) % columns != 0:
          sub_list.append(list[(pointer - i)+(i*columns)])
    result.append(sub_list)
    pointer += 1
  return result

print Solution(nums)
