# https://codefights.com/arcade/intro/level-6/6Wv4WsrsMJ8Y2Fwno

# Correct variable names consist only of Latin letters, digits and underscores and they can't start with a digit.

# Check if the given string is a correct variable name.

import re

def variableName(name):
    pattern = "^[a-z_]\w*$"
    return re.match(pattern, name) != None
