"""
         ______      __  ___ _            
        |_  /\ \    / / / __| |_ ___ __ _ 
         / /  \ \/\/ /  \__ \  _/ -_) _` |
        /___|  \_/\_/   |___/\__\___\__, |
                                    |___/
                            
Python Command-Line Tool for Zero-Width Characters Steganography.
Hide text in other text using invisible zero-width unicode characters.

by MayADevBe
https://mayadevbe.me/

MIT License
Copyright (c) 2022 MayADevBe
"""

import itertools

# Unicode
# 'WORD JOINER' (U+2060) 0xE2 0x81 0xA0
# 'ZERO WIDTH SPACE' (U+200B) 0xE2 0x80 0x8B
# 'ZERO WIDTH NON-JOINER' (U+200C) 0xE2 0x80 0x8C
# ...

bin_list = [" ","0","1"] # mapping of binary string for Zero-Width Characters
char_list = ["\u2060", "\u200B", "\u200C"] # default Zero-Width Characters to do encoding

possible_zero_width_chars = [ # list of possible Zero-Width Characters to use for encoding
    "\u2060", #WORD JOINER
    "\u200B", #ZERO WIDTH SPACE
    "\u200C", #ZERO WIDTH NON-JOINER
    "\u180E", #MONGOLIAN VOWEL SEPARATOR
    "\u200D", #ZERO WIDTH JOINER
    "\u200E", #LEFT-TO-RIGHT MARK
    "\u200F", #RIGHT-TO-LEFT MARK
    "\uFEFF", #ZERO WIDTH NO-BREAK SPACE
    "\u202A", #LEFT-TO-RIGHT EMBEDDING
    "\u202C", #POP DIRECTIONAL FORMATTING
    "\u202D", #LEFT-TO-RIGHT OVERRIDE
    "\u2062", #INVISIBLE TIMES
    "\u2063"  #INVISIBLE SEPARATOR
] 

# Encode the secret text with help of Zero-Width Characters and hide in the open text
def encode(secret_text, open_text):
    bin_text = ""
    encoded_text = open_text
    bin_text = ' '.join(format(ord(x), 'b') for x in secret_text)
    for b in bin_text:
        encoded_text += char_list[bin_list.index(b)]
    return encoded_text

# Decode Zero-Width Character string
def decode(open_text):
    bin_text = ""
    for w in open_text:
        if w in char_list:
            bin_text += bin_list[char_list.index(w)]
    bin_val = bin_text.split()
    secret_text = ""
    for b in bin_val:
        secret_text += chr(int(b, 2))
    return secret_text

# "Brute Forces" all options of possible Zero-Width Characters
# Use if combination of Zero-Width Characters is not known
def brute_decode(open_text):
    used_chars = []
    for p in possible_zero_width_chars:
        if p in open_text:
            used_chars.append(p)
    if len(used_chars) != 3:
        return "Cannot decode!"

    possible_secret_texts = []

    perms = list(itertools.permutations(used_chars))
    for perm in perms:
        try:
            bin_text = ""
            for w in open_text:
                if w in char_list:
                    bin_text += bin_list[perm.index(w)]
            bin_val = bin_text.split()
            secret_text = ""
            for b in bin_val:
                secret_text += chr(int(b, 2))
            possible_secret_texts.append(secret_text)
        except:
            pass
    return possible_secret_texts

# Prints List with Zero-Width Chars as Hex
def string_list(the_list):
    the_string = ""
    i = 1
    for l in the_list:
        the_string += str(i) + ": " + str(l.encode()) + ", "
        i += 1
    return the_string[:-2]

# Command-line tool
def main():
    print(" ______      __  ___ _            ")
    print("|_  /\ \    / / / __| |_ ___ __ _ ")
    print(" / /  \ \/\/ /  \__ \  _/ -_) _` |")
    print("/___|  \_/\_/   |___/\__\___\__, |")
    print("                            |___/")
    print()

    choice = 0
    while choice != 5:
        print("Options:")
        print("1. Encode/Hide Text")
        print("2. Decode/Reveal Text")
        print("3. Replace Zero Width Character")
        print("4. 'Brute-Force' Decoding")
        print("5. Exit")
        print()
        choice = int(input("Choice: "))
        print()
        match choice:
            case 1:
                secret_text = input("Text to be encoded: ")
                open_text = input("Text to be shown: ")
                print()
                encoded_text = encode(secret_text, open_text)
                print('"' + encoded_text + '"')
                file = input("Save in file: ")
                with open(file, 'w', encoding="utf-8") as f:
                    f.write(encoded_text)
                print("Saved in file: " + file)
            case 2:
                text = input("Text to be decoded: ")
                secret_text = decode(text)
                print(secret_text)
            case 3: # Allows to change the default Zero-Width Characters list for the encoding
                print("Currently: " + " ".join(bin_list) + " -> " + string_list(char_list))
                print("Possible characters: " + string_list(possible_zero_width_chars))
                i = int(input("What position you want to change: "))
                j = int(input("Character you choose: "))
                print()
                if (i <= len(bin_list) & j <= len(possible_zero_width_chars)):
                    bin_list[i] = possible_zero_width_chars[j]
                print("Updated: " + " ".join(bin_list))
            case 4:
                text = input("Text to be decoded: ")
                print()
                secret_texts = brute_decode(text)
                if secret_texts == "Cannot decode!":
                    print(secret_texts)
                else:
                    print("Possible texts: ")
                    for t in secret_texts:
                        print(t)
            case 5:
                print("Exiting")
            case _:
                print("Wrong Input!")
        print()
        print()

if __name__ == '__main__':
    main()
