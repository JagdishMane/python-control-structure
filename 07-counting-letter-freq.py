text = "hello worldddddd"
letter_frequency = {}

for char in text:
    if char.isalpha():
        char = char.lower()
        if char in letter_frequency:
            letter_frequency[char] += 1
        else:
            letter_frequency[char] = 1
        print(letter_frequency)
print("Letter Frequency")
for letter, freq in letter_frequency.items():
    print(f"Letter: {letter}, Frequency: {freq}")