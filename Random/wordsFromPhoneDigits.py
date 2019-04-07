# Before advent of QWERTY keyboards, texts and numbers were placed on the same key.
# For example 2 has “ABC” if we wanted to write anything starting with ‘A’ we need to type key 2 once.
# If we wanted to type ‘B’, press key 2 twice and thrice for typing ‘C’. below is picture of such keypad.


# For example if input number is 234, possible words which can be formed are (Alphabetical order):

# adg adh adi aeg aeh aei afg afh afi bdg bdh bdi beg beh bei bfg bfh bfi cdg cdh cdi ceg ceh cei cfg cfh cfi

# Define keypad

keypad = {
    0: '0',
    1: '1',
    2: 'ABC',
    3: 'DEF',
    4: 'GHI',
    5: 'JKL',
    6: 'MNO',
    7: 'PQRS',
    8: 'TUV',
    9: 'WXYZ'
}

def possible_words(digits):
    # store combinations
    letters = list()

    # helper function
    def recursive(current, i):
        # Base case
        if len(current) == len(digits):
            letters.append(current)
            return

        current_letters = keypad[int(digits[i])]
        for l in current_letters:
            # Recursive case
            recursive(current + l, i + 1)
    # function call
    recursive('', 0)
    return letters

# Test

print(possible_words('22'))
