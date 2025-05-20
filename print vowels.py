text = ' This quick brown fox jumps over the lazy dog'

converted = text.lower()

for char in converted:
    if char in 'aeiou':
        print(char)
    else:
        print(f"{char}:is not the vowel")