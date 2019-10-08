def packetDescrambler(seq, fragmentData, n):

    # Construct hash table seq/fragment
    sequence = {}
    for i in range(len(seq)):
        id = seq[i]
        fragment = fragmentData[i]
        if id not in sequence:
            sequence[id] = [fragment]
        else:
            sequence[id].append(fragment)

    ids = list(sequence.keys())
    ids.sort()
    message = ""

    for i in range(len(ids)):
        if i != ids[i]:
            return ""
        fragment = validate_fragment(sequence[ids[i]], n*0.5)
        if fragment != None:
            message += fragment
    return message if len(message) >= n and message[-1] == "#" or message == "#" else ""

def validate_fragment(lst, threshold):
    for fragment in set(lst):
        if lst.count(fragment) >= threshold:
            return fragment
    return None















# Old
from math import ceil
def packetDescrambler(seq, fragmentData, n):
    # n : number of copies of each fragment (50% of n to validate)
    # seq : number or id of the fragment
    # fragmentData : single character from the message
    # return : reconstruct message or empty string

    # rules :
        #1 50% of n
        #2 last fragment "#"
        #3 no gap

    # Validate sequence (increasing order)
    ids = list(set(id for id in seq))
    if validate_seq(ids) == False:
        return ""

    # Construct hash table seq/fragment
    sequence = {}
    for i in range(len(seq)):
        id = seq[i]
        if id not in sequence:
            sequence[id] = [fragmentData[i]]
        else:
            sequence[id].append(fragmentData[i])

    message = ""
    threshold = math.ceil(n*0.5)
    for id in ids:
        validate_id = validate_fragment(sequence[id], threshold)
        #print(validate_id)
        if validate_id != None:
            message += validate_id
    return message if len(message) >= n and message[-1] == "#" or message == "#" else ""

def validate_fragment(lst, threshold):
    fragment = ""
    count = 0
    # searching for the most frequent fragment
    # and check if 50% of n to be validate
    for value in lst:
        compare = max(count, lst.count(value))
        if compare  > count:
            count = compare
            fragment = value
    if count >= threshold:
        return fragment
    return None

def validate_seq(ids):
    for i in range(1, len(ids)):
        if ids[i-1] != ids[i]-1:
            return False
    return True

# last

from math import ceil
def packetDescrambler(seq, fragmentData, n):
    # n : number of copies of each fragment (50% of n to validate)
    # seq : number or id of the fragment
    # fragmentData : single character from the message
    # return : reconstruct message or empty string

    # rules :
        #1 50% of n
        #2 last fragment "#"
        #3 no gap

    # Validate sequence (increasing order)
    ids = set(seq)
    if validate_seq(ids) == False:
        return ""

    # Construct hash table seq/fragment
    sequence = {}
    for i in range(len(seq)):
        id = seq[i]
        fragment = fragmentData[i]
        if id not in sequence:
            sequence[id] = [fragment]
        else:
            sequence[id].append(fragment)

    message = ""
    threshold = math.ceil(n*0.5)
    for id in ids:
        validate_id = validate_fragment(sequence[id], threshold)
        #print(validate_id)
        if validate_id != None:
            message += validate_id
    return message if len(message) >= n and message[-1] == "#" or message == "#" else ""

def validate_fragment(lst, threshold):
    fragment = ""
    count = 0
    set_lst = set(lst)
    # searching for the most frequent fragment
    # and check if 50% of n to be validate
    #for value in lst:
    for value in set_lst:
        compare = max(count, lst.count(value))
        if compare  > count:
            count = compare
            fragment = value
    if count >= threshold:
        return fragment
    return None

def validate_seq(ids):
    ids = list(ids)
    for i in range(1, len(ids)):
        if ids[i-1] != ids[i]-1:
            return False
    return True
