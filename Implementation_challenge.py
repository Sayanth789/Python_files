#Find the longest substring without repeating the character
# Given a string s, find the length of the longest substring without 
# repeating the characters
#Eg: input : "abcabcbb" # Output : 3 # the answer is "abc ", with length 3.
 
# Problem Solving Approach -Sliding window

"""
We use a set to store chars and a 2 pointer technique to keep track of the current substring.
Expand the window by adding chars until a duplicate is found
Shrink the window from the left  until there are no duplicates
keep track of the max: length found
"""
def length_of_longest_substring(s: str) -> int:
    char_set = set()
    left =  0
    max_length = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1  # Move the left pointer to shrink window

        char_set.add(s[right])    
        max_length = max(max_length, right - left + 1)
    return max_length    
# Testing the code
print(length_of_longest_substring("abcabcbb"))  # Expected:3
print(length_of_longest_substring("bbbbb")) # Expected: 1
print(length_of_longest_substring("pewkwew"))
print(length_of_longest_substring(""))

