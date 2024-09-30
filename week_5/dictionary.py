# dictionary = a collection of {key:value} pairs ordered and 
#       changeable. No duplicates.

capitals = {"USA" : "Washington D.C.",
            "India" : "New Delhi",
            "China" : "Beijing",
            "Russia" : "Moscow",
            "Japan" : "Tokyo",
            "South Korea" : "Seoul"}

# print(dir(capitals)) # "dir" shows you methods of the dictionary
# print(help(capitals)) # "help" gives you back documentation of each of the methods

# print(capitals.get("Japan"))

# if capitals.get("Russia"):
#     print("That capital exists")
# else:
#     print("That capital doesn't exist")

# capitals.update({"Germany" : "Berlin"}) # "update" is how you can add changes in your dictionary
# capitals.update({"USA" : "Detroit"})

# capitals.pop("China") # "pop" will remove the typed item
# capitals.popitem() # "popitem" will remove the last text in the dictionary
# capitals.clear() # "clear" will remove all items in the dictionary

# keys = capitals.keys() # "keys" method will return only the keys and not the values. In this example, only the countries names will be printed

# for key in capitals.keys():
#     print(key)

# values = capitals.value() "values" method will return only the values and not the keys. In this example, only the capitals names will be printed

# for value in capitals.values():
#     print(value)

# items = capitals.items()
# for key, value in capitals.item():
#     print(f"{key}: {value}")