# python3
# Vadims Belovs 221RDB129


def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)

    n = len(data)

    for i in range(n // 2, -1, -1):
        heap(i, data, swaps)

    return swaps


def heap(i, data, swaps):
    n = len(data)
    min_index = i

    left = 2 * i + 1
    if left < n and data[left] < data[min_index]:
        min_index = left

    right = 2 * i + 2
    if right < n and data[right] < data[min_index]:
        min_index = right

    if i != min_index:
        swaps.append((i, min_index))
        data[i], data[min_index] = data[min_index], data[i]

        heap(min_index, data, swaps)

def main():
    choice = input()

    if 'I' in choice:
        n = int(input())
        data = list(map(int, input().split()))
    if 'F' in choice:
        fpath = input()
        if 'a' not in fpath:
            with open(str("tests/"+fpath)) as f:
                n = int(f.readline())
                data = list(map(int, f.readline().split()))

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
