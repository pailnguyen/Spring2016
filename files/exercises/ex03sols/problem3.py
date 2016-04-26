seq1 = input("Enter sequence 1: ")
seq2 = input("Enter sequence 2: ")
seq3 = input("Enter sequence 3: ")
seq4 = input("Enter sequence 4: ")

seqs = [seq1, seq2, seq3, seq4]
positions = []

for i in range(len(seq1)):
	counts = [0, 0, 0, 0]
	for seq in seqs:
		counts["ACGT".index(seq[i])] += 1
	positions.append(counts)
	print(counts)

consensus = []
for counts in positions:
	consensus.append("ACGT"[counts.index(max(counts))])
print("Consensus seq is: " + "".join(consensus))
