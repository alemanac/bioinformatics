def PatternIndex(pattern, DNA):
    Indices = []

    for i in range(len(DNA)):
        if DNA[i:i + len(pattern):1] == pattern:
            Indices.append(i)

    return Indices


#test
def TestMe(GenomeFileName):
    
    with open(GenomeFileName) as file:
        genome = file.read()

    print(PatternIndex("ATGATCAAG", genome))


TestMe("Coursera/Vibrio_cholerae.txt")