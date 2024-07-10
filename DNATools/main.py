# DNA Toolset/Code testing file
from DNAToolkit import *
import random

# random DNA sequence
randDNAStr = ''.join([random.choice(Nucleotides)
                        for nuc in range(50)])

DNAStr = validateSeq(randDNAStr)
#DNAStr = ""

#print(f'\nSequence: {DNAStr}\n')
#print(f'[1] + Sequence Length: {len(DNAStr)}\n')
#print(f'[2] + Nucleotide Frequency: {countNucFrequency(DNAStr)}\n')
#print(f'[3] + DNA/RNA Transcription: {transcription(DNAStr)}\n')
#print(f"[4] + DNA + Reverse Complement:\n5' {DNAStr} 3'\n")
#print(f"3' {reverse_complement(DNAStr)} 5'\n")
#print(f"[5] + GC Content: {gc_content(DNAStr)}%\n")
#print(f"[6] + GC Content in subsection k=5: {gc_content_subset(DNAStr, k=5)}\n")
#print(f"[7] + Amino Acid Sequence of DNA: {translate_seq(DNAStr, 0)}\n")
#print(f"[8] + Codon Frequency (L): {codon_usage(DNAStr, 'L')}\n")
print(f"[9] + Reading Frames:\n")
for frame in gen_reading_frames(DNAStr):
    print(frame)

print('\n[10] + All proteins in 6 open reading frames:')
for prot in all_proteins_from_prfs(AH002844, 0, 0, True):
    print(f'{prot}')
