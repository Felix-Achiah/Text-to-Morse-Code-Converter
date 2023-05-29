# A text-based Python program to convert Strings into Morse Code.

# Morse Code Data
morse_code_data = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    ' ': '/',
    ',': '--..--',
    '?': '..--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
}

# Enter text 
text = input("Enter the text to convert to its equivalent Morse Code: \n")

# Loop through the entered text and append each letter to the list variable 'letters'
letters = [char for char in text.upper()]

text_convert = [morse_code_data[letter] for letter in letters if letter in morse_code_data]

# Results of text converted to morse code.
morse_code = "".join(text_convert)


