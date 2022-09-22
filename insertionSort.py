def main(n):
    print(f'unordered list {n}')
    for j in range(1, len(n)):
        key = n[j]
        i = j - 1
        while i > 0 and n[i] > key:
            print(i)
            n[i+1] = n[i]
            i += 1
    n[i + 1] = key
    print(f'Ordered list: {n}')

if __name__ == '__main__':
    n = [3, 6, 1, 9, 0]
    main(n)