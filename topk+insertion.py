import time

def insertion_sort(elements):
	for i in range(1, len(elements)):
		key = elements[i]
		j = i-1

		while j >=0 and key[1] > elements[j][1] :
				elements[j+1] = elements[j]
				j -= 1
		elements[j+1] = key

	return elements

def topK(elements, K):
	N = len(elements)
	freq_mp = {}
	for i in range(N):
		if elements[i] in freq_mp:
			freq_mp[elements[i]] += 1
		else:
			freq_mp[elements[i]] = 1

	a = [0] * (len(freq_mp))
	j = 0
	for i in freq_mp:
		a[j] = [i, freq_mp[i]]
		j += 1

	a = insertion_sort(a)

	for i in range(K):
		print(a[i][0])

if __name__ == "__main__":
    elements = [3, 1, 1, 1, 4, 4, 4, 5, 2, 6, 1]
    K = 2
    tic = time.time()
    topK(elements, K)
    toc = time.time()
    print(f'runtime: {toc-tic} seconds')

