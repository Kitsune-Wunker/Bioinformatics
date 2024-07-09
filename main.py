# DNA Toolset/Code testing file
from DNAToolkit import *
import random

# random DNA sequence
randDNAStr = ''.join([random.choice(Nucleotides)
                        for nuc in range(20)])

DNAStr = validateSeq(randDNAStr)
print(countNucFrequency(DNAStr))
