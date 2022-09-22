import time

def insertion_sort(elementos):
    pass


def topk_fe(elementos, k):
    tic = time.time()
    #insertion_sort(elementos)
    if k <= 0:
        return None

    k_elem = [] # primeiro sempre é o mais frequente.
    ant = elementos[0]
    i = 1
    while len(k_elem) < k:
        if elementos[i] != ant:
            k_elem.append(elementos[i])
        ant = elementos[i]
        i += 1

    toc = time.time()
    print(k_elem)
    print(f'Tempo de processamento: {abs(tic - toc)} s')

if __name__ == '__main__':
    elementos = [1, 3, 5, 5, 6, 7, 7, 8, 8, 8]
    k = 2
    topk_fe(elementos, k)