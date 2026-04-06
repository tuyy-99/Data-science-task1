def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0

    for char in text:
        if char in vowels:
            count += 1

    return count


sentence = input("Enter text: ")
total_vowels = count_vowels(sentence)

print("Number of vowels:", total_vowels)