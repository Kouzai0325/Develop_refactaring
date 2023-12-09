from random import randint


def print_random():
    """0～1億の範囲のランダムな数の100万個のリストから0～1億個の範囲のランダムな数の100個のリストが含まれていれば表示する
    """
    base_set = set(randint(0, 100000000) for _ in range(1000000))
    checked_list = [randint(0, 100000000) for _ in range(100)]

    for temp in checked_list:
        if temp in base_set:
            print(f'temp:{temp} in a')


if __name__ == '__main__':
    print_random()
