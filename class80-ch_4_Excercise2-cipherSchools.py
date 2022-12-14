#pallindrome
# def is_palindrome(word):
#     reversed_word=word[::-1]
#     if word==reversed_word:
#         return True
#     else:
#         return False
# print(is_palindrome("yash"))
# print(is_palindrome("naman"))
     
def is_palindrome(word):
    return word==word[::-1]
print(is_palindrome("yash"))
print(is_palindrome("naman"))
