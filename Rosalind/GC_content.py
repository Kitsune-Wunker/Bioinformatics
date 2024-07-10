# Read data from file
def readFile(filepath):
    with open(filepath, 'r') as f:
        return [l.strip() for l in f.readlines()]

def gc_content(seq):
    return ((seq.count('C') + seq.count('G')) / len(seq) * 100)

FASTAFile = readFile("test_data/gc_content.txt")

FASTADict = {}

FASTALabel = ""

# Clean data

for line in FASTAFile:
    if '>' in line:
        FASTALabel = line
        FASTADict[FASTALabel] = ""
    else:
        FASTADict[FASTALabel] += line

# Format data
# Run GC content
RESULTDict  = {key: gc_content(value) for (key, value) in FASTADict.items()}

MaxGCKey = max(RESULTDict, key=RESULTDict.get)
# Results

print(f"{MaxGCKey[1:]}\n{RESULTDict[MaxGCKey]}")
