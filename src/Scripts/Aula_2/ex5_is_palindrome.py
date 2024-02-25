"""
Exercise 5: Palindrome Verification Recursively
A palindrome is a word, phrase, number, or other sequence of
characters that reads the same forward and backward (disregarding
spaces, punctuation, and differences in uppercase and lowercase).
Examples include "racecar", "Ana" and "12321".

Objective: Write a recursive function in Python that checks if
a given string is a palindrome.

Instructions:
• The function should ignore spaces, punctuation, and differences between
uppercase and lowercase letters.
• The function should return True if the string is a palindrome and
False otherwise.
• Do not use ready-made language functions that do the inversion
of the string or direct comparisons of substrings.

Tips:
1. Consider cleaning the string before starting the verification, removing
spaces and punctuation, and converting everything to lowercase.
2. Think about how you can compare the first and last
character of the string, remove them from consideration and repeat the
process recursively.
3. Remember to clearly define the base case that will stop the
recursion.

"""

accents = {
    'á':'a', 'é':'e', 'í':'i', 'ó':'o', 'ú':'u', 'â':'a', 'ê':'e', 'î':'i', 'ô':'o', 'û':'u',
    'ã':'a', 'õ':'o', 'ç':'c', 'à':'a', 'è':'e', 'ì':'i', 'ò':'o', 'ù':'u', 'ä':'a', 'ë':'e',
    'ï':'i', 'ö':'o', 'ü':'u', 'Á':'A', 'É':'E', 'Í':'I', 'Ó':'O', 'Ú':'U', 'Â':'A', 'Ê':'E',
    'Î':'I', 'Ô':'O', 'Û':'U', 'Ã':'A', 'Õ':'O', 'Ç':'C', 'À':'A', 'È':'E', 'Ì':'I', 'Ò':'O',
    'Ù':'U', 'Ä':'A', 'Ë':'E', 'Ï':'I', 'Ö':'O', 'Ü':'U'
}

def is_palindrome(s):
    """
    This function recives a sequence of only alphanumeric characters
    and return if the inputes sequence is a palindrome(True) or not(False)
    """
    if len(s) == 0:
        return True
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    return False

def remove_accents(s):
    """
    This function remove all accents from the inputed string
    """
    return ''.join(accents.get(i, i) for i in s)

def remove_punctuation(s):
    """
    This function remove all ponctuations from the inserted
    string.
    """
    punctuation = '''!()-[]{};:'"\\,<>./?@#$%^&*_~'''
    return ''.join(c for c in s if c not in punctuation)

def prepare_string(s):
    """
    This function transforms the sequence entered by the user,
    treating it so that the second function works perfectly.
    """
    s = s.replace(" ", "")
    s = remove_accents(s)
    s = remove_punctuation(s)
    return s.lower()

print(is_palindrome(prepare_string(input("Enter to find out if it's a palindrome: "))))
