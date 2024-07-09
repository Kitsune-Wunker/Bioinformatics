# DNA Toolset/Code testing file
from DNAToolkit import *
import random

# random DNA sequence
randDNAStr = ''.join([random.choice(Nucleotides)
                        for nuc in range(50)])

DNAStr = validateSeq(randDNAStr)

print(f'\nSequqnce: {DNAStr}\n')
print(f'[1] + Sequence Length: {len(DNAStr)}\n')
print(f'[2] + Nucleotide Frequency: {countNucFrequency(DNAStr)}\n')
print(f'[3] + DNA/RNA Transcription: {transcription(DNAStr)}\n')
print(f"[4] + DNA + Reverse Complement:\n5' {DNAStr} 3'\n")
print(f"3' {reverse_complement(DNAStr)} 5'\n")
