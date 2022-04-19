# ZW-Steg
Python Command-Line Tool for Zero-Width Characters Steganography. <br>
Hide text in other text using invisible zero-width unicode characters.

Inspired by [Steganographr](https://github.com/neatnik/steganographr)

## How it Works
Chose a private and public message. The private message will be converted into binary data. The binary data will be mapped to three Zero-Width Characters. I will then be appended to the public message. The result is the public message with a hidden message‌‌​‌​​​⁠‌‌‌​‌​​⁠‌‌‌​‌​​⁠‌‌‌​​​​⁠‌‌‌​​‌‌⁠‌‌‌​‌​⁠‌​‌‌‌‌⁠‌​‌‌‌‌⁠‌‌‌​‌‌‌⁠‌‌‌​‌‌‌⁠‌‌‌​‌‌‌⁠‌​‌‌‌​⁠‌‌‌‌​​‌⁠‌‌​‌‌‌‌⁠‌‌‌​‌​‌⁠‌‌‌​‌​​⁠‌‌‌​‌​‌⁠‌‌​​​‌​⁠‌‌​​‌​‌⁠‌​‌‌‌​⁠‌‌​​​‌‌⁠‌‌​‌‌‌‌⁠‌‌​‌‌​‌⁠‌​‌‌‌‌⁠‌‌‌​‌‌‌⁠‌‌​​​​‌⁠‌‌‌​‌​​⁠‌‌​​​‌‌⁠‌‌​‌​​​⁠‌‌‌‌‌‌⁠‌‌‌​‌‌​⁠‌‌‌‌​‌⁠‌‌​​‌​​⁠‌​‌​​​‌⁠‌‌‌​‌‌‌⁠‌‌​‌​​⁠‌‌‌​‌‌‌⁠‌‌‌​​‌⁠‌​‌​‌‌‌⁠‌‌​​‌‌‌⁠‌​‌‌​​​⁠‌‌​​​‌‌⁠‌​‌​​​‌⁠‌​​‌‌​⁠‌‌​​​​‌⁠‌‌​​​‌​⁠‌​‌‌‌‌‌⁠‌‌​​​‌‌⁠‌‌​‌​​​⁠‌‌​​​​‌⁠‌‌​‌‌‌​⁠‌‌​‌‌‌​⁠‌‌​​‌​‌⁠‌‌​‌‌​​⁠‌‌‌‌​‌⁠‌​‌​​‌​⁠‌‌​‌​​‌⁠‌‌​​​‌‌⁠‌‌​‌​‌‌⁠‌​​​​​‌⁠‌‌‌​​‌‌⁠‌‌‌​‌​​⁠‌‌​‌‌​​⁠‌‌​​‌​‌⁠‌‌‌‌​​‌ through invisible/hidden unicode characters.

The default characters:

"\u2060", #WORD JOINER - as " " <br>
"\u200B", #ZERO WIDTH SPACE - as 0 <br>
"\u200C", #ZERO WIDTH NON-JOINER - as 1 <br>


All possible characters:

"\u2060", #WORD JOINER <br>
"\u200B", #ZERO WIDTH SPACE <br>
"\u200C", #ZERO WIDTH NON-JOINER <br>
"\u180E", #MONGOLIAN VOWEL SEPARATOR <br>
"\u200D", #ZERO WIDTH JOINER <br>
"\u200E", #LEFT-TO-RIGHT MARK <br>
"\u200F", #RIGHT-TO-LEFT MARK <br>
"\uFEFF", #ZERO WIDTH NO-BREAK SPACE <br>
"\u202A", #LEFT-TO-RIGHT EMBEDDING <br>
"\u202C", #POP DIRECTIONAL FORMATTING <br>
"\u202D", #LEFT-TO-RIGHT OVERRIDE <br>
"\u2062", #INVISIBLE TIMES <br>
"\u2063"  #INVISIBLE SEPARATOR <br>

## How to run
- download the python file
- run `python3 zw_steg.py`

```bash
 ______      __  ___ _
|_  /\ \    / / / __| |_ ___ __ _ 
 / /  \ \/\/ /  \__ \  _/ -_) _` |
/___|  \_/\_/   |___/\__\___\__, |
                            |___/ 

Options:
1. Encode/Hide Text
2. Decode/Reveal Text
3. Replace Zero Width Character
4. 'Brute-Force' Decoding
5. Exit

Choice:
```
