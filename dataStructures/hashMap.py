'''
Hashing mapping is used to store data in key value pairs.
It is implemented through the dictionary in Python
Its average case is O(1), so it is very fast.
You need to avoid collisions, where two values are assigned the same key.
You need to avoid load factors greate then 0.7
'''

testing = {
    "Tyler": 22,
    "Noah": 22,
    "Caity": 21
}

testing["Franklin"] = 22

tyler_age = testing.get("Tyler") # returns value of given key
testing_items = testing.items() # returns all items in a dictionary
testing_keys = testing.keys() # returns all keys in a dictionary
testing_values = testing.values() # returns all values in a dictionary
testing.pop("Franklin") # removes a value from a dictionary given a key
testing.update({"Bryce": 23}) # Adds to a dictionary
