"""String utility functions for common text operations."""

def reverse_string(text):
    """Reverse a string."""
    return text[::-1]

def is_palindrome(text):
    """Check if a string is a palindrome."""
    clean = text.lower().replace(' ', '')
    return clean == clean[::-1]

def capitalize_words(text):
    """Capitalize the first letter of each word."""
    return ' '.join(word.capitalize() for word in text.split())

def remove_duplicates(text):
    """Remove duplicate characters from a string."""
    seen = set()
    result = []
    for char in text:
        if char not in seen:
            result.append(char)
            seen.add(char)
    return ''.join(result)
