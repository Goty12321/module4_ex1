def is_palyndrome(text):
    reverse_order = ""
    for letter in text:
        reverse_order += letter
    if reverse_order == text:
        return True
    else: 
        return False

print(is_palyndrome("But"))