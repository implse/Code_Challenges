# https://app.codesignal.com/interview-practice/task/cAXEnPyzknC5zgd7x

# You need to climb a staircase that has n steps, and you decide to get some extra exercise by jumping up the steps.
# You can cover at most k steps in a single jump.
# Return all the possible sequences of jumps that you could take to climb the staircase, sorted.


def climbingStaircase(n, k):
    seq = list()
    steps = list()
    climbingStaircaseHelper(seq, steps, n, k)
    return seq

def climbingStaircaseHelper(seq, steps, n, k):
    # base case
    if n == 0:
        seq.append(list(steps))
    else:
        for i in range(1, k+1):
            if i <= n:
                # choose
                steps.append(i)
                # explore
                climbingStaircaseHelper(seq, steps, n - i, k)
                # un-choose
                steps.pop()
