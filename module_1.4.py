my_string = input("Enter your sentence: ")
"""
    Если не считать пробел за символ, хотя везде это символ
    print(f"Number of characters entered {len(my_string.replace(' ',''))}")
"""
print(f"Number of characters entered {len(my_string)}")
print(f"Sentence in upper case:\n{my_string.upper()}")
print(f"Sentence in lower case:\n{my_string.lower()}")
print(f"Sentence in without spaces case:\n{my_string.replace(' ','')}")
print(f"Sentence in without spaces case:\n{my_string[0]}")
print(f"Sentence in without spaces case:\n{my_string[len(my_string)-1]}")