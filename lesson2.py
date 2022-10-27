# Dicts
# Methods forms a new dict from list. The keys will be as elements in the list
# some_list = ["+7", "+6", "+5", "+4"]
# some_dict = dict.fromkeys(some_list, "код страны")
# print(some_dict)
#.copy() - copies the dict and returns the new dict
# some_dict = {True: 1, False: "Ложь", "list": [1, 2, 3], 5: 5}
# some_dict2 = some_dict.copy()
# some_dict2[True] = 2
#
# print(some_dict)
# print(some_dict2)
#.get() - returns keys value in the some dict:

# some_dict = {True: 1, False: "Ложь", "list": [1, 2, 3], 5:5}
#
# print(some_dict.get("list"))

# some_dict = {True: 1, False: "Ложь", "list": [1, 2, 3], 5:5}
#
# print(some_dict.get(3, False))

#.setdefault() - set some key with default value None, if key does not exists

# some_dict = {True: 1, False: "Ложь", "list": [1, 2, 3], 5:5}
#
# print(some_dict.setdefault(3))

#.pop() - deletes key and value from dict and returns it

# some_dict = {True: 1, False: "Ложь", "list": [1, 2, 3], 5: 10}
#
# print(some_dict.pop(5))
# print(some_dict)

#.popitem() - deletes last key and value and returns a tuple

# some_dict = {True: 1, False: "Ложь", "list": [1, 2, 3], 5: 10}
#
# print(some_dict.popitem())

#.keys() - returns all keys of the dict

# some_dict = {True: 1, False: "Ложь", "list": [1, 2, 3], 5: 10}
#
# print(some_dict.keys())

# for cycles:

# some_dict = {True: 1, False: "Ложь", "list": [1, 2, 3], 5: 10}
#
# for x in some_dict:
#     print(x)

#.values() returns a list of values of some dict

# some_dict = {True: 1, False: "Ложь", "list": [1, 2, 3], 5: 10}
#
# print(some_dict.values())

# for cycle for values:
# some_dict = {True: 1, False: "Ложь", "list": [1, 2, 3], 5: 10}
#
# for x in some_dict.values():
#     print(x)

#for cycle for keys and values, it will return a tuple. Before we will execute it we need to call .items() method which returns key value in tuple:

# some_dict = {True: 1, False: "Ложь", "list": [1, 2, 3], 5: 10}
#
# for x in some_dict.items():
#     print(x)

#for cycle for key and values in dict:

# some_dict = {True: 1, False: "Ложь", "list": [1, 2, 3], 5: 10}
#
# for key, value in some_dict.items():
#     print(key, value)

#.update() - unites two dicts into one and rewrites the already existig keys with values:

# some_dict = {True: 1, False: "Ложь", "list": [1, 2, 3], 5: 10}
#
# some_dict_2 = {2: "two", 3: "three"}
#
# some_dict.update(some_dict_2)
# print(some_dict)

# another way to unite and update the several dicts:

# some_dict = {True: 1, False: "Ложь", "list": [1, 2, 3], 5: 10}
# some_dict_2 = {2: "two", 3: "three"}
#
# some_dict_3 = {**some_dict, **some_dict_2}
# print(some_dict_3)

# another way to unite and update the several dicts available from 3.9:

# some_dict = {True: 1, False: "Ложь", "list": [1, 2, 3], 5: 10}
# some_dict_2 = {2: "two", 3: "three"}
# some_dict_3 = some_dict | some_dict_2
# print(some_dict_3)