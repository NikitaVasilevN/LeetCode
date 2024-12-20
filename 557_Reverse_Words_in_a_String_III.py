# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

# Example 1:

# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# Example 2:

# Input: s = "Mr Ding"
# Output: "rM gniD"
 

# Constraints:

# 1 <= s.length <= 5 * 104
# s contains printable ASCII characters.
# s does not contain any leading or trailing spaces.
# There is at least one word in s.
# All the words in s are separated by a single space.



class Solution_1:
    def reverseWords(self, s: str) -> str:
        list_res = []
        for str in s.split(' '):
            list_res.append(str[::-1])
        return ' '.join(list_res)
    
class Solution_2:
    def reverseWords(self, s: str) -> str:
        str_list = s.split(' ')
        for i in range(len(str_list)):
            str_list[i] = str_list[i][::-1]
        return ' '.join(str_list)