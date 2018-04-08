# https://www.hackerrank.com/challenges/tree-huffman-decoding/problem

# Huffman coding assigns variable length codewords to fixed length input characters based on their frequencies.
# More frequent characters are assigned shorter codewords and less frequent characters are assigned longer codewords.
# A Huffman tree is made for the input string and characters are decoded based on their position in the tree.
# We add a '0' to the codeword when we move left in the binary tree and a '1' when we move right in the binary tree.

class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None

def decodeHuff(root , s):
    current = root
    decode = []
    for c in s:
        if int(c) == 1:
            current = current.right
        elif int(c) == 0:
            current = current.left
        if current.right == None and current.left == None:
            decode.append(current.data)
            current = root
    print(''.join(decode))
