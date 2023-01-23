def Probable(dna, k, profile):
    row_map = {
        'A': 0,
        'C': 1,
        'G': 2,
        'T': 3,
    }

    max_prob = 0
    most_probable_kmer = ""
    for i in range(len(dna)-k+1):
        kmer = dna[i:i+k]
        prob = 1
        for j, char in enumerate(kmer):
            row = row_map[char]
            prob *= profile[row][j]
        if prob > max_prob:
            max_prob = prob
            most_probable_kmer = kmer

    return most_probable_kmer

def Pr(pattern, dna):
    p = 1
    for i in range(len(dna)-len(pattern)+1):
        p = p * dna[pattern[i][i]]
    return p 


text = """
0.2 0.2 0.3 0.2 0.3
0.4 0.3 0.1 0.5 0.1
0.3 0.3 0.5 0.2 0.4
0.1 0.2 0.1 0.1 0.2
"""
text = text.strip()

lst = text.split('\n')
lst = list(map(str.split, lst))
lst = [list(map(float, row)) for row in lst]

matrix = lst
dna = "ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT"

print(matrix)

#convert list into a 5X4 matrix 

print(Probable(dna, 5, matrix))
