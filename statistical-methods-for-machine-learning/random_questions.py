import random

if __name__ == "__main__":
    all_n = set([i for i in range(1, 64)])
    first = set([4, 5, 6, 7, 10, 17, 20, 27, 28, 31, 33, 34, 37, 38, 46, 53, 57, 59, 60, 62])
    second =set([1, 3, 8, 12, 15, 16, 25, 26, 29, 30, 36, 39, 40, 41, 43, 47, 50, 51, 52, 58])

    third = all_n - first - second 
    print(third)
