import time

def merge(elements, L, R):
    i = j = k = 0 
    while i < len(L) and j < len(R):
        if L[i][1] >= R[j][1]:
            elements[k] = L[i]
            i += 1
        else:
            elements[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        elements[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        elements[k] = R[j]
        j += 1
        k += 1

def mergeSort(elements):
    if len(elements) > 1: 
        mid = len(elements)//2 
        L = elements[:mid] 
        R = elements[mid:]
 
        mergeSort(L) 
        mergeSort(R)
        merge(elements, L, R)

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

	mergeSort(a)

	for i in range(K):
		print(a[i][0])

if __name__ == "__main__":
    elements = [3, 1, 1, 1, 4, 4, 4, 5, 2, 6, 1,
                2, 1, 3, 5, 7, 8, 9, 9, 0, 0, 1,
                3, 0, 5, 4, 9, 7, 6, 5, 8, 7, 0,
                1, 9, 6, 3, 8, 4, 5, 5, 9, 5, 2,
                2, 8, 7, 2, 1, 4, 3, 2, 1, 4, 3]
    K = 3
    tic = time.time()
    topK(elements, K)
    toc = time.time()
    print(f'runtime: {toc-tic} seconds')

