import matplotlib.pyplot as plt
import csv
import time
import sys
sys.setrecursionlimit(999999999)

#--------------------------------Read file
def read_file():
    data = [] 
    with open('5k.csv','r') as myfile:
        read = csv.reader(myfile)
        data = list(read)

    for i in range(1, len(data)):
        for j in range(2, len(data[i])):
            data[i][j] = float(data[i][j])

    return data


#-----------------------------Insertion Sort
def insertion_sort(data, sortby):
    
    for i in range(0, len(data)):
        key = data[i]
        j = i - 1           
        while j >= 0 and key[sortby] < float(data[j][sortby]):
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data


#------------------------------Merge Sort
def merge(left, right, column):
    left_index = 0
    right_index = 0
    result = []

    while left_index < len(left) and right_index < len(right) :
        if left[left_index][column] < right[right_index][column]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result += left[left_index:]
    result += right[right_index:]
    return result

def merge_sort(data, column):

    if len(data) <= 1: 
        return data

    half = len(data) // 2
    left =merge_sort(data[:half], column)
    right = merge_sort(data[half:], column)
    return merge(left, right, column)



#------------------------Quick Sort
def partition(data, p, r, sortby):

    i = p - 1
    pivot = data[r][sortby]
    for j in range(p, r):
        if data[j][sortby] <= pivot:
            i = i + 1
            data[i], data[j] = data[j], data[i]
    data[i + 1], data[r] = data[r], data[i + 1]
    return i 

#implement the quick sort algorithum with tail recursion because of time consumption
def quick_sort(data, p, r, sortby):

    while p < r:
        q = partition(data, p, r, sortby)
        if q-p < r-q:
            quick_sort(data, p, q-1, sortby)
            p = q+1
        else:
            quick_sort(data, q+1, r, sortby)
            r = q-1


def Main():
    print("------------------WELCOME-------------------------")
    print("1:Open\n2:High\n3:Low\n4:Close")
    sortby = 1+int(input("Select any 1-4 :"))

    if sortby > 1 and sortby < 6:

        data = read_file()
        length = len(data)
        print("Read data is")
        for row in data:
            print(row)
        
        data.clear()

        print("\n......Wait till data has been sorted thorugh all algorithms...")
        print("Graph will be shown for Analysis")
        cordinates = [[] for i in range(6)]
        for size in range(0, length, 100):

            #insertion
            data = read_file()
            data.pop(0)
            start = time.process_time()
            insertion_sort(data[1:size], sortby)
            end = time.process_time()
            T = end - start
            cordinates[0].append(T)
            cordinates[1].append(size)
            data.clear()
    
            #Merge
            data = read_file()
            data.pop(0)
            start = time.process_time()
            merge_sort(data[1:size], sortby)
            end = time.process_time()
            T = end - start
            cordinates[2].append(T)
            cordinates[3].append(size)
            data.clear()

            #Quick
            data = read_file()
            data.pop(0)
            start = time.process_time()
            quick_sort(data, 1, size-1, sortby)
            end = time.process_time()
            T = end - start
            cordinates[4].append(T)
            cordinates[5].append(size)
            data.clear()

        #Plot
        plt.plot(cordinates[1], cordinates[0], "-b", label="Insertion sort")
        plt.plot(cordinates[3], cordinates[2], "-r", label="Merge sort")
        plt.plot(cordinates[5], cordinates[4], "-g", label="Quick sort")
        plt.legend(loc = "upper left")
        plt.grid(True)
        plt.xlabel("n")
        plt.ylabel("Time(S)")
        plt.title("Analysis Of Algorithms")
        plt.show()

    else:
        print("Wrong insert")


#drive code:
Main()