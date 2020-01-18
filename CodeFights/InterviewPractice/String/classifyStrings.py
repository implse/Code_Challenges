def classifyStrings(s):
    vowels_check = vowels(s)
    #print(vowels_check)
    consonants_check = consonants(s)
    #print(consonants_check)

    if vowels_check == "bad" or consonants_check == "bad":
        return "bad"
    elif vowels_check == "mixed" or consonants_check == "mixed":
        return "mixed"

    return "good"

def vowels(str):
    for i in range(len(str)-2):
        substring = str[i:i+3]
        count = 0
        flag = 0
        for char in substring:
            if char in "aeiou":
                count += 1
                if count == 3:
                    return "bad"
            if char == "?":
                flag += 1
            if count + flag == 3:
                return "mixed"
        return "good"

def consonants(str):
        for i in range(len(str)-4):
            substring = str[i:i+5]
            print(substring)
            count = 0
            flag = 0
            for char in substring:
                if char in "bcdfghjklmnpqrstvwxyz":
                    count += 1
                    if count == 5:
                        return "bad"
                if char == "?":
                    flag += 1
                if count + flag == 5:
                    return "mixed"
        return "good"


s = "typ?asdf?relkhfd"
print(classifyStrings(s))
