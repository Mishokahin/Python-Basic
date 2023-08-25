import string
first_letter = input()
second_letter = input()
third_letter = input()

combinations = [f"{i}{j}{k}"
                for i in string.ascii_lowercase
                if second_letter >= i >= first_letter and i != third_letter
                for j in string.ascii_lowercase
                if second_letter >= j >= first_letter and j != third_letter
                for k in string.ascii_lowercase
                if second_letter >= k >= first_letter and k != third_letter]

print(*combinations, len(combinations))