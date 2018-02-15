# https://codefights.com/interview-practice/task/FwAR7koSB3uYYsqDp

# Consider a special family of Engineers and Doctors. This family has the following rules:

# Everybody has two children.
# The first child of an Engineer is an Engineer and the second child is a Doctor.
# The first child of a Doctor is a Doctor and the second child is an Engineer.
# All generations of Doctors and Engineers start with an Engineer.

 #             E
 #        /         \
 #       E           D
 #     /   \        /  \
 #    E     D      D    E
 #   / \   / \    / \   / \
 #  E   D D   E  D   E E   D

# Given the level and position of a person in the ancestor tree above, find the profession of the person.
# Note: in this tree first child is considered as left child, second - as right.

# The idea is based on the fact that profession of a person depends on following two.

#     1- Profession of parent.
#     2 - Position of node : If position of a node is odd, then its profession is same as its parent. Else profession is different from its parent.

# We recursively find the profession of parent, then use point 2 above to find the profession of current node.
    
def findProfession(level, pos):
    if level == 1:
        return "Engineer"
    if pos % 2 == 1:
        return findProfession(level - 1, (pos+1)/2)
    else:
        if findProfession(level - 1, pos/2) == "Doctor":
            return "Engineer"
        else:
            return "Doctor"
