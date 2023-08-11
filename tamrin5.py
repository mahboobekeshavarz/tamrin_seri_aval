txt = 'The Quick Brown Fox'
str1 = ''

for char in txt:
    if 64 < ord(char) < 91:
        char = chr(ord(char) + 32)
        str1 += char
    elif 96 < ord(char) < 123:
        char = chr(ord(char) - 32)
        str1 += char
    else:
        char = chr(ord(char))
        str1 += char

print(str1)