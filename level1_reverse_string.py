def reverse_text(text):
    return text[::-1]


user_text = input("Enter a word or sentence: ")
reversed_text = reverse_text(user_text)

print("Reversed string:", reversed_text)