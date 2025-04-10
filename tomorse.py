morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
    '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...',
    ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.'
}


def text_to_morse(text):
    words = text.upper().split()
    morse_words = []

    for word in words:
        morse_chars = []
        for char in word:
            if char in morse_code_dict:
                morse_chars.append(morse_code_dict[char])
            else:
                print(f"Ignoring unsupported character: {char}")
        morse_words.append(' '.join(morse_chars))

    return ' / '.join(morse_words)



"""
user_input = input("Enter your message to convert to Morse code: ")
morse_translation = text_to_morse(user_input)
print("\nMorse Code Output:")
print(morse_translation)
"""

#print(text_to_morse("hello world"))