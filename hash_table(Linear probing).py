print '3. Создать приложение, реализующее хэш-таблицу для хранения объектов произвольного класса (в классе должно быть как минимум одно текстовое поле, на основе которого вычисляется хэш) с методом разрешения коллизий - “probing”(closed hashing). В качестве хэш-функции использовать рассмотренную на лекции (слайд 12). К качестве метода “probing” просматривать каждую следующую ячейку ХТ. Продемонстрировать работу разработанной ХТ.'

class Car(object):
    model = ""
    year = 0
    plate_number = ""

    def __init__(self, model, year, plate_number):
        self.model = model
        self.year = year
        self.plate_number = plate_number

def make_car(model, year, plate_number):
    car = Car(model, year, plate_number)
    return car

make_car('Toyota', 2014, '90KVW23')



class MyHashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.slots = [None] * self.capacity
        self.count = 0

    # def __str__(self):
    #     return str(self.slots)

    # def __contains__(self, item):
    #     return self.search(item) != -1

    # def __len__(self):
    #     return self.count

    def hash_function(self, key):
        return hash(key) % self.capacity

    def find_slot(self, object):
        index = self.hash_function(object.plate_number)
        while self.slots[index] is not None and self.slots[index] != object:
            index = (index + 1) % self.capacity
        return index


    capacity = 10
    index = 1
    hash_table[1]
    (1+1)%10 = 2


    def insert(self, key):
        slot = self.find_slot(key)
        if self.slots[slot] != key:
            self.slots[slot] = key
            self.count += 1

    def search(self, key):
        i = self.find_slot(key)
        if self.slots[i] is not None:
            return i
        return -1




print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
toyota = make_car('Toyota', 2014, '90KVW23')
bmw = make_car('BMW', 2015, 'NVP9021')
infinity = make_car('Infinity', 2012, '12POE34')
acura = make_car('Acura', 2017, '37PVE12')
print toyota.year
my_table = MyHashTable(97)
my_table.insert(toyota)
my_table.insert(bmw)
my_table.insert(infinity)
my_table.insert(acura)
print 'total objects in hash_table:',my_table.count
print my_table.slots
