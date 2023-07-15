def PatternCount(DNA, pattern):

    count = 0

    for i in range(0, len(DNA) - len(pattern) + 1, 1):
        if DNA[i:i + 3: 1] == pattern:
            count += 1

    return count