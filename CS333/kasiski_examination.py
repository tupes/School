
from collections import Counter


MAX_KEY_LENGTH = 16


# ////////////////////////
# PUBLIC
# ////////////////////////

def kasiskiExamination(ciphertext):
	repeated_seq_spacings = getRepeatedSeqSpacings(ciphertext)
	seq_factors = getSeqFactors(repeated_seq_spacings)
	factor_counts = getMostCommonFactors(seq_factors)
	return [factor for (factor, count) in factor_counts]

# ////////////////////////
# PRIVATE
# ////////////////////////

def getRepeatedSeqSpacings(message):
	""" Goes through the message and finds any 3 to 5 letter sequences
	that are repeated. Returns a dict with the keys of the sequence and
	values of a list of spacings (num of letters between the repeats)"""

	seq_spacings = {}
	for seq_length in range(3, 6):
		message_end = len(message) - seq_length
		for seq_start in range(message_end):
			seq_end = seq_start + seq_length
			seq = message[seq_start : seq_end]
			for i in range(seq_end, message_end):
				if message[i: i + seq_length] == seq:
					seq_spacings.setdefault(seq, []).append(i - seq_start)
	return seq_spacings

def getSeqFactors(seq_spacings):
	seq_factors = {}
	for seq in seq_spacings:
		seq_factors[seq] = []
		for spacing in seq_spacings[seq]:
			seq_factors[seq].extend(getUsefulFactors(spacing))
	return seq_factors

def getUsefulFactors(num):
	if num < 2: 
		return []
	return list(set([i for i in range(2, MAX_KEY_LENGTH + 1) if num % i == 0 and i != 1]))

def getMostCommonFactors(seq_factors):
	factor_counts = getFactorCounts(seq_factors)
	return getFactorsByCount(factor_counts)

def getFactorCounts(seq_factors):
	factor_counts = Counter()
	for factor_list in seq_factors.values():
		for factor in factor_list:
			factor_counts[factor] += 1
	return factor_counts

def getFactorsByCount(factor_counts):
	return sorted(factor_counts.items(), key=lambda x: x[1], reverse=True)
