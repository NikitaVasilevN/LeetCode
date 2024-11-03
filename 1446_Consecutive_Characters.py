# The power of the string is the maximum length of a non-empty substring that contains only one unique character.

# Given a string s, return the power of s.

 

# Example 1:

# Input: s = "leetcode"
# Output: 2
# Explanation: The substring "ee" is of length 2 with the character 'e' only.
# Example 2:

# Input: s = "abbcccddddeeeeedcba"
# Output: 5
# Explanation: The substring "eeeee" is of length 5 with the character 'e' only.
 

# Constraints:

# 1 <= s.length <= 500
# s consists of only lowercase English letters.

class Solution:
    def maxPower(self, s: str) -> int:
        max_lenght = 1 if len(s) == 1 else 0
        counter = 1
        for i in range(1, len(s)):
            if s[i-1] == s[i]:
                counter+=1
            else:
                if max_lenght < counter:
                    max_lenght = counter
                counter = 1
        return max_lenght if max_lenght > counter else counter
    
class Solution_cache:
    def maxPower(self, s: str) -> int:
        lenght = 1 
        prev_c = ''
        list_lenght = []

        for i in range(len(s)):

            if prev_c == s[i]:
                lenght += 1

                if i == len(s)-1:
                    list_lenght.append(lenght)

            else:
                list_lenght.append(lenght)
                lenght = 1
            prev_c = s[i]
        return max(list_lenght)



