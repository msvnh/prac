from typing import List

s = "abcdabcd"
# hash_set = set(s)
# for e in hash_set:
#     print(e)

hash_map = {}
for char in s:
    hash_map[char] = 1 + hash_map.get(char, 0)

print(hash_map)