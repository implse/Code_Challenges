# https://app.codesignal.com/challenge/cWB64385L6Fe6zD4D

# Each note in the chromatic scale corresponds to a sound wave, which has a unique frequency.

# The same set of notes appear in higher octaves (with higher frequencies), and in lower
# octaves (with lower frequencies), and there's a system called scientific pitch notation
# which distinguishes between notes in different octaves (for example, F\#3 is two octaves below F\#5)

# The magical property is that for any two notes separated by an octave (eg: A4 and A5),
# the ratio of their frequencies is exactly 2 - in other words, doubling a note's frequency is
# equivalent to ascending an octave! In this particular case, the frequency of A4 is 440 and the frequency of A5 is 880.

# With this information in mind, your task is to identify the frequency of the input note (provided in scientific pitch notation).

def noteFrequency(note):
    A4 = 440
    octave = 4
    Twelfth_root_of_two = 2**(1/12)
    semitone_distance = {"A": 0, "B": 2,"C": -9, "D": -7, "E": -5, "F": -4, "G": -2}
    note = [c for c in note]
    def f_zero(coef):
        if coef < 0:
            f0 = A4 / (2**abs(coef))
        elif coef >= 0:
            f0 = A4 * (2**coef)
        return f0
    # no flat or sharp
    if len(note) == 2:
        f0 = f_zero(int(note[1]) - octave)
        n = semitone_distance[note[0]]
    # sharp and flat
    if len(note) == 3:
        f0 = f_zero(int(note[2]) - octave)
        n = semitone_distance[note[0]]
        if note[1] == "#":
            n += 1
        if note[1] == "b":
            n -= 1
    return f0 * (Twelfth_root_of_two ** n)
