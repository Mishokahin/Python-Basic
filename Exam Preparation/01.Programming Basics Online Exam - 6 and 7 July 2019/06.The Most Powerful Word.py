import math
vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']
command = input()
word = 0
power = 0

while command != "End of words":
    is_vowel = False
    current_word = command
    current_power = 0
    if current_word[0] in vowels:
        is_vowel = True

    for char in command:
        current_power += ord(char)

    if is_vowel:
        current_power *= len(current_word)
    else:
        current_power = math.floor(current_power/3)

    if current_power > power:
        power = current_power
        word = current_word

    command = input()

print(f"The most powerful word is {word} - {power}")