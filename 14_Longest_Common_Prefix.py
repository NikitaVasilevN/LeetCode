###################
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.
###################


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        strs.sort(key = lambda x : len(x))
        count = 0
        str = ''

        for letter_i in range(len(strs[0])):
            for word in strs[1:]:
                if strs[0][letter_i] == word[letter_i]:
                    count += 1
                else:
                    break
            if count != len(strs[1:]):
                break
            else:
                str += strs[0][letter_i]
                count = 0
        return str
