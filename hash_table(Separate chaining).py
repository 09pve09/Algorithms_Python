from __future__ import division
import random
import string
print 'ЗАДАНИЕ 1'
print 'создать ХТ на 30 ячеек. Заполнить ХТ с помощью 100 строк (создать функцию-генератор случайных строк одинаковой длины). В качестве ХФ использовать ХФ со слайда 12 лекции по ХТ. Проанализировать ХТ на предмет равномерной заполненности списков в каждой ячейке.'

def Hash_index(string):
  total = 0
  for i in range(len(string)):
    total = total + (ord(string[i])*(i+1))
  total = total % 30
  # total = total % 2069
  return total

def insert(string, hash_table, hashing_function):
  key = hashing_function(string)
  if key in hash_table:
    hash_table[key].append(string)
  else:
    hash_table[key] = [string]
  return hash_table

def search(string, hash_table):
  key = Hash_index(string)
  print 'key:', key
  if key not in hash_table:
    return None
  for i in hash_table[key]:
    if i == string:
      return i

def create_hash_table(num_of_cells):
  hash_table = {k: [] for k in range(num_of_cells)}
  return hash_table

def create_random_string(len):
  return ''.join(random.choice(string.ascii_lowercase) for i in range(len))

def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

my_hash_table = create_hash_table(30)

for i in range(100):
  insert(create_random_string(6), my_hash_table, Hash_index)

# print my_hash_table

# анализируем полученный ХТ
values =[]
for key in my_hash_table:
  values.append(len(my_hash_table[key]))
print values
# print my_hash_table
print 'average amount in every cell: ',mean(values)

print ' '
print 'ЗАДАНИЕ 2'
print 'Использовать ХФ типа md5 или sha из библиотеки hashlib. Сравнить результаты. В случае отсутствия различий увеличить размер таблицы и количество вставляемых строк.'

import hashlib

def Hash_index_using_md5(string):
  md5_hash = hashlib.md5()
  md5_hash.update(string)
  total = 0
  for i in range(0, len(md5_hash.hexdigest()), 2):
    total = total + (ord(md5_hash.hexdigest()[i])*(i+1))
  total = total % 30
  return total

my_hash_table1 = create_hash_table(30)

for i in range(100):
  insert(create_random_string(6), my_hash_table1, Hash_index_using_md5)

# анализируем полученный ХТ
values1 =[]
for key in my_hash_table1:
  values1.append(len(my_hash_table1[key]))
print values1
print 'average amount in every cell using md5: ', mean(values1)

print ''
print 'Вывод: Оба способы примерно одинаковы'
