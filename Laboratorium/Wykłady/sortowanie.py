import os
import heapq
from timeit import default_timer as timer

def QucikSort():
    List1 = [10,12,3,2,1,5,12]

    print(List1)
    print("Po sortowaniu Quick sort:")
    StartTime = timer()
    List1.sort()
    TimeEnd = timer()
    print(List1)
    print("Czas ",TimeEnd - StartTime)
def HeapSort():
    Lista2 = [10,12,3,2,1,5,12]
    print()
    print(Lista2)
    print("Po sortowaniu Heap Sort: ")
    StartTime1 = timer()
    heapq.heapify(Lista2)
    TimeEnd1 = timer()
    print(Lista2)
    print("Czas Heap Sort",TimeEnd1 - StartTime1)

QucikSort()
HeapSort()