def is_palindrome(text):
    """This code checks if the string is a
    palindrome!
    It takes the argument and asigns the value to a new
    variable called 'reverse_order' by iterating the whole string backwards
    and checking if value is same as the original string!"""
    reverse_order = text[::-1]
    if reverse_order == text:
        return True
    else: 
        return False
    

print(is_palindrome("kajak"))