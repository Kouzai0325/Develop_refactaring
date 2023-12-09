import numpy as np


def print_random():
    base_set = set(np.random.randint(0, 100000000, 1000000))
    checked_list = np.random.randint(0, 100000000, 100)

    for temp in checked_list:
        if temp in base_set:
            print(f"temp:{temp} in a")


if __name__ == "__main__":
    print_random()
