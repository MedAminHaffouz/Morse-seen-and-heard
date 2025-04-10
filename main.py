from tomorse import text_to_morse

import sounddevice as sd
import numpy as np
import time

# Morse timing constants (in seconds)
DOT_DURATION = 0.1
DASH_DURATION = DOT_DURATION * 3
SYMBOL_SPACE = DOT_DURATION
CHAR_SPACE = DOT_DURATION * 3
WORD_SPACE = DOT_DURATION * 7

def generate_tone(freq=800, duration=0.1):
    sample_rate = 44100
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    audio = 0.5 * np.sin(2 * np.pi * freq * t)
    return audio

def play_morse(morse_code):
    for symbol in morse_code:
        if symbol == '.':
            sd.play(generate_tone(duration=DOT_DURATION), samplerate=44100)
            sd.wait()
            time.sleep(SYMBOL_SPACE)
        elif symbol == '-':
            sd.play(generate_tone(duration=DASH_DURATION), samplerate=44100)
            sd.wait()
            time.sleep(SYMBOL_SPACE)
        elif symbol == ' ':
            time.sleep(CHAR_SPACE - SYMBOL_SPACE)  # Already waited SYMBOL_SPACE after last symbol
        elif symbol == '/':
            time.sleep(WORD_SPACE - SYMBOL_SPACE)  # Account for previous symbol space

# Test with verified Morse code

text=input()
code=text_to_morse(text)
print(len(code)+" symbols")
play_morse(code)