import sys
import os


def prime(s):
    count = 0
    for i in range(1, s):
        if s % i == 0:
            count += 1
        print(count)
    if count <= 1:
        return True
    return False



    # for n in range(2, s):
    #     if n > 1:
    #         if s % n == 0:
    #             return False
    #         else:
    #             return True


def solution(s):
    return prime(s)


if __name__ == "__main__":
    solution(40)