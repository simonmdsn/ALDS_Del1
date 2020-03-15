"""
DM507 Algoritmer og datastrukturer
Projekt, del I
Lavet af Joachim Henrik Bülow(jobul18), Sofie Louise Madsen(sofma18) og Simon Soele Madsen(smads18)
@ University of Southern Denmark
Afleveres d. 16.03.2020
"""

import math

def minHeapify(A, i):
    l = left(i)
    r = right(i)
    if l < len(A) and A[l] < A[i]:
        smallest = l
    else:
        smallest = i
    if r < len(A) and A[r] < A[smallest]:
        smallest = r
    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i]
        minHeapify(A, smallest)


def extractMin(A):
    A[0], A[len(A) - 1] = A[len(A) - 1], A[0]
    min = A.pop(len(A) - 1)
    minHeapify(A, 0)
    return min


def insert(A, e):
    A.append(e)
    i = len(A) - 1
    while i > 0 and A[parent(i)] > A[i]:
        A[i], A[parent(i)] = A[parent(i)], A[i]
        i = parent(i)


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def parent(i):
    return math.floor((i - 1) / 2)