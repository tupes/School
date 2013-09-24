from collections import Counter

#Statistics with Numeric Lists

def average(data):
	if not data: return None
	return round(sum(data) / len(data), 2)


def moment(data, powers):
	if not data: return None
	mean = sum(data) / len(data)
	return [average([(datum - mean)**power for datum in data]) for power in powers]


def mode(data):
	ordered = Counter(data).most_common()
	return sorted([round(value, 2) for value, count in ordered if count == ordered[0][1]])


def histogram(data, ranks):
	bins = ranks + [float('infinity')]
	return [sum([1 for datum in data if datum <= bins[b] and (bins[b-1] < datum or b == 0)]) for b in range(len(bins))]

