# # inlementation using deque...
# from collections import deque

# stack = deque()

# stack.append("vicky")
# print(stack)

# stack.append("kumar")
# stack.append("bihar")
# print(stack)
# print(stack.pop())
# print(stack)


class Solution:
   def isPalindrome(x: int) -> bool:
    # negative numbers are not palindrome
    if x < 0:
        return False
    # convert number to string and check
    s = str(x)
    return s == s[::-1]

# Examples
print(isPalindrome(121))   # True
print(isPalindrome(-121))  # False
print(isPalindrome(10))    # False

           