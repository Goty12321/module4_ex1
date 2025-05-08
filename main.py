def is_palindrome(text):
    reverse_order = ""
    for letter in text:
        reverse_order += letter
    if reverse_order == text:
        return True
    else: 
        return False

print(is_palindrome("But"))