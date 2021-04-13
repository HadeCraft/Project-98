import os
import shutil

def swapFileData():
    source = input("Enter source file name!!!:")
    victim = input("Enter victim file name!!!:")

    data_a = source + '/'
    data_b = victim + '/'

    with open(file1, 'r') as a:
    data_a = a.read()

    with open(file1, 'w') as a:
    a.write(data_b) 