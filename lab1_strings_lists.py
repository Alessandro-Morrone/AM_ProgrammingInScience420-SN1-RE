dna = 'atgcgatgcgatgcg'
exons = [(2,5), (10,12)]
annot = list(dna.lower())
for s,e in exons:
    for i in range (s,e):
        annot[i] = annot[i].upper()
print(''.join(annot))

counts = {nuc: dna.upper().count(nuc) for nuc in 'ATGC'}
print(counts)
print(dna[::-1])