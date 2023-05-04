from itertools import permutations

def orderOfPresentation(n, input):
	arr = [i for i in range(1, n + 1)]
	nPr = permutations(arr, n)
	print(list(nPr).index(input))

orderOfPresentation(3, (2, 3, 1))
orderOfPresentation(5, (1, 3, 2, 4, 5))
