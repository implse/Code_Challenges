def packetDescrambler(seq, fragmentData, n):
    # build sequence_ids dict
    sequence_ids = {}
    for i in range(len(seq)):
        id = seq[i]
        fragment = fragmentData[i]
        if id not in sequence_ids.keys():
            sequence_ids[id] = [fragment]
        else:
            sequence_ids[id].append(fragment)
    ids = sorted(list(sequence_ids.keys()))
    message = ""

    for i in range(len(ids)):
        # test increase id order 0, 1, 2 ...
        if i != ids[i]:
            return ""
        # test fragment
        fragment = validate_fragment(sequence_ids[i], n)
        if fragment == False:
            return ""
        message += fragment
    return validate_message(message)

def validate_fragment(lst, n):
    threshold = n * 0.5
    for fragment in set(lst):
        if lst.count(fragment) > threshold:
            return fragment
    return False

def validate_message(message):
    return message if message[-1] == "#" and message.count('#') == 1 else ""

# Test
seq = [1, 1, 0, 0, 0, 2, 2, 2]
fragments = ['+', '+', 'A', 'A', 'B', '#', '#', '#']
n = 3
print(packetDescrambler(seq, fragments, n))
