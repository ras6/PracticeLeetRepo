# Checking Anagram
# Time: o(1) 
# Space: O(1)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
