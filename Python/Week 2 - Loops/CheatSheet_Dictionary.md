| 1. Accessing & Searching |                            |                                                                                            |
|--------------------------|----------------------------|--------------------------------------------------------------------------------------------|
| **Method**                   | **Syntax**                     | **Description**                                                                                |
| get()                    | d.get(key, default)        | Returns value for key. Returns default (or None) if key is missing. Prevents KeyErrors.    |
| keys()                   | d.keys()                   | Returns a dynamic view of all keys in the dictionary.                                      |
| values()                 | d.values()                 | Returns a dynamic view of all values.                                                      |
| items()                  | d.items()                  | Returns a view of (key, value) tuples. Great for looping.                                  |
|                          |                            |                                                                                            |
| 2. Adding & Updating     |                            |                                                                                            |
| **Method**                   | **Syntax**                     | **Description**                                                                                |
| update()                 | d.update(other_dict)       | Updates the dictionary with pairs from another dict or iterable. Overwrites existing keys. |
| setdefault()             | d.setdefault(key, default) | Returns value if key exists. If not, inserts key with the default value.                   |
| copy()                   | d.copy()                   | Returns a shallow copy of the dictionary.                                                  |
|                          |                            |                                                                                            |
| 3. Removing Data         |                            |                                                                                            |
| **Method**                   | **Syntax**                     | **Description**                                                                                |
| pop()                    | d.pop(key)                 | Removes the key and returns its value. Raises KeyError if not found.                       |
| popitem()                | d.popitem()                | Removes and returns the last inserted (key, value) pair.                                   |
| clear()                  | d.clear()                  | Removes all items, leaving an empty dictionary {}.                                         |
