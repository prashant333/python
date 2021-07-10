#!/bin/python3

import string
#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#


def designerPdfViewer(h, word):
    # Write your code here
    val = []
    letters = [i for i in string.ascii_lowercase]
    new_word = list(word)
    for i in range(len(new_word)):
        x = letters.index(new_word[i])
        y = h[x]
        val.append(y)
    print(val)
    return max(val) * len(word)


if __name__ == '__main__':

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    print(result)
