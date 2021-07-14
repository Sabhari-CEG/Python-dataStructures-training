#Subsequently we are presented with a different set of options,
# and depending on the series of choices made either a goal state or a dead end is reached.
# If it is the latter, we must backtrack to a previous node and traverse a different branch.

def BackTrack(n,s):
    if n == 1:
        return s
    return [digit+bits for digit in BackTrack(1,s) for bits in BackTrack(n-1,s)]

if __name__ == '__main__':
    print(BackTrack(3,'abc'))