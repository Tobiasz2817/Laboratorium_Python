#Quick And Heap Sort , Wczytywanie liczb z pliku txt do tablicy i convert ze stringa na Inta
import os
import heapq
from timeit import default_timer as timer
from collections import deque
def QucikSort():
    List1 = LoadNumbersFromFile()
    print(List1)
    print("Po sortowaniu Quick sort:")
    StartTime = timer()
    List1.sort()
    TimeEnd = timer()
    print(List1)
    print("Czas ",TimeEnd - StartTime)

def HeapSort():
    List2 = LoadNumbersFromFile()
    print()
    print(List2)
    print("Po sortowaniu Heap Sort: ")
    StartTime1 = timer()
    heapq.heapify(List2)
    TimeEnd1 = timer()
    print(List2)
    print("Czas Heap Sort",TimeEnd1 - StartTime1)
    

def LoadNumbersFromFile():   
    foo = open("Variable.txt")
    List_Number = []
    line = foo.readline()
    while line!="":
        n_line = line.replace("\n", "")
        List_Number.append(int(n_line))
        line = foo.readline()
    return List_Number


QucikSort()
HeapSort()
LoadNumbersFromFile()