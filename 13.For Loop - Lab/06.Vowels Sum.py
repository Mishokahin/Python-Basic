char_map = {"a": 1, "e": 2, "i": 3, "o": 4, "u": 5}
input_text = input()
vowels_sum = 0

for char in input_text:
    if char in char_map:
        vowels_sum += char_map[char]

print(vowels_sum)